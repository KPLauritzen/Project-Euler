from pylab import *
import networkx as nx

f = open("matrix.txt","r")

mat = []
for line in f:
    mat.append(line.split(","))
# use numpy array
mat = array(mat) 
# change from strings to ints
mat = mat.astype(int) 
origMat = mat.copy()

# mat = [
# [131,	673,	234,	103,	18],
# [201,	96,	342,	965,	150],
# [630,	803,	746,	422,	111],
# [537,	699,	497,	121,	956],
# [805,	732,	524,	37,	331]
# ]
# # use numpy array
# mat = array(mat) 
# # change from strings to ints
# mat = mat.astype(int) 


size = 80
# Testing graphs with networkx
G = nx.DiGraph()
def main():
    for i in range(size):
        for j in range(size):
            G.add_edge((i,j), (i+1,j), weight=mat[i,j])
            G.add_edge((i,j), (i,j+1), weight=mat[i,j])


    for i in range(size):
        G.remove_node((i,size))
        G.remove_node((size,i))
    
    print nx.shortest_path_length(G, (0,0), (size-1,size-1), weight='weight')

if __name__ == "__main__":
    main()
