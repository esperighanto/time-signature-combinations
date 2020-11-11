#Tommy Royall, 11/10/2020.

import math
from itertools import combinations_with_replacement

all_text_printed = False #Set this to False to just have results printed, or to True to have all of the information printed.
target = 32 #A good default, many verses, choruses, etc. are 32 bars.
constituents = [4, 5, 6, 7] #These are the examples given since they're rather common divisions.
repetitions_maximum = math.ceil(target/constituents[0])
repetitions_minimum = math.floor(target/constituents[-1])
results = []

for i in range(repetitions_maximum - repetitions_minimum + 1):
    if(all_text_printed):
        print("With r:", (i + repetitions_minimum))
    constituents_comb = combinations_with_replacement(constituents, (i + repetitions_minimum))
    for i in list(constituents_comb): #Check through all combinations created.
        if(all_text_printed):
            print(str(i) + " Summated:", sum(i))
        if(sum(i) == target): #Check to see if sum is the target we're looking for.
            results.append(i)
    if(all_text_printed):
        print(" ")

if(all_text_printed):
    print("_________")

print(results)
