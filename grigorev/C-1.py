#!/usr/bin/python
from __future__ import division
from io import BytesIO

vowels = list("aeiouy")

def anagram_generator(head, target_length, unique_letters, letter_count):
	if len(head) < target_length:
		for letter in unique_letters:
			if head.count(letter) < letter_count[letter]: # not all instances in head
				if len(head) > 0 and head[-1] in vowels and letter in vowels: # consecutive vowels
					continue
				for anagram in anagram_generator(head + [letter], target_length, unique_letters, letter_count):
					yield anagram
	else:
		yield head

with open("anagrams.in") as infile:
	word = infile.readline().strip().lower()
	letters = sorted(list(word))

# calculate frequencies of letters only once (for speed gain)
letter_count = {
	letter: letters.count(letter)
	for letter in set(letters)
}

with open("anagrams.out", "w") as outfile:
	anagrams = anagram_generator(
		head = [],
		target_length = len(letters),
		unique_letters = sorted(set(letters)),
		letter_count = letter_count
	)
	for anagram in anagrams:
		outfile.write("".join(anagram) + "\n")
