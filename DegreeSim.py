import networkx as nx

def DegreeMeasure(G):
	RM_Val = nx.adjacency_matrix(G).copy()

	for u in G.nodes():
		for v in G.nodes():
			if G.degree(u) == G.degree(v) == 0:
				RM_Val[G.nodes().index(u),G.nodes().index(v)] = float(1)
			elif G.degree(v) > G.degree(u):
				RM_Val[G.nodes().index(u),G.nodes().index(v)] = float(G.degree(u))/float(G.degree(v))
			else:
				RM_Val[G.nodes().index(u),G.nodes().index(v)] = float(G.degree(v))/float(G.degree(u))
				
	return RM_Val