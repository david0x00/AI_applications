import numpy as np
import itertools
import os.path


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
    
    def init_from_string(self, string):
        self.parse_string_into_maze(string)
    
    def set_start_tile(self, tile_x, tile_y):
        pass
    
    def set_goal_tile(self, tile_x, tile_y):
        pass
    
    def parse_string_into_maze(self, string):
        pass
    
    def __str__(self):
        for tile in self.tiles:
            print(tile)


m = Maze(maze_string="hello")

class Tile:
    Empty = " "
    Wall = "%"
    Start = "P"
    Food = "."
    
    def __init__(self, **kwargs):
        # neighbors, maze location (x,y), type eg wall, dot, etc,
        # label eg visited unvisited 
        # Also include maze dimensions for useful helper functions
        # maze_width (x dir), maze_height (y dir)
        self.x = kwargs.get("x", -1)
        self.y = kwargs.get("y", -1)
        self.tile_type = kwargs.get("tile_type", Tile.Empty)
    
    def get_neighbors(self):
        pass
    
    def get_empty_neighbors(self):
        pass
    
    def get_wall_neighbors(self):
        pass

    def is_wall(self):
        return self.tile_type == Tile.Wall
    
    def is_empty(self):
        return self.tile_type == Tile.Empty
    
    def is_start(self):
        return self.tile_type == Tile.Start

    def is_food(self):
        return self.tile_type == Tile.Food
    
    def has_up(self):
        pass # has a neighbor in up direction
    
    def has_down(self):
        pass
    
    def has_right(self):
        pass
    
    def has_left(self):
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
