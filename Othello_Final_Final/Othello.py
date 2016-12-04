#Sanjith Venkatesh 20038520
#Othello module for Project 4

from Directions import checkDirections
from flipDirections import flipTiles

class InvalidMoveError(Exception): 
    """raises it if the player enters an invalid move"""
    pass

class Othello:

# Contains the Othello game logic.  Invokees flipDirections, Directions modules as helpers.
# Receives input from any user interface that can create this board and invoke the methods.

    def __init__(self, numRows: int, numCols: int, firstPlayer: str): #declares the board and possible moves lists
        self.board = []
        self.possibleCells = []
        self.rowCount = numRows
        self.colCount = numCols
        self.nextPlayer = firstPlayer

    def getBoard(self):
        #returns board a two-dimensional list
        return self.board

    def getNextPlayer(self):
        # returns the next player whose turn is to play
        return self.nextPlayer

    def getPossibleLocations(self):
        # returns list of possibe zero-indexed cells
        # used for debugging only
        return self.possibleCells

    def setBoard(self, disc: str):
        #sets up the initial board using the rows and columns
        #declared in the inputs     
        for row in range(self.rowCount):
            boardRow = []
            for col in range(self.colCount):
                boardRow.append(".")
            self.board.append(boardRow)	
            
        firstRow = int(self.rowCount/2)-1 
        firstCol = int(self.colCount/2)-1
        self.board[firstRow][firstCol] = disc
        self.board[firstRow+1][firstCol+1] = disc
        if disc == "B":
            self.board[firstRow][firstCol+1] = "W"
            self.board[firstRow+1][firstCol] = "W"
        else:
            self.board[firstRow][firstCol+1] = "B"
            self.board[firstRow+1][firstCol] = "B"

    def continuePlaying(self):
        # Checks if the game has come to an end or can continue playing
        if (self.determineProperLocations() != None):
            self.nextPlayer = self.determineTurn() #determines whose move it is
            if (self.nextPlayer != None): 
                return True
        return False
           
    def determineTurn(self):
        #determines whose turn it is by looking at the board and the possible Move list
        numberOfTiles = self.determineNumberTiles()
        if self.possibleCells[0] == None and self.possibleCells[1] == None and numberOfTiles != (2,2):
            return None

        if self.nextPlayer == "B" and self.possibleCells[1] != None and numberOfTiles != (2,2):
            return "W"
        elif self.nextPlayer == "W" and self.possibleCells[0] != None and numberOfTiles != (2,2):
            return "B"
        else:
            return self.nextPlayer
        
    def determineProperLocations(self):
        #determines where tiles of each color can be placed
        results = []
        results.append(self._getPositions("B"))
        results.append(self._getPositions("W"))
        noneCount = 0
        for each in results:
            if each == None:
                noneCount += 1

        self.possibleCells = results
        
        if noneCount == 2:
            return None
        else:
            return results

    def determineNumberTiles(self):
        #determines how many tiles of each player there are on the board
        white = 0
        black = 0
        for row in self.board:
            for col in row:
                if col == "W":
                    white += 1
                elif col == "B":
                    black += 1
        return (black,white)

    def getTileCounts(self):
        #returns a dictionary for the number of tiles for each color,
        #makes it easier to call the number of tiles
        colorTuple = self.determineNumberTiles()
        colorTable = {"black" : colorTuple[0], "white" : colorTuple[1]}
        return colorTable

    def updateBoard(self,playerInput,move):
        #updates the board after the player input has been specified
        checkD = flipTiles()
        row = playerInput[0] - 1
        col = playerInput[1] - 1
        self.board[row][col] = move
        self.board = checkD.flipTiles(self.board,row,col)
        return self.board

    def _validateInput(self,tupleInput,move):
        row = tupleInput[0] - 1
        col = tupleInput[1] - 1
        if (row < 0 or col < 0 or row >= self.rowCount or col >= self.colCount):
            raise InvalidMoveError

        selectedPos = (row,col)
        whereInPossibleMoves = 0
        if move == "W":
            whereInPossibleMoves = 1
        for eachBlock in self.possibleCells[whereInPossibleMoves]:
            for eachTuple in eachBlock:
                if eachTuple == selectedPos:
                    return True
#        return False
        raise InvalidMoveError

    def _getPositions(self, colorOfTile: str):
        #gets the possible location for specified color of tile
        results = []
        rows = 0
        cols = 0
        while rows < self.rowCount:
            cols = 0
            while cols < self.colCount:
                if self.board[rows][cols] == colorOfTile:
                    a = self._checkHowFarInEachDirection(colorOfTile,rows,cols)
                    if len(a) != 0:
                        results.append(a)
                cols += 1
            rows += 1
        if len(results) != 0:
            return results
        else:
            return None

    def _checkHowFarInEachDirection(self, colorOfTile,rows,cols):
        #returns a list in each direction of the closest spot that is not occupied by a piece 
        results = []
        for direction in range(8):
            a = self._checkDirection(direction+1, colorOfTile, rows, cols)
            if a != None:
                results.append(a)
        return results
                

    def _checkDirection(self,direction, colorOfTile, rows, cols):
        #checks in each direction and returns a possible location or None
        otherColor = ""
        if colorOfTile == "W":
            otherColor = "B"
        else:
            otherColor = "W"
        cd = checkDirections()
        if direction == 1:#checks in northern direction
            return cd.checkVerticalUp(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
        if direction == 2:#checks in northeasterndirection
            return cd.checkDiagnolIncreasingUp(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
        if direction == 3:#checks in eastern direction
            return cd.checkHorizontalRight(self.board,colorOfTile,rows,cols,otherColor)
        if direction == 4:#checks in southeastern direction
            return cd.checkDiagnolDecreasingDown(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
        if direction == 5: #checks in southern direction
            return cd.checkVerticalDown(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
        if direction == 6: #checks in southwestern direction
            return cd.checkDiagnolIncreasingDown(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
        if direction == 7: #checks in western direction
            return cd.checkHorizontalLeft(self.board,colorOfTile,rows,cols,otherColor)
        if direction == 8: #checks in northwestern direction
            return cd.checkDiagnolDecreasingUp(self.board,colorOfTile,rows,cols,otherColor,self.colCount)
            
    def _trimResults(self,results):
        #trims out empty lists and None and returns only a list of position tuples
        trimedResults = []
        for eachList in results:
            if eachList != None and len(results) != 0:
                trimedResults.append(eachList)
        return trimedResults
        
            
                    
            
            
