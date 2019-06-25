"""
    The module is for sorting the servers information contained in a CSV
"""
import csv
from collections import defaultdict
import collections
import json

#Class to represent a graph
# https://www.geeksforgeeks.org/topological-sorting/
class Graph:
    """
    The Graph object represents graph

    Args:
        vertices (int): The variable is used for getting the number of vertices in graph

    Attributes:
        graph (default dict list): This is where we store the adjaceny list of graph
        V (int): This is where we store the number of vertices in a graph
    """
    def __init__(self, vertices=0):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices # number of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        """
            Description TBD
        """
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
        """
            Description TBD
        """
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]:
                continue
            else:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    def topologicalSort(self):
        """
            Description TBD
        """
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i]:
                continue
            else:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        #print (stack)
        return stack

    def isCyclicUtil(self, v, visited, recStack):
        """
            Description A recursive function used by isCyclic
        """
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        """
        Description Returns true if graph is cyclic else false
        """
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

#Class to represent a server
class ServersInfo:
    """
    The ServersInfo object contains information about servers got from CSV

    Attributes:
        serversinfo (default dict list): This is where we store the adjaceny list of servers
        V (int): This is where we store the number of vertices in a graph
    """
    def __init__(self):
        """
            Description TBD
        """
        self.serversinfo = defaultdict(list) #dictionary containing adjacency List
        self.V = 0 #No. of servers, will be set during readCSV rows(= number of servers) are read
        self.undirected_graph = Graph() # graph information used for Group(ing) i.e. u - v
        self.directed_graph = Graph() # graph information used for Order(ing) i.e. u -> v

    # To read the CSV file and initialize the member variables
    def readCSV(self, csvFileName):
        """
            Description TBD
        """
        try:
            with open(csvFileName, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                # to get the line count in the csv file
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    line_count += 1

                #print(f'Processed {line_count} lines.')

                # total number of servers in the dictionary list
                self.V = line_count - 1

                # read each line of CSV and add to the server information variable serversinfo
                csv_file.seek(0)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    self.addServer(line_count - 1, row)
                    line_count += 1

            return True

        except FileNotFoundError:
            print(f'CSV file not found - {csvFileName}')
            return False

    # To add the server to default dict list
    def addServer(self, u, v):
        """
            Description TBD
        """
        self.serversinfo[u].append(v)
        # add the key Group and Order to each dict list
        self.serversinfo[u][0].update(Group=0)
        self.serversinfo[u][0].update(Order=0)

    # To print Adjacency Matrix to verify on https://graphonline.ru/en/
    def printadjacencyMatrix(self):
        """
            Description TBD
        """
        print(f'Adjacency Matrix to verify on https://graphonline.ru/en/')
        for row in self.serversinfo.values():
            #print('\n')
            if row[0]["ServerName"] == "ServerName":
                continue
            list_adjacency = []
            for col in self.serversinfo.values():
                if col[0]["ServerName"] == "ServerName":
                    continue
                if col[0]["ServerName"] in self.directed_graph.graph[row[0]["ServerName"]]:
                    list_adjacency.append(1)
                else:
                    list_adjacency.append(0)
            print(f'{list_adjacency}')
        return True

    # To print values ServerName, Group and Order to the console
    def printServer(self):
        """
            Description TBD
        """
        print(f'\nServerName,Group,Order')
        for list_item in self.serversinfo.values():
            if list_item[0]["ServerName"] == "ServerName":
                continue
            print(f'{list_item[0]["ServerName"]},{list_item[0]["Group"]},{list_item[0]["Order"]}')
        return True

    # To write to a JSON file
    def writeToJson(self, jsonFile):
        """
            Description TBD
        """
        group_dict = {}
        for list_item in self.serversinfo.values():
            if list_item[0]["ServerName"] == "ServerName":
                continue
            group_string = "Group" + str(list_item[0]["Group"])
            group_dict.setdefault(group_string, [])
            group_dict[group_string].append(dict(list_item[0]))

        with open(jsonFile, 'w') as fout:
            #json.dump(group_dict, fout)
            json.dump(group_dict, fout, indent=4, separators=(',', ':'))

        return True

    # To set the value of a particular column corresponding to the list_of_servers
    def setServersColumnValue(self, list_of_servers, column, value):
        """
            Description TBD
        """
        # parse each Group corresponding to the server in the list_of_servers
        for list_item in self.serversinfo.values():
            # check if ServerName is in the list_of_servers
            if column == "Group":
                # list_of_servers is a list
                if list_item[0]["ServerName"] in list_of_servers:
                    # set the Group value
                    list_item[0][column] = value
            elif column == "Order":
                # list_of_servers is a string
                if list_item[0]["ServerName"] == list_of_servers:
                    # set the Group value
                    list_item[0][column] = value
                    break
        return 0

    # To validate servers
    def validateServers(self):
        """
            Description TBD
        """
        list_of_servers = []
        list_of_reboot_dependency_servers = []
        for list_item in self.serversinfo.values():
            # continue with the first row containing
            if list_item[0]["ServerName"] == "ServerName":
                continue
            list_of_servers.append(list_item[0]["ServerName"])
            reboot_dependencies = list_item[0]["RebootDependency"]
            # add the reboot dependencies also to the list of servers
            reboot_dependencies = reboot_dependencies.replace(" ", "")
            list_reboot_dependency_servers = reboot_dependencies.split(";")
            for dependent_server in list_reboot_dependency_servers:
                #if len(dependent_server) > 0:
                if dependent_server:
                    list_of_reboot_dependency_servers.append(dependent_server)

        #print (f' list_of_servers - {list_of_servers}  list_of_reboot_dependency_servers - {list_of_reboot_dependency_servers} ')

        # check the total servers
        #if len(list_of_servers) == 0:
        if not list_of_servers:
            print('Error: No servers found in ServerName')
            return False

        # check if there are duplicate in the ServerName
        list_of_servers_without_duplicates = list(dict.fromkeys(list_of_servers))
        if len(list_of_servers) != len(list_of_servers_without_duplicates):
            print('Error: Duplicates in ServerName')
            return False

        # check if all the reboot dependencies are present in the ServerName
        list_of_reboot_dependency_servers_without_duplicates = list(dict.fromkeys(list_of_reboot_dependency_servers))
        # check if list_of_servers_without_duplicates contains all elements in list_of_reboot_dependency_servers_without_duplicates
        result = all(elem in list_of_servers_without_duplicates  for elem in list_of_reboot_dependency_servers_without_duplicates)
        if result:
            #print("list_of_servers contains all elements in list_of_reboot_dependency_servers")
            return True
        else:
            print("Error: list_of_servers does not contains all elements in list_of_reboot_dependency_servers")
            return False

        return True

    # To group the servers using BFS and Order using topological sort
    def groupServerBFSandTopoSort(self):
        """
            Description TBD
        """
        # create the graph data
        for list_item in self.serversinfo.values():
            # continue with the first row assuming it's header
            vertex_u = list_item[0]["ServerName"]
            if vertex_u == "ServerName":
                continue
            for list_item_destination in self.serversinfo.values():
                # continue with the first row assuming it's header
                vertex_v = list_item_destination[0]["ServerName"]
                if vertex_v == "ServerName":
                    continue
                list_reboot_dependency_servers_v = list_item_destination[0]["RebootDependency"].split(";")
                if vertex_u in list_reboot_dependency_servers_v:
                    #print(f'vertex_u - {vertex_u} vertex_v - {vertex_v} RebootDependency {list_reboot_dependency_servers_v}')
                    # add edge to the directed graph
                    self.directed_graph.addEdge(vertex_u, vertex_v)

                    # add both the edges to the undirected graph
                    self.undirected_graph.addEdge(vertex_u, vertex_v)
                    self.undirected_graph.addEdge(vertex_v, vertex_u)

        # send this directed graph to print on screen for validation
        self.printadjacencyMatrix()

        # check for cycle with
        # call the BFS for each graph in the graph data
        #print(f'graph  edges - {self.graph}')
        group_count = 0
        for list_item in self.serversinfo.values():
            vertex = list_item[0]["ServerName"]
            # continue in case of first row assuming it's header or the Group already set
            if vertex_u == "ServerName" or list_item[0]["Group"] > 0:
                continue
            # graph vertices contains the same group servers
            graph_vertices = []
            graph_vertices = self.bfs(self.undirected_graph.graph, vertex)
            if len(graph_vertices) == 1:
                continue
            else:
                group_count = group_count + 1

                print(f'Group {group_count}')
                print(f'Servers {graph_vertices}')
                #print(f'\n{graph_vertices}')

                # set the value of each server in the list of graph members
                self.setServersColumnValue(graph_vertices, "Group", group_count)

                # intialize a temp object for topological sort with the lengh of number of servers in a group
                graph_for_topo_sort = Graph(len(graph_vertices))
                #print(f'\nBC - {self.directed_graph.graph}')
                for vertex in graph_vertices:
                    for neighbour in self.directed_graph.graph[vertex]:
                        #print(f'\ngroup-{group_count}, vertex-{vertex}, neighbour-{neighbour}')
                        # u -> v with u = vertex and v = neighbour and u always come before v
                        graph_for_topo_sort.addEdge(graph_vertices.index(vertex), graph_vertices.index(neighbour))

                # Before calling topo sort check Acyclic graphs i.e 1 -> 2 -> 3 -> 1
                if graph_for_topo_sort.isCyclic():
                    print("Graph is cyclic, Check adjacency matrix on https://graphonline.ru/en/")
                    return False

                # call the topoligical sort function
                list_order_graph = graph_for_topo_sort.topologicalSort()
                print(f'Servers indexed order {list_order_graph}')

                #set Order of servers in the serverInfo
                server_order = 0
                list_order_of_servers = []
                for index_in_order_graph in list_order_graph:
                    list_order_of_servers.append(graph_vertices[index_in_order_graph])
                    server_order = server_order + 1
                    self.setServersColumnValue(graph_vertices[index_in_order_graph], "Order", server_order)
                print(f'Order - {list_order_of_servers}')
        print(f'total groups are {group_count}')
        return True

    # Creates a graph with a root node, basically it returns the member of a group
    def bfs(self, graph, root):
        """
            Description TBD
        """
        #visited, queue = set(), collections.deque([root])
        visited, queue = list(), collections.deque([root])
        #visited.add(root)
        visited.append(root)
        while queue:
            vertex = queue.popleft()
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    #visited.add(neighbour)
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

# Program execution starting point
# create an object that contains servers information
s = ServersInfo()

# read the CSV and put values into the servers information object created above
#if s.readCSV('C:\\Users\\amardeep.singh\\Documents\\Automated_Patching\\ServerDependencyList\\samplePatchMetadata-Complex.csv') != True:
#csvFile = 'sample_inputs\\samplePatchMetadata-Simple.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Complex.csv'
csvFile = 'sample_inputs\\samplePatchMetadata-Complex-MultipleGroups.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Cyclic-1group.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Cyclic-1group_in_Multiple_Groups.csv'

flag = s.readCSV(csvFile)

if not flag:
    print('read CSV fail')
    exit()

# do some initial validations on the data received from CSV
flag = s.validateServers()
if not flag:
    print('validateServers fail')
    exit()

# Group the serves using BFS and Order using topological sort
flag = s.groupServerBFSandTopoSort()
if not flag:
    print('groupServerBFSandTopoSort fail')
    exit()

# writes to JSON file
s.writeToJson(csvFile + '.json')

# print values ServerName, Group and Order to the console
s.printServer()
