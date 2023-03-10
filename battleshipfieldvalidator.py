#Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

#Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

#Before the game begins, players set up the board and place the ships accordingly to the following rules:
#There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
#Each ship must be a straight line, except for submarines, which are just single cell.

#The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

def validate_battlefield(field):
    battleships=0 #size 4; 1 ship
    cruisers=0 #size 3; 2 ships
    destroyers=0 #size 2, 3 ships
    submarines=0 #size 1, 4 ships
    ships=[submarines, destroyers, cruisers, battleships]
    for row in range(len(field)):
        for column in range(len(field[row])):
            horizShipCounter=0
            vertShipCounter=0
            if field[row][column] == 1:
                x=row
                y=column
                
                #initail diagonal check
                if row<9 and column<9:
                    if field[row+1][column+1] == 1:
                        return False
                if row<9 and column>0:
                    if field[row+1][column-1] == 1:
                        return False
                        
                #check horiz
                for c in range(y,10):
                    if field[row][c]==1:
                        horizShipCounter+=1 #increase ship horizontal length
                        if row<9 and c<9: #do diagonal checks for each additional horizontal 1
                            if field[row+1][c+1] == 1:
                                return False
                        if row<9 and c>0:
                            if field[row+1][c-1] == 1:
                                return False
                        field[row][c]=0 #erase 1s to prevent double counting
                    else:
                        break
                field[x][y]=1 #reset initial value to 1 so it can be checked verticals
                
                #check vert
                for r in range(x,10):
                    if field[r][column]==1:
                        vertShipCounter+=1 #increase ship vertical length
                        if r<9 and column<9: #do dignal check for each additional vertial 1
                            if field[r+1][column+1] == 1:
                                return False
                        if r<9 and column>0:
                            if field[r+1][column-1] == 1:
                                return False
                        field[r][column]=0 #erase 1s to prevent double counting
                    else:
                        break
                
                #checking for valid ship lengths and configurations
                if horizShipCounter > 4  or vertShipCounter > 4: #check if ship is longer than 4
                    return False
                if horizShipCounter > 1 and vertShipCounter > 1: #make sure ships are not beside each other
                    return False
                    
                #counting ship types
                if horizShipCounter == 1 and vertShipCounter == 1:
                    submarines += 1
                if horizShipCounter > vertShipCounter: #ship is horizontial
                    ships[horizShipCounter-1]+=1 
                else: #ship is vertical
                    ships[vertShipCounter-1]+=1
                  
    for x in range(len(ships)): #check to make sure there are the correct number of ships of the different types
        if ships[x] != 4-x: #[4,3,2,1] for [subs, destroy, cruisers, battle]
            return False
                    
    return True
