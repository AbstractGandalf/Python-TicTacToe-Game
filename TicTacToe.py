gameBoard = {'a1':' ','b1':' ','c1':' ',
             'a2':' ','b2':' ','c2':' ',
             'a3':' ','b3':' ','c3':' ', }

Winner=''



def GamePrinter(board):
    print(gameBoard['a1']+'|'+gameBoard['b1']+'|'+gameBoard['c1'])
    print('-+-+-')
    print(gameBoard['a2']+'|'+gameBoard['b2']+'|'+gameBoard['c2'])
    print('-+-+-')
    print(gameBoard['a3']+'|'+gameBoard['b3']+'|'+gameBoard['c3'])
    

Winner = ''
print(Winner)
def GameChecker(board):
    global Winner
    if(gameBoard['a1'] == 'X' and gameBoard['b1'] == 'X' and gameBoard['c1'] == 'X' ):
        Winner='X'
    elif(gameBoard['a2'] == 'X' and gameBoard['b2'] == 'X' and gameBoard['c2'] == 'X' ):
        Winner='X'
    elif(gameBoard['a3'] == 'X' and gameBoard['b3'] == 'X' and gameBoard['c3'] == 'X' ):
        Winner='X'
    elif(gameBoard['a1'] == 'X' and gameBoard['a2'] == 'X' and gameBoard['a3'] == 'X' ):
        Winner='X'
    elif(gameBoard['b1'] == 'X' and gameBoard['b2'] == 'X' and gameBoard['b3'] == 'X' ):
        Winner='X'
    elif(gameBoard['c1'] == 'X' and gameBoard['c2'] == 'X' and gameBoard['c3'] == 'X' ):
        Winner='X'
    elif(gameBoard['a1'] == 'X' and gameBoard['b2'] == 'X' and gameBoard['c3'] == 'X' ):
        Winner='X'
    elif(gameBoard['c1'] == 'X' and gameBoard['b2'] == 'X' and gameBoard['a3'] == 'X' ):
        Winner='X'
    elif(gameBoard['a1'] == 'O' and gameBoard['b1'] == 'O' and gameBoard['c1'] == 'O' ):
        Winner='O'
    elif(gameBoard['a2'] == 'O' and gameBoard['b2'] == 'O' and gameBoard['c2'] == 'O' ):
        Winner='O'
    elif(gameBoard['a3'] == 'O' and gameBoard['b3'] == 'O' and gameBoard['c3'] == 'O' ):
        Winner='O'
    elif(gameBoard['a1'] == 'O' and gameBoard['a2'] == 'O' and gameBoard['a3'] == 'O' ):
        Winner='O'
    elif(gameBoard['b1'] == 'O' and gameBoard['b2'] == 'O' and gameBoard['b3'] == 'O' ):
        Winner='O'
    elif(gameBoard['c1'] == 'O' and gameBoard['c2'] == 'O' and gameBoard['c3'] == 'O' ):
        Winner='O'
    elif(gameBoard['a1'] == 'O' and gameBoard['b2'] == 'O' and gameBoard['c3'] == 'O' ):
        Winner='O'
    elif(gameBoard['c1'] == 'O' and gameBoard['b2'] == 'O' and gameBoard['a3'] == 'O' ):
        Winner='O'
    else: Winner = '' 




GamePrinter(gameBoard)
print("Welcome to CLI Tic-Tac-Toe !")
print(" ")
print("The co-ordinates are as so")
print("1  | | ")
print("  -+-+-")
print("2  | | ")
print("  -+-+-")
print("3  | | ")
print("  a b c")
print(" Moves are 2 character co-ordinate numbers- for example,a1 or b3 or c2")
print("And the game Begins ! Start with Player X")
turn = 'X' 

for i in range(9):
    print("Turn for "+ turn +" ,which space will you mark ?")
    move=input()
    gameBoard[move]=turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    GamePrinter(gameBoard)
    GameChecker(gameBoard)
    #if(Winner == ''):
        #print("bhooo")
        #continue
    if(Winner == 'X' or Winner == 'O'):        
        break
    
print(" ")
 
if(Winner != ''):    
    print("Game Over !")
    print("The winner is player "+Winner+" !! Congratulations !!")
else: print("The game is a draw !")






