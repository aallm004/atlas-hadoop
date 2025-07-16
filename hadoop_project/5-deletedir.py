#!/usr/bin/env python2.7
"""module for delete dir"""
from snakebite.client import Client


def deletedir(l):
    """Function that reemoves the directories listen on l within HDFS"""
    client = Client("localhost", 9000)

    # Iterate through each directory path in the list
    for directory in l:
        # Delete directory using delete method with recurse=True
        # recurse=True allows deletion of non-empty directories
        for result in client.delete([directory], recurse=True):
            # Print the result dictionary containing path
            print(result)