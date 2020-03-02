#!/usr/bin/env python3	
    
def example1(input):
    odds = [i for i in input.split(" ") if int(i) % 2 != 0]
    even = [i for i in input.split(" ") if int(i) % 2 == 0]
    ans = [odds,even][len(even)==1][0]
    return input.split(" ").index(ans)+1


def example2(s):
	return min(len(word) for word in s.split())


def example3(l):
	return [i for i in l if not isinstance(i, str)]
