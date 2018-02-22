# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 03:25:58 2018

@author: User
"""
import os
import csv
#activate csv
x = open("election_data_1.csv")
#dict
reader = csv.DictReader(x)
data = [row for row in reader]
sum = []
# for loop total votes
for row in data:
	sum.append(row["Voter ID"])
print("Total Votes: " + str(len(sum)))
totcand = []
cand = []
for row in data:
	totcand.append(row["Candidate"])
for x in totcand:
	if x not in cand:
		cand.append(x)
print("Candidates " + str(cand))
#list
voteseach = dict(Counter(totcand))
votes = list(voteseach.values())
names = list(voteseach.keys())
y = 0
# table
while y < len(names):
	print(names[y] + ": "+ str(int(int(votes[y]) / len(sum) * 100)) + "% " + "("+ str(int(votes[y]))+ ")")
	y = y+1
# max() votes