#Sanjith Venkatesh 20038520
#Logic module for Project 4

class checkDirections:
# Obtains possible valid positions for the supplied row, column
# Helper class for Logic module

    def checkHorizontalRight(self,boardInfo, currentColor, row, column, otherColor):
        #returns blank position to the right if there is an otherColor between the currentColor and blank position
        numCols = len(boardInfo[row])
        if column < numCols - 2:  # need at least 2 additional cells to the right for valid position
            if boardInfo[row][column] == currentColor and boardInfo[row][column+1] == otherColor:
                for c in range(column+1,numCols):
                    if boardInfo[row][c]== currentColor:
                        return None
                    elif boardInfo[row][c] == ".":
                        return(row,c)
                return None

    def checkHorizontalLeft(self,boardInfo,currentColor,row,column,otherColor):
         #returns blank position to the left if there is an otherColor between the currentColor and blank position
        if column > 1:
            if boardInfo[row][column] == currentColor and boardInfo[row][column-1] == otherColor:
                for c in range(column-1,-1,-1):
                    if boardInfo[row][c] == currentColor:
                        return None
                    elif boardInfo[row][c] == ".":
                        return (row,c)
                return None
            return None
        return None

    def checkVerticalDown(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the bottom if there is an otherColor between the currentColor and blank position
        numRows = len(boardInfo)
        if row < numRows - 2:
            if boardInfo[row][column] == currentColor and boardInfo[row+1][column]==otherColor:
                for r in range(row+1,numRows):
                    if boardInfo[r][column] == currentColor:
                        return None
                    elif boardInfo[r][column] == ".":
                        return (r,column)
                return None

    def checkVerticalUp(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the top if there is an otherColor between the currentColor and blank position
        if row > 1:
            if boardInfo[row][column] == currentColor and boardInfo[row-1][column]==otherColor:
                for r in range(row-1,-1,-1):
                    if boardInfo[r][column] == currentColor:
                        return None
                    elif boardInfo[r][column] == ".":
                        return (r,column)
                return None
            return None
        return None

    def checkDiagnolIncreasingUp(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the top right if there is an otherColor between the currentColor and blank position
        numCols = len(boardInfo[row])
        if row > 1 and column < numCols - 2:
            if boardInfo[row][column] == currentColor and boardInfo[row-1][column+1] == otherColor:
                r = row-1
                c = column + 1
                while r >= 0 and c < numCols:
                    if boardInfo[r][c] == currentColor:
                        return None
                    elif boardInfo[r][c] == otherColor:
                        r -=1
                        c += 1
                    elif boardInfo[r][c] == ".":
                        return (r,c)
                return None
            return None
        return None

    def checkDiagnolIncreasingDown(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the bottom left if there is an otherColor between the currentColor and blank position
        numRows = len(boardInfo)
        if row < numRows - 2 and column > 1:
            if boardInfo[row][column] == currentColor and boardInfo[row+1][column-1] == otherColor:
                r = row+1
                c= column-1
                while r < numRows and c >= 0:
                    if boardInfo[r][c] == currentColor:
                        return None
                    elif boardInfo[r][c] == otherColor:
                        r += 1
                        c -= 1
                    elif boardInfo[r][c] == ".":
                        return (r,c)
                return None
            return None
        return None

    def checkDiagnolDecreasingDown(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the bottom right if there is an otherColor between the currentColor and blank position
        numRows = len(boardInfo)
        numCols = len(boardInfo[row])
        if row < numRows - 2 and column < numCols - 2:
            if boardInfo[row][column] == currentColor and boardInfo[row+1][column+1] == otherColor:
                r = row+1
                c= column+1
                while r < numRows and c < numCols:
                    if boardInfo[r][c] == currentColor:
                        return None
                    elif boardInfo[r][c] == otherColor:
                        r += 1
                        c += 1
                    elif boardInfo[r][c] == ".":
                        return (r,c)
                return None
            return None
        return None

    def checkDiagnolDecreasingUp(self,boardInfo,currentColor,row,column,otherColor,lengthOfcolumn):
         #returns blank position to the top left if there is an otherColor between the currentColor and blank position
        if row > 1 and column > 1:
            if boardInfo[row][column] == currentColor and boardInfo[row-1][column-1] == otherColor:
                r = row-1
                c= column-1
                while r >= 0 and c >= 0:
                    if boardInfo[r][c] == currentColor:
                        return None
                    elif boardInfo[r][c] == otherColor:
                        r -= 1
                        c -= 1
                    elif boardInfo[r][c] == ".":
                        return (r,c)
                return None
            return None
        return None

