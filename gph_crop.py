import networkx as nx 
import matplotlib.pyplot as plt
from util import *
import cv2
from os import listdir
from os.path import isfile, join

def write_gph(path, nodes, edges):
    '''given nodes and edges list of a graph, it is written as txt'''
    with open(path, 'w') as f:
        for item in nodes:
            f.write("%s" % str(item[0]))
            f.write(" ")
            f.write("%s\n" % str(item[1]))
        f.write("\n")
        for e in edges:
            f.write("%s" % str(e[0]))
            f.write(" ")
            f.write("%s\n" % str(e[1]))

def make_gph(nodes, edges, index):
    '''a graph is visualized from nodes,edges and position'''
    G = nx.Graph()
    counter = 0
    for i in index:
        G.add_node(i,coor=nodes[counter])
        counter += 1

    for i in range(len(edges)):
        G.add_edge(*edges[i])

    pos = dict(zip(index, nodes))
    print(index)
    nx.draw(G, pos)
    plt.show()

def crop_to_gph(gph_path):
    '''crop graph txt according to given super img files'''

    f = [f for f in listdir(gph_path) if isfile(join(gph_path, f))]
    #f = f[0:2]

    for i in f :
        gph = open(gph_path + i, 'r')
        cont = gph.readlines()
        #print(len(cont))
        ls_node, ls_edge = gphtols_view(cont)
        #ls_node, ls_edge = gphtols(cont)
        name = i.split('.')[0]
        print(name)
        #print(ls_edge)
        gph.close()
        #nodes, edges, index = gph_crop(ls_node, ls_edge, name)
        
        #nodes, edges, index = crop_p(ls_node, ls_edge, name)
        crop_gph_256(ls_node, ls_edge, name)
        #make_gph(nodes, edges, index)
        #write_gph('./data/try/'+ name +'.txt', nodes, edges)
crop_to_gph('./data/supergph/')

def view_gph(path):
    
    f = [f for f in listdir(path) if isfile(join(path, f))]
    f = f[0:2]

    for i in f :
        print(i)
        gph = open(path + i, 'r')
        cont = gph.readlines()
        ls_node, ls_edge = gphtols_view(cont)
        #ls_node, ls_edge = gphtols(cont)
        make_gph(ls_node, ls_edge, range(len(ls_node))) 


#fol_path = '../road_trc/dataset/data/graphs/'
#crop_to_gph(fol_path)
#fol_path = './data/supergph/'
#f = [f for f in listdir(fol_path) if isfile(join(fol_path, f))]
#f = f[0:2]

#path = '../road_trc/dataset/data/graphs/'
#view_gph(fol_path)
