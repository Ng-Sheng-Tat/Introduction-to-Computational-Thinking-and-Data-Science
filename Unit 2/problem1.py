class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        #raise NotImplementedError
        self.width = width
        self.height = height
        self.cleaned_tiles = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        #raise NotImplementedError
        point = (int(pos.getX()), int(pos.getY()))
        if point not in self.cleaned_tiles:
            self.cleaned_tiles.append(point)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #raise NotImplementedError
        self.m = m
        self.n = n
        tile = (self.m, self.n)
        if tile in self.cleaned_tiles:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        #raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        #raise NotImplementedError
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        #raise NotImplementedError
        randx = random.uniform(0, self.width)
        randy = random.uniform(0, self.height)
        return Position(randx, randy)
        

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #raise NotImplementedError
        if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
            return True
        else:
            return False