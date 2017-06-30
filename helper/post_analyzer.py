#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'

import facebook
import requests
import multiprocessing_util


class PostAnalyzer(object):

    API_VERSION = '2.7'
    MAX_QUEUE_SIZE = 50
    WAITING_TIME = 5

    def __init__(self, token, target_user_id, post_id, post_message, comments_queue, log_queue):
        self._token = token
        self._target_user_id = target_user_id
        self._post_id = post_id
        self._post_message = post_message
        self._comments_queue = comments_queue
        self._log_queue = log_queue

        self._graph = self._get_facebook_graph()

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

    def __call__(self):
        try:
            comment_count = 0
            comments = self._graph.get_connections(id=self._post_id, connection_name='comments', limit=100)
            while comments:

                for comment in comments['data']:
                    try:
                        comment_id = comment['id']
                        comment_created_at = comment['created_time']
                        comment_message = comment['message']
                        comment_from = comment['from']
                        user_name = comment_from['name']
                        user_id = comment_from['id']

                        attachment = self._graph.get_object(id=comment_id, fields='attachment').get('attachment')

                        if attachment:
                            attachment_description = self._get_property(attachment, 'description')
                            attachment_type = self._get_property(attachment, 'type')
                            attachment_url = self._get_property(attachment, 'url')

                            if attachment_type in ('photo', 'video') and user_id != self._target_user_id:
                                self._comments_queue.put({'id': comment_id, 'created_at': comment_created_at})

                                self._log_queue.put("Adding comment[" + str(comment_id) + "] to the queue, current qsize: " + str(self._comments_queue.qsize()) + "\n")
                        # if '?' in comment_message:
                        #     self._comments_queue.put({'id': comment_id, 'created_at': comment_created_at})

                        comment_count += 1
                        multiprocessing_util.check_queue_size(self._comments_queue, PostAnalyzer.MAX_QUEUE_SIZE, PostAnalyzer.WAITING_TIME)
                    except Exception as ex:
                        template = "The comment " + str(comment['id']) + " has been skipped. An exception of type {0} occurred. Arguments:{1!r}"
                        message = template.format(type(ex).__name__, ex.args)

                        self._log_queue.put(message.replace("\n", "") + "\n")
                        continue

                comments = self._fetch_next_page(comments)

            self._log_queue.put("Finishing post[" + str(self._post_id) + "]:" + (self._post_message[0:20]).replace("\n", "") + "..., " + str(comment_count) + " comments analyzed\n")
        except Exception:
            do_nothing = True