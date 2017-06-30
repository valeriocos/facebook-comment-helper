#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'

import facebook
import multiprocessing
import requests
import multiprocessing_util
from post_analyzer import PostAnalyzer


class PostAnalyzerMain(multiprocessing.Process):

    MAX_QUEUE_SIZE = 50
    WAITING_TIME = 5
    NUM_PROCESSES = 5

    def __init__(self, token, target_user, posts_queue, comments_queue, log_queue):
        multiprocessing.Process.__init__(self)

        self._token = token
        self._target_user = target_user

        self._posts_queue = posts_queue
        self._comments_queue = comments_queue
        self._log_queue = log_queue

        self._graph = self._get_facebook_graph()
        profile = self._graph.get_object(self._target_user)
        self._target_user_id = profile.get('id')

    def _get_facebook_graph(self):
        return facebook.GraphAPI(access_token=self._token, version=PostAnalyzer.API_VERSION)

    def _get_property(self, obj, p):
        try:
            found = obj[p]
        except:
            found = None

        return found

    def _fetch_next_page(self, obj):
        try:
            next = obj['paging']['next']
            obj = requests.get(next).json()
        except:
            obj = []
        finally:
            return obj

    def run(self):
        try:
            multiprocessing_util.start_consumers(self.NUM_PROCESSES, self._posts_queue)

            posts = self._graph.get_connections(self._target_user_id, 'posts')
            while posts:
                for p in posts['data']:
                    try:
                        post_id = p['id']
                        post_message = p['message']
                        #post_created_at = p['created_time']

                        post_processor = PostAnalyzer(self._token, self._target_user_id,
                                                      post_id, post_message, self._comments_queue, self._log_queue)
                        self._posts_queue.put(post_processor)

                        self._log_queue.put("Adding post[" + str(post_id) + "]:" + (post_message[0:20]).replace("\n", "") + "..., current qsize: " + str(self._posts_queue.qsize()) + "\n")

                        multiprocessing_util.check_queue_size(self._posts_queue, PostAnalyzerMain.MAX_QUEUE_SIZE, PostAnalyzerMain.WAITING_TIME)
                    except Exception as ex:
                        template = "The post " + str(p['id']) + " has been skipped. An exception of type {0} occurred. Arguments:{1!r}"
                        message = template.format(type(ex).__name__, ex.args)

                        self._log_queue.put(message.replace("\n", "") + "\n")

                        continue

                posts = self._fetch_next_page(posts)

            multiprocessing_util.add_poison_pills(self.NUM_PROCESSES, self._posts_queue)
        except Exception:
            do_nothing = True



