#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'


from post_analyzer_main import PostAnalyzerMain
from queue_logger import QueueLogger
import multiprocessing
import multiprocessing_util
import webbrowser


class FacebookCommentHelper():

    def __init__(self, token, target_user):
        m = multiprocessing.Manager()
        self._posts_queue = multiprocessing.Queue()
        self._comments_queue = m.Queue()

        self._url = "https://www.facebook.com/"
        self._start_browser()

        self._log_queue = m.Queue()
        self._logger = QueueLogger(self._log_queue)
        self._logger.start()

        self._analyzer = PostAnalyzerMain(token, target_user, self._posts_queue, self._comments_queue, self._log_queue)
        self._analyzer.start()

    def _start_browser(self):
        webbrowser.open(self._url, new=1)

    def comments_queue_is_empty(self):
        try:
            check = self._comments_queue.qsize() == 0
        except:
            check = True
        finally:
            return check

    def process_next_comment(self):
        next_comment = self._comments_queue.get()
        self._log_queue.put("Removing comment from the queue, current size: " + str(self._comments_queue.qsize()) + "\n")
        webbrowser.open_new_tab(self._url + next_comment.get('id'))

    def stop_activity(self):
        self._log_queue.put("Closing application...\n")
        multiprocessing_util.empty_queue(self._posts_queue)
        multiprocessing_util.add_poison_pills(PostAnalyzerMain.NUM_PROCESSES, self._posts_queue)

        multiprocessing_util.empty_queue(self._comments_queue)

        multiprocessing_util.empty_queue(self._log_queue)
        multiprocessing_util.add_poison_pills(1, self._log_queue)






