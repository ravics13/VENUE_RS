
# This script is meant for calculating the weights corresponding to journals.
# On the basis of these we will rank the recommended venues.
# Assumptions made
# 1. Input will be the score vector of a training paper corresponding to each journal.
# Assume we have 5 features and 3 venues
# Then each paper will ne represented as 
# s1_j1, s2_j1, s3_j1, s4_j1, s5_j1
# s1_j2, s2_j2, s3_j2, s4_j2, s5_j2
# s1_j3, s2_j2, s3_j3, s4_j3, s5_j3
# s<x>_j<y> represents score of xth feature calculated using lists  of venue y.

import os
from os.path import isfile, join
import numpy as np;
import math

n=5 # Replace n by the number of features
venues = 3 # Number of venues
weights = np.ones(n)  
weights = weights/n
learning_rate = 0.25
actauVenueIndex = 0

def sigmoid(x):
	return 1/(1+math.e**-x)

def inputToSigmoid(score_matrix, indexUnderConsideration):
	x = 0
	for i in range(0, n):
		x = x + weights[i]*(score_matrix[actauVenueIndex][i] - score_matrix[indexUnderConsideration][i])
	return x

def update_weights(score_matrix):
	diff = np.zeros(n)
	for i in range(0, n):
		for j in range(0, venues):
			if(j != actauVenueIndex):
				x = inputToSigmoid(score_matrix, j)
				diff[i] = diff[i] + sigmoid(x)*(1-sigmoid(x))*(score_matrix[actauVenueIndex][i] - score_matrix[j][i])	
		weights[i] = weights[i] + learning_rate*diff[i]
	if(not np.any(diff)):
		return False
	return True 

os.chdir('/Users/rsonam/Personal/VRS/score_matrix')
for i in sorted(os.listdir(os.getcwd())):
	print i;
	score_matrix = np.loadtxt(i, delimiter=',', unpack=False)
	if(update_weights(score_matrix)):
		#continue t
	else:
		#write weights in a file
		#break


print(weights)
