#!/usr/bin/python
from collections import defaultdict

GOLD, SILVER, BRONZE = 0, 1, 2

def count_medals(medal_kits):
	medals = defaultdict(list)
	gross = defaultdict(dict)
	for medal_kit in medal_kits:
		countries = medal_kit.split()
		for medal in (GOLD, SILVER, BRONZE):
			medals[medal].append(countries[medal])
	for medal in (GOLD, SILVER, BRONZE):
		contenders = set(medals[medal])
		for contender in contenders:
			gross[medal][contender] = medals[medal].count(contender)
	return gross

def keys_by_value(dictionary, value):
	for k, v in dictionary.iteritems():
		if v == value:
			yield k

def calculate_weights(medal_count, base):
	based = (base**2, base, 1)
	weights = defaultdict(int)
	for medal in (GOLD, SILVER, BRONZE):
		for country in medal_count[medal]:
			weights[country] += medal_count[medal][country] * based[medal]
	return weights


with open("olympic.in") as olympic_in:
	lines = olympic_in.readlines()

kit_amount = int(lines[0].strip())
medal_count = count_medals(lines[1:])
weights = calculate_weights(medal_count, base = kit_amount+1)
max_weight = max(weights.values())
contenders = list(keys_by_value(weights, max_weight))
winner = min(contenders)

with open("olympic.out", "w") as olympic_out:
	olympic_out.write(winner)
