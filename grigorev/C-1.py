#!/usr/bin/python
from __future__ import division
from io import BytesIO

vowels = list("aeiouy")

def anagram_generator(head, letters):
	if len(head) < len(letters):
		for letter in sorted(set(letters)): # consider unique letters only
			if head.count(letter) < letters.count(letter): # not all instances in head
				if len(head) > 0 and head[-1] in vowels and letter in vowels: # consecutive vowels
					continue
				for anagram in anagram_generator(head + [letter], letters):
					yield anagram
	else:
		yield head

with open("anagrams.in") as infile:
	word = infile.readline().strip().lower()
	letters = sorted(list(word))

with open("anagrams.out", "w") as outfile:
	for anagram in anagram_generator([], letters):
		outfile.write("".join(anagram) + "\n")
