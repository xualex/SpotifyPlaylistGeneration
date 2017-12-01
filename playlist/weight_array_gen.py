import pandas as pd
from sklearn import preprocessing
import numpy as np
from scipy.spatial.distance import pdist, squareform


#This just gets rid of the warnings that have been annoying me
import warnings
warnings.filterwarnings("ignore")

#This is the file where weights are to be messed with.
#Usage is: 1) normalizeDF 2) createWeightArray
#Function to mess with is: songWeight

#Normalize data frame where song features are stored
def normalizeDf(df):
	min_max_scaler = preprocessing.MinMaxScaler()
	for i in allFeatures: #Change for general df
		df[i] = pd.DataFrame(min_max_scaler.fit_transform(df[i]))
	return df.set_index("songid")


#Creates an n*n array that corresponds to weights on how close 2 songs are
#The ith row and jth column corresponds to relation from the ith song to the jth song
def createWeightArray(df):
    weightArray = np.zeros((df.shape[0],df.shape[0]))
    #Probabilistic weight for song i -> song j
    for i in range(df.shape[0]):
        for j in range(df.shape[0]):
            weightArray[i][j] = songWeight(df.ix[i],df.ix[j])
            if (i == j):
                weightArray[i][j] = 0
    return weightArray


#Gives a weight for song1 -> song2 based off of their distance. Song 1 and 2 are arrays of numbers.
#TODO add different weight functions
def songWeight(song1,song2):
    dist = pdist([song1,song2],'minkowski',1)[0] #taxicab
    return max(1-dist,0)
