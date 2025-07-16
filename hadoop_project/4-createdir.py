#!/usr/bin/env python2.7
"""Module for creating directory"""
from snakebite.client import Client

def createdir(l):
    """creates the directories listen on l within HDFS"""
    client = Client("localhost", 9000)

    # Iterate through each directory path in list
    for directory in l:
        # Create directory using mkdir with create_parent=True
        # create_parent=True creates parent dir if they don't exist
        for result in client.mkdir([directory], create_parent=True):
            print(result)