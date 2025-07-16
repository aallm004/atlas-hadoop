#!/usr/bin/env python2.7
"""Module for download file"""
import os
from snakebite.client import Client


def download(l):
    """Function that retrieves from the HDFS files listen in l and store them
    in the home /tmp folder of the user"""
    client = Client('localhost', 9000)

    # Iterate through each file path in the list
    for hdfs_file_path in l:
            
        # Extract filename from the HDFS path
        filename = os.path.basename(hdfs_file_path)

        # Create local destination path in /tmp
        local_file_path = os.path.join('/tmp', filename)

        # Show success and final output
        for result in client.copyToLocal([hdfs_file_path], local_file_path):
            print({
                'path': local_file_path,
                'result': True,
                'error': '',
                'source_path': hdfs_file_path
            })
