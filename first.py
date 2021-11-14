#!/usr/bin/env python3

#First testfile Raspberry Pi Zero 1.1 W
#by Anton Grahn

import time
import numpy as np
import statistics as st

def counter():
    tim = []
    counter = 0
    for i in range(100):
        t0 = time.time()
        result = np.sin(counter)
        t1 = time.time()
        print(result)
        counter+=1
        tim.append(t1-t0)
    print("Average compute time sin: ",st.mean(tim))
    tim = []
    counter = 0
    for i in range(100):
        t0 = time.time()
        result =  counter/(counter+13)
        t1 = time.time()
        print(result)
        counter+=1
        tim.append(t1-t0)
    print("Average compute time divide: ",st.mean(tim))
    tim = []
    counter = 0
    for i in range(100):
        t0 = time.time()
        result =  np.arctan2(counter,counter+3)
        t1 = time.time()
        print(result)
        counter+=1
        tim.append(t1-t0)
    print("Average compute time atan2: ",st.mean(tim))
def main():
    print("Hej!")
    counter()
    print("Hejdå!")
if __name__ == "__main__":
    main()
