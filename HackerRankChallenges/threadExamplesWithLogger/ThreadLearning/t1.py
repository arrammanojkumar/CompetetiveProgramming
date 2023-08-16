#!/bin/python3

__author__ = "Manoj Kumar Arram"

# Python program to illustrate the concept
# of threading
import logging
import threading
import os
import time

from threadExamplesWithLogger.utils import Utils

t1Logger = logging.getLogger("cal_application.t1pyLogger")


class ThreadsExample:
    def __init__(self):
        self.threadExampleLogger = logging.getLogger("cal_application.t1pyLogger.ThreadsExample")
        self.s = None

    def task1(self, s):
        self.s = s
        self.threadExampleLogger.info(
            "Task 1 assigned to thread: {} and s {}".format(threading.current_thread().name, s))
        time.sleep(5)
        self.threadExampleLogger.info("Utils {} Caller {}".format(s, Utils.get_s(s)))
        self.threadExampleLogger.info("ID of process running task 1: {}".format(threading.current_thread().ident))

    def task2(self):
        self.threadExampleLogger.info("Task 2 assigned to thread: {}".format(threading.current_thread().name))
        self.threadExampleLogger.info("ID of process running task 2: {}".format(threading.current_thread().ident))


class CallThread:

    def __init__(self):
        self.callThreadLogger = logging.getLogger("cal_application.t1pyLogger.callThread")
        # print ID of current process
        self.callThreadLogger.info("ID of process running main program: {}".format(os.getpid()))

        # print name of main thread
        self.callThreadLogger.info("Main thread name: {}".format(threading.main_thread().name))

    def callT(self):
        t = ThreadsExample()
        self.callThreadLogger.info("created threadobject t and Task 1 calling daemon")
        threading.Thread(target=t.task1, args=[4], daemon=False).start()
        self.callThreadLogger.info("Task2 and calling ")
        threading.Thread(target=t.task1, args=[5]).start()
        t1Logger.info("Process Complted in t1 ")
