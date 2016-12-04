#Sanjith Venkatesh 20038520
#Logic module for Project 4

class flipTiles:
# Contains the logic for flipping the files
# Helper class for Logic module

    def flipTiles(self,boardInfo,row,col):
        # Tries all directions from placed disc in (row,col) and flips for valid configurations
        self.flipHorizontalRight(boardInfo,row,col)
        self.flipHorizontalLeft(boardInfo,row,col)
        self.flipVerticalUp(boardInfo,row,col)
        self.flipVerticalDown(boardInfo,row,col)
        self.flipDiagnolIncreasingUp(boardInfo,row,col)
        self.flipDiagnolIncreasingDown(boardInfo,row,col)
        self.flipDiagnolDecreasingDown(boardInfo,row,col)
        self.flipDiagnolDecreasingUp(boardInfo,row,col)
        return boardInfo

    def getOtherColor(self,givenColor):
        # precondition: space value is not provided
        otherColor = "W"
        if givenColor == "W":
            otherColor = "B"
        return otherColor

    def flipHorizontalRight(self, boardInfo, row,col):
        #flips in eastern direction
        currentColor = boardInfo[row][col]
        otherColor = self.getOtherColor(currentColor)
        numCols = len(boardInfo[row])
        if col < numCols - 2:
            if boardInfo[row][col+1] == otherColor:
                colIndex = col + 1
                endCol = col - 1;  # initialize to invalid range
                while colIndex < numCols:
                    disc = boardInfo[row][colIndex]
                    if (disc == otherColor):
                        colIndex += 1
                    elif (disc == "."):
                        break
                    elif (disc == currentColor):
                        endCol = colIndex
                        break
                for colIndex in range(col+1,endCol):
                    boardInfo[row][colIndex] = currentColor
        return boardInfo

    def flipHorizontalLeft(self,boardInfo,row,col):
        #flips in western direction
        if col > 1:
            currentColor = boardInfo[row][col]
            otherColor = self.getOtherColor(currentColor)
            if boardInfo[row][col-1] == otherColor:
                colIndex = col-1
                endCol = col+1  # initialize to invalid range
                while colIndex >= 0:
                    disc = boardInfo[row][colIndex]
                    if disc == otherColor:
                        colIndex -= 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endCol = colIndex
                        break
                for colIndex in range(col-1, endCol-1, -1):
                    boardInfo[row][colIndex] = currentColor
        return boardInfo

    def flipVerticalDown(self,boardInfo,row,col):
        #flips in southern direction
        numRows = len(boardInfo)
        if row < numRows-2 :
            currentColor = boardInfo[row][col]
            otherColor = self.getOtherColor(currentColor)
            if boardInfo[row+1][col] == otherColor:
                rowIndex = row+1
                endRow = row-1  # initialize to invalid range
                while rowIndex < numRows:
                    disc = boardInfo[rowIndex][col]
                    if disc == otherColor:
                        rowIndex += 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        break
                for rowIndex in range(row+1,endRow):
                    boardInfo[rowIndex][col] = currentColor
        return boardInfo

    def flipVerticalUp(self,boardInfo,row,col):
        #flips in northern direction
        if row > 1:
            currentColor = boardInfo[row][col]
            otherColor = self.getOtherColor(currentColor)
            if boardInfo[row-1][col] == otherColor:
                rowIndex = row-1
                endRow = row+1  # initialize to invalid range
                while rowIndex >= 0:
                    disc = boardInfo[rowIndex][col]
                    if disc == otherColor:
                        rowIndex -= 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        break
                for rowIndex in range(row-1,endRow,-1):
                    boardInfo[rowIndex][col] = currentColor
        return boardInfo

    def flipDiagnolIncreasingUp(self,boardInfo,row,col):
        #flips in northeastern direction
        numRows = len(boardInfo)
        numCols = len(boardInfo[row])
        currentColor = boardInfo[row][col]
        otherColor = self.getOtherColor(currentColor)
        if row > 1 and col < numCols-2:
            if boardInfo[row-1][col+1] == otherColor:
                rowIndex = row-1
                colIndex = col+1
                endRow = row+1   # initialize to invalid range
                endCol = col-1   # initialize to invalid range
                while rowIndex >= 0 and colIndex < numCols:
                    disc = boardInfo[rowIndex][colIndex]
                    if disc == otherColor:
                        rowIndex -= 1
                        colIndex += 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        endCol = colIndex
                        break

                rowIndex = row - 1
                colIndex = col + 1
                while (rowIndex > endRow and colIndex < endCol):
                    boardInfo[rowIndex][colIndex] = currentColor
                    rowIndex -= 1
                    colIndex += 1
                    
        return boardInfo

    def flipDiagnolIncreasingDown(self,boardInfo,row,col):
        #flips in southwestern direction
        numRows = len(boardInfo)
        currentColor = boardInfo[row][col]
        otherColor = self.getOtherColor(currentColor)
        if row < numRows-2 and col > 1:
            if boardInfo[row+1][col-1] == otherColor:
                rowIndex = row+1
                colIndex = col-1
                endRow = row-1   # initialize to invalid range
                endCol = col+1   # initialize to invalid range
                while rowIndex < numRows and colIndex >= 0 :
                    disc = boardInfo[rowIndex][colIndex]
                    if disc == otherColor:
                        rowIndex += 1
                        colIndex -= 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        endCol = colIndex
                        break

                rowIndex = row + 1
                colIndex = col - 1
                while (rowIndex < endRow and colIndex > endCol):
                    boardInfo[rowIndex][colIndex] = currentColor
                    rowIndex += 1
                    colIndex -= 1
                    
        return boardInfo

    def flipDiagnolDecreasingUp(self,boardInfo,row,col):
        #flips in northwestern direction
        numRows = len(boardInfo)
        currentColor = boardInfo[row][col]
        otherColor = self.getOtherColor(currentColor)
        if row > 1 and col > 1:
            if boardInfo[row-1][col-1] == otherColor:
                rowIndex = row-1
                colIndex = col-1
                endRow = row+1   # initialize to invalid range
                endCol = col+1   # initialize to invalid range
                while rowIndex >= 0 and colIndex >= 0:
                    disc = boardInfo[rowIndex][colIndex]
                    if disc == otherColor:
                        rowIndex -= 1
                        colIndex -= 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        endCol = colIndex
                        break

                rowIndex = row - 1
                colIndex = col - 1
                while (rowIndex > endRow and colIndex > endCol):
                    boardInfo[rowIndex][colIndex] = currentColor
                    rowIndex -= 1
                    colIndex -= 1
                    
        return boardInfo

    def flipDiagnolDecreasingDown(self,boardInfo,row,col):
        #flips in southesastern direction
        numRows = len(boardInfo)
        numCols = len(boardInfo[row])
        currentColor = boardInfo[row][col]
        otherColor = self.getOtherColor(currentColor)
        if row < numRows-2 and col < numCols-2:
            if boardInfo[row+1][col+1] == otherColor:
                rowIndex = row+1
                colIndex = col+1
                endRow = row-1   # initialize to invalid range
                endCol = col-1   # initialize to invalid range
                while rowIndex < numRows and colIndex < numCols:
                    disc = boardInfo[rowIndex][colIndex]
                    if disc == otherColor:
                        rowIndex += 1
                        colIndex += 1
                    elif disc == ".":
                        break
                    elif disc == currentColor:
                        endRow = rowIndex
                        endCol = colIndex
                        break

                rowIndex = row + 1
                colIndex = col + 1
                while (rowIndex < endRow and colIndex < endCol):
                    boardInfo[rowIndex][colIndex] = currentColor
                    rowIndex += 1
                    colIndex += 1
                    
        return boardInfo

