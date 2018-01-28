from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import math
import pandas as pd

#SET CSV FILE HERE
df = pd.read_csv('csv2.csv')
#PROVIDE THE CSV HEADER
X = df.as_matrix(["sentiment","/Science/Mathematics","/Science/Physics","/News/Business News","/Home & Garden/Home Appliances","/Science/Earth Sciences","/Reference","/Arts & Entertainment/Music & Audio/Radio","/Science","/Finance/Investing/Currencies & Foreign Exchange","/People & Society/Subcultures & Niche Interests","/Sports/Team Sports","/Reference/Humanities/History","/Health/Public Health","/Law & Government/Public Safety/Law Enforcement","/Sports/Team Sports/Baseball","/Games/Computer & Video Games","/Arts & Entertainment/Fun & Trivia/Flash-Based Entertainment","/Games/Computer & Video Games/Shooter Games","/Home & Garden/Kitchen & Dining","/Computers & Electronics/Software","/Arts & Entertainment/Music & Audio/World Music","/Games","/Sensitive Subjects","/Arts & Entertainment/TV & Video","/Reference/General Reference/Calculators & Reference Tools","/Business & Industrial/Energy & Utilities","/Computers & Electronics/Consumer Electronics","/Games/Roleplaying Games","/Arts & Entertainment","/Arts & Entertainment/Music & Audio/Dance & Electronic Music","/Arts & Entertainment/Music & Audio/Religious Music","/Arts & Entertainment/TV & Video/TV Shows & Programs","/Sports/Team Sports/Cricket","/Jobs & Education/Education/Teaching & Classroom Resources","/Arts & Entertainment/Music & Audio","/Law & Government/Public Safety","/Science/Engineering & Technology","/Food & Drink","/Arts & Entertainment/Performing Arts","/Home & Garden/Kitchen & Dining/Small Kitchen Appliances","/Arts & Entertainment/TV & Video/Online Video","/Business & Industrial","/Law & Government/Public Safety/Crime & Justice","/Arts & Entertainment/Music & Audio/Urban & Hip-Hop","/Computers & Electronics/Software/Multimedia Software","/Arts & Entertainment/Online Media","/Hobbies & Leisure","/Arts & Entertainment/Music & Audio/Music Equipment & Technology","/Arts & Entertainment/Music & Audio/Soundtracks","/Arts & Entertainment/Music & Audio/Rock Music","/People & Society/Religion & Belief","/Computers & Electronics/Software/Business & Productivity Software","/Books & Literature","/Computers & Electronics/CAD & CAM","/Games/Board Games/Chess & Abstract Strategy Games","/Internet & Telecom","/Health/Health Conditions/Infectious Diseases","/Online Communities","/Arts & Entertainment/Comics & Animation/Comics","/Business & Industrial/Energy & Utilities/Renewable & Alternative Energy","/Arts & Entertainment/Comics & Animation/Cartoons","/Law & Government","/Computers & Electronics/Computer Security","/Jobs & Education/Education/Colleges & Universities","/Computers & Electronics","/Science/Biological Sciences","/Science/Computer Science","/News/Sports News","/Science/Earth Sciences/Geology","/Sports","/Arts & Entertainment/Comics & Animation/Anime & Manga","/Arts & Entertainment/Visual Art & Design","/Computers & Electronics/Consumer Electronics/Game Systems & Consoles","/Arts & Entertainment/Music & Audio/Music Reference","/News/Politics","/Business & Industrial/Aerospace & Defense/Space Technology","/Hobbies & Leisure/Special Occasions/Holidays & Seasonal Events","/Arts & Entertainment/Fun & Trivia","/Arts & Entertainment/Humor","/Arts & Entertainment/Movies","/Online Communities/Social Networks","/Arts & Entertainment/Music & Audio/Pop Music","/Home & Garden","/Jobs & Education/Education","/Games/Computer & Video Games/Casual Games","/Pets & Animals/Wildlife","/Business & Industrial/Agriculture & Forestry","/Computers & Electronics/Computer Hardware","/Games/Computer & Video Games/Simulation Games","/Reference/General Reference","/Science/Astronomy","/News","/Arts & Entertainment/Comics & Animation","/Internet & Telecom/Mobile & Wireless/Mobile & Wireless Accessories"])
N = len(X)

#ISOMAP algorithm w/ M equal to 2D
X_isomap = Isomap(n_components=2)
X_mapped_matrix = X_isomap.fit_transform(X)

#Define k clusters as the sqrt of the total amount of samples
k = int(round(math.sqrt(N)))

#KMeans w/ k clusters
kmeans_object = KMeans(n_clusters=k, random_state=0)
#Obtain the labels that map the data to their cluster
kmeans_labels = kmeans_object.fit(X_mapped_matrix)
cluster_labels = kmeans_labels.labels_
#Transform
kmeans_cluster = kmeans_object.transform(X_mapped_matrix)

#Scale the colors for the clusters proportional to 256 / the number clusters
for i in cluster_labels:
	i = i * (256 / len(cluster_labels))

x = kmeans_cluster[:, 0]
y = kmeans_cluster[:, 1]



#Prediction w/ arbitrary vector
arb_vect = X[0]
#Transform the vector & perform a prediction to get the most similar cluster
transformed_arb_vect = X_isomap.transform(np.expand_dims(arb_vect, axis=0))
prediction_cluster = kmeans_labels.predict(transformed_arb_vect)

#Create a list of indicies
indicies = []
for i in range(0, len(cluster_labels), 1):
	if cluster_labels[i] == prediction_cluster[0]:
		indicies.append(i)

#Create a list of video ids corresponding to all in the cluster that is most similar to the provided vector
video_ids = []
for i in indicies:
	video_ids.append(df["video_id"].iloc[i])
#Print the video Ids
print(video_ids)

#Plot
plt.scatter(x, y, s=50, c=cluster_labels, alpha=0.5)
plt.show()