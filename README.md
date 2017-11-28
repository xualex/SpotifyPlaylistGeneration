# Spotify Playlist

This project seeks to generate coherent (whatever that means) playlists. The final goal of this project is to be able to authorize a user and build a custom playlist on their account given an input of songs. Various methods of song generation are detailed below. 

# How to use

## Setup
Essential packages are detailed in requirements.txt. You will need to make a file called auth\_info.py in the playlist\_generation directory, with CLIENT\_ID, CLIENT\_SECRET, username, redirect\_uri. 

## Files
Currently, spotipy\_auth.py will take a playlist as a system argument (unsure of terminology, usage is python3 spotipy\_auth.py \<playlist id\>. 



# Milestones

## Week 9 (11/27/2017)

**To do**

- Start analyzing effects of modifications on weight function in Markov Generation
- Optimize generation of Markov chains
- Grab playlists/genres of songs from Spotify to use

**Finished**

- Have linear and Markov chain generation
- Can generate playlists online

## Week 1 (10/19/2017)


**To Do**

- Get Spotify API endpoints set up
- Start Linear Generation code
- Brainstorm other potential generation techniques
- Clean up playlist generation in readme 

**Finished**

- Get repo set up
- Get team members up to speed







# Building a playlist

In: a bunch of songs & user data  
Out: a list of song ids (a playlist)

## 1. Random walks on a graph

#### Motivation

Using random walks with respect to some distance function gives a relatively natural method to generate a playlist. Given a list of relatively similar songs will hopefully have consecutive songs meshing well.

#### Methodology

Represent the songs as vertices of a graph and weight the edges on how 'closely' two songs would fit consecutively on a playlist. Then perform a random walk with the weights. This is suitable for long playlists meant to be played continuously 

1. Build a graph where vertices are songs with edges between them if they are 'related'. This can be done with KNN/clustering algorithms. Data on song openings/closings 
2. Define a weight function that defines how related connected vertices are. This can use euclidean/other distance function augmented with user preferences (e.g. recent music)
3. Define a random walk via weights on last song(s) played. Will need tweaking to prevent excessive repetition and include all songs.

#### Graph building

We can define a graph as an *n* x *n* array where the entry in the *i*th row and *j*th column corresponds to the weight to go from the *i*th song to the *j*th song. Essentially an array representation of a weighted digraph.

To reduce computation required, we can consider only the *k* nearest vertices with respect to Euclidean distance between the songs. *k* must be small enough to ensure relevance of all edges considered, yet large enough to avoid repetition. Other schemes to limit the number of edges can also be considered. 

#### Weight functions

A weight function is a function that assigns a value to each of the edges of the graph being considered (as per limitations in previous section). The simplest method to do this is by using a Euclidean metric on the space the songs are in. However, other metrics can also be considered, e.g. taxicab distance (sum of differences in each attribute) and in general they can be relatively arbitrary. Emphasis should be placed on attributes that affect how two songs link together, e.g. tempo and key as well as 

We can also use recent user data to modify weights. For example, we can use the 50 most recently played songs (or some training set) to determine weights. Songs closer to the mean of the set get higher weights. Possibly preserving the 'direction' of songs in a curated playlist is an interesting idea (generalized brownian motion maybe?). Other ideas of weight modification are welcomed.

#### Random walks 

After building weights, the idea of a random walk is relatively obvious. However, possible modifications and some issues such as repeats and repetition of overly similar songs will be addressed here. Avoiding repetition of songs is relatively easy: it suffices to make a list of the *k* most recently played songs and exclude them as candidates. However, we need to be careful, since it is possible to exclude all possible candidates－try to avoid choosing too large a *k*.

Sometimes it may be desireable to keep the songs relatively similar. To do this, we can use weights of previous *k* songs in the playlist; songs with high weights with multiple recent songs are likely highly related. If a more dynamic environment is desired, we can simply do the opposite.

## 2. Linear generation

#### Motivation

Generating songs with a definite progression from a start point to an end point is often desirable. Thus, drawing a line and fitting songs to the line can be a very good approximation to what we want.

#### Methodology

Choose a starting song and ending song and choose the desired duration of the playlist. By drawing a line between the two points in space, it follows that we should pick songs near the line, and in particular, near the place we should be at that time (since we know the combined duration of previous songs). 


An analogue for a polygonal segment of multiple songs is easily found by combining multiple line segments, adn we can generalize further by defining arbitrary paths to follow through space.  This is suitable for events where gradual transformations in the atmosphere are desirable.  


