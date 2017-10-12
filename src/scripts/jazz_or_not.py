import pandas as pd
import getData as gd
import sys
import pickle

SONGID = sys.argv[2]
ACCESS_HEADER = gd.getAccessHeader()

def songDataFrame(songid):
	features = ["popularity", "danceability", "energy", "loudness", "speechiness", "acousticness",\
			"instrumentalness", "liveness", "valence", "tempo"]
	data = gd.getSongs([songid])[0]
	pre_frame_d = {}
	for f in features:
		pre_frame_d[f] = data[f]
	df = pd.DataFrame(index=[0], data=pre_frame_d)
	return df

def printResults(df, clf):
	print("="*25)
	classes = clf.classes_
	prediction = classifier.predict(song_df)[0]
	proba = classifier.predict_proba(song_df)[0]
	print(proba)
	if prediction:
		print("This is Jazz")
	else:
		print("This is not Jazz")
	print("="*25, "\n")

if __name__ == '__main__':
	fileObject = open(sys.argv[1],'rb')
	classifier = pickle.load(fileObject)
	song_df = songDataFrame(SONGID)
	printResults(song_df, classifier)