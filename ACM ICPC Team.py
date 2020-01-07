#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    l = []
    size = len(topic)
    max_topics_numbers = 0
    teams = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            topics = str("{0:b}".format((int(topic[i], 2) | int(topic[j], 2))))
            if topics.count("1") > max_topics_numbers:
                max_topics_numbers = topics.count("1")
                teams = 1
            else:
                if topics.count("1") == max_topics_numbers:
                    teams += 1
    l.append(max_topics_numbers)
    l.append(teams)
    return l



            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
