#!/bin/python3

__author__ = "Manoj Kumar Arram"


from threadExamplesWithLogger import logger
from threadExamplesWithLogger.ThreadLearning.t1 import CallThread

t = CallThread()
logger.info("Created thread object")
t.callT()
logger.info("Completed Calling thread obejct")
