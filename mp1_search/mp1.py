import numpy as np
import itertools

class Maze:
    def __init__(self, tiles):
        self.tiles = tiles
    def __init__(self, filename):
        pass
    def __init__(self, string):
        pass
    def __init__(self, **kwargs):
        self.maze_string = kwargs.get("maze_string", "shit")
        self.init_from_string(self.maze_string)
    def init_from_string(string):
        parse_string_intomaze(string)
        

m = Maze(maze_string="hello")

class Tile:
    def __init__(self, **kwargs):
        # neighbors, maze location (x,y), type eg wall, dot, etc
        pass

class Move:
    def __init__(self, direction): # up down left right
        pass

class SearchAlgorithm:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def search(maze, objective):
        pass

class DFS(SearchAlgorithm):
    pass

class BFS(SearchAlgorithm):
    pass

class GBFS(SearchAlgorithm):
    pass

class Astar(SearchAlgorithm):
    pass
