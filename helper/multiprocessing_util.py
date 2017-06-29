#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'

import multiprocessing
import time


def empty_queue(q):
    while not q.empty():
        q.get()


def check_queue_size(q, max_q, sleep_time):
    while q.qsize() > max_q:
        time.sleep(sleep_time)


def add_poison_pills(num_consumers, task_queue):
    for i in xrange(num_consumers):
        task_queue.put(None)


def start_consumers(num_consumers, task_queue):
    consumers = [Consumer(task_queue) for i in xrange(num_consumers)]
    for w in consumers:
        w.start()


class Consumer(multiprocessing.Process):
    """
    This class provides multiprocessing utilities
    """

    def __init__(self, task_queue):
        """
        :type task_queue: Object
        :param task_queue: the queue of the tasks
        """
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue

    def run(self):
        """
        runs the consumer's task
        """
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                break

            answer = next_task()

        return