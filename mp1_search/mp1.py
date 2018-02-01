import numpy as np
import itertools
import os.path


# Singleton design pattern to let us do fancy shit, like access other tiles from
# the main maze instance by just instantiating a new maze
# idea from here: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
class Maze:
    class __Maze:
        '''
        TODO: check for string input, filename input
        raise error if none of these given
        '''
        def __init__(self, *args, **kwargs):
            pass

        def init_from_file(self, filename):
            pass

        def init_from_string(self, string):
            self.parse_string_into_maze(string)
        
        def set_start_tile(self, tile_x, tile_y):
            # TODO: iterate and just find it?
            pass
        
        def set_goal_tile(self, tile_x, tile_y):
            pass
        
        def parse_string_into_maze(self, string):
            '''
            TODO: set maze width and height
            TODO: create tile objects and put them into numpy array
            '''
            pass
        
        def __str__(self):
            for tile in self.tiles:
                print(tile)

    instance = None
    def __init__(self, *args, **kwargs):
        if not Maze.instance:
            Maze.instance = Maze.__Maze(args, kwargs)
        else:
            pass # do nothing, we've already initialized it
    def __getattr__(self, name):
        '''
        Pass all other function calls onto the internal instance
        '''
        return getattr(self.instance, name)


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
        self.x = kwargs.get("x", None)
        self.y = kwargs.get("y", None)
        self.tile_type = kwargs.get("tile_type", Tile.Empty)
        self.maze_width = kwargs.get("maze_width", None)
        self.maze_height = kwargs.get("maze_height", None)
        self.maze = Maze() # TODO: actually have this constructor lol
    
    def maze_tuple(self):
        return tuple(self.x, self.y)

    def get_neighbors(self):
        '''
        Create an iterator to iterate over all neighbors
        '''
        if self.has_up():
            yield self.get_up()
        if self.has_down():
            yield self.get_down()
        if self.has_left():
            yield self.get_left()
        if self.has_right():
            yield self.get_right()

    def get_empty_neighbors(self):
        pass
    
    def get_wall_neighbors(self):
        pass

    def get_up(self):
        pass

    def is_wall(self):
        return self.tile_type == Tile.Wall
    
    def is_empty(self):
        return self.tile_type == Tile.Empty
    
    def is_start(self):
        return self.tile_type == Tile.Start

    def is_food(self):
        return self.tile_type == Tile.Food
    
    def exists(self, *args):
        try:
            test = self.maze[args]
        except IndexError:
            return False
        return True

    def has_up(self): # has a neighbor in up direction
        return self.exists(self.x, self.y - 1)
    
    def has_down(self):
        return self.exists(self.x, self.y + 1)
    
    def has_right(self):
        return self.exists(self.x + 1, self.y)
    
    def has_left(self):
        return self.exists(self.x - 1, self.y)

class Move:
    #TODO: do we need dis
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
