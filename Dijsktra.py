
from collections import defaultdict, deque

class Graph:
  
  def __init__(self,componentList,transferLineList):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    #self.tracker = tracker

    self.initializeGraph(componentList,transferLineList)

  def initializeGraph(self,componentList,transferLineList):
    # for component in componentList:
    #   self.add_node(str(component.title()))
    #   for neighbor in component.neighbors:
    #     self.add_edge(str(component.title()),str(neighbor.title()))
    for component in componentList:
      self.add_node(str(component.title()))
    for transferLine in transferLineList:
      self.add_edge(str(transferLine.connections[0].title()),str(transferLine.connections[1].title()),transferLine.name)
      print str(transferLine.connections[0].title()) + " connected to " + str(transferLine.connections[1].title())

  def add_node(self, value):
    self.nodes.add(value)

  # def add_edge(self, from_node, to_node, distance=1):
  #   self.edges[from_node].append(to_node)
  #   self.edges[to_node].append(from_node)
  #   self.distances[(from_node, to_node)] = distance
  #   self.distances[(to_node, from_node)] = distance

  # def dijkstra(self, initial):
  #   visited = {initial: 0}
  #   path = {}
  #   nodes = set(self.nodes)

  #   while nodes: 
  #     min_node = None
  #     for node in nodes:
  #       if node in visited:
  #         if min_node is None:
  #           min_node = node
  #         elif visited[node] < visited[min_node]:
  #           min_node = node

  #     if min_node is None:
  #       break

  #     nodes.remove(min_node)
  #     current_weight = visited[min_node]

  #     for edge in self.edges[min_node]:
  #       weight = current_weight + self.distances[(min_node, edge)]
  #       if edge not in visited or weight < visited[edge]:
  #         visited[edge] = weight
  #         path[edge] = min_node
  #   return visited, path
###########################################TESTING FOR FUNCTIONALITY#######################################
  def add_edge(self, from_node, to_node, transfer_line, distance=1):
    self.edges[from_node].append([to_node,transfer_line])
    self.edges[to_node].append([from_node,transfer_line])
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

  def dijkstra(self, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(self.nodes)

    while nodes: 
      min_node = None
      for node in nodes:
        if node in visited:
          if min_node is None:
            min_node = node
          elif visited[node] < visited[min_node]:
            min_node = node

      if min_node is None:
        break

      nodes.remove(min_node)
      current_weight = visited[min_node]

      for edge in self.edges[min_node]:
        weight = current_weight + self.distances[(min_node, edge[0])]
        if edge[0] not in visited or weight < visited[edge[0]]:
          visited[edge[0]] = weight
          path[edge[0]] = min_node
    #print "visited: " + str(visited)
    #print "path: " + str(path)
    return visited, path
########################################################################################################
  def findShortestPath(self, origin, destination):
    visited, paths = self.dijkstra(origin)
    full_path = deque()
    transfer_line_path = deque()
    try:
      _destination = paths[destination]
    except KeyError:
      return "NO VALID PATH", "available"

    ##########
    for pair in self.edges[destination]:
      if (pair[0] == _destination):
        transfer_line_path.appendleft(pair[1])
        break


    ##########
    #print _destination
    while _destination != origin:
        full_path.appendleft(_destination)
        for pair in self.edges[_destination]: 
          if (pair[0] == paths[_destination]):
            print "appended" + pair[1]
            transfer_line_path.appendleft(pair[1])
            break



        _destination = paths[_destination]
        print _destination

    full_path.appendleft(origin)
    full_path.append(destination)

    #print full_path
    #print transfer_line_path
    #return visited[destination], list(full_path)
    return list(full_path),list(transfer_line_path)

