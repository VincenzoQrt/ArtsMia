import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        # modo 1: successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0)

        # modo 2: predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)

        # modo 3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)

        # modo 4: node connected component
        connComp = nx.node_connected_component(self._grafo, v0)

        return len(connComp)

    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()
        allEdges = DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weight=e.peso)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def checkExistence(self, idOggetto):
        return idOggetto in self._idMap
