#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'

import multiprocessing
import codecs
import datetime


class QueueLogger(multiprocessing.Process):

    LOG_EXTENSION = ".log"

    def __init__(self, log_queue):
        multiprocessing.Process.__init__(self)
        self._log_queue = log_queue
        self._log_path = "fb-util.log"

        self._init_log()

    def _init_log(self):
        f = open(self._log_path, "w+")
        f.close()

    def run(self):
        flag = True
        while flag:
            try:
                next_comment = self._log_queue.get()

                if next_comment:
                    with codecs.open(self._log_path, "a+", "utf-8") as log:
                        log.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ":" + next_comment)
                else:
                    flag = False
            except Exception:
                flag = False