#!/usr/bin/python
from __future__ import division
from io import BytesIO

vowels = list("aeiouy")

def anagram_generator(head, letters, letterset, lettercount):
	if len(head) < len(letters):
		for letter in letterset: # consider unique letters only
			if head.count(letter) < lettercount[letter]: # not all instances in head
				if len(head) > 0 and head[-1] in vowels and letter in vowels: # consecutive vowels
					continue
				for anagram in anagram_generator(head + [letter], letters, letterset, lettercount):
					yield anagram
	else:
		yield head

with open("anagrams.in") as infile:
#   with BytesIO("catt") as infile:
	word = infile.readline().strip().lower()
	letters = sorted(list(word))

lettercount = {
	letter: letters.count(letter)
	for letter in set(letters)
}

with open("anagrams.out", "w") as outfile:
	for anagram in anagram_generator([], letters, sorted(set(letters)), lettercount):
		outfile.write("".join(anagram) + "\n")
