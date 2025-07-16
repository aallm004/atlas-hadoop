#!/bin/bash

# Creates the /holbies directory in HDFS
hdfs dfs -mkdir /holbies

# Create the /holbies/input directory
hdfs dfs -mkdir /holbies/input