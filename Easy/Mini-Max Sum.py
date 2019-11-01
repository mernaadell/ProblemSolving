#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr=sorted(arr)
    print(sum(arr)-arr[4],sum(arr)-arr[0])
   
