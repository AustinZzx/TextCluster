from DPSParser import *
from sklearnCluster import *

from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt

dpsc = DPSParser()
myDict = {}
myclassDict = {}
dictify(dpsc, myDict, myclassDict)
myclassInfo = []
myClassList = []
dicttolist(myclassDict, myclassInfo, myClassList)

dist = 1 - get_similarity_matrix(myclassInfo)
linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="right", labels=myClassList);

plt.tick_params(\
    axis= 'x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')

plt.tight_layout() #show plot with tight layout

#uncomment below to save figure
plt.savefig('ward_clusters.png', dpi=200) #save figure as ward_clusters