# progamme TIC TAC TOE
from random import sample
def equal_board (board):
    global end
    #equal_column(board)
    #c=equal_column(board)
    if (board[0]==board[1]) and (board[0]==board[2]):
        if board[0]=="X":
            print("vous avez perdu cette partie")
            end=True
        elif board[0]=="O":
            print("Wouah vous avez battu l'ordinateur")
            end =True
def equal_column (board):
     for i in range(3):
                board[0][i]=great_board[i]
     for i in range(3):
                board[1][i]=great_board[i+3]
     for i in range(3):
                board[2][i]=great_board[i+6] 
            
     for i in range (3):
        global end
        equal_board(board[i])
        if end==True:
                break
        if board[0][i]==board[1][i] and board[0][i]==board[2][i]:
            if board[0][i]=="X":
                print("vous avez perdu")
                end=True
                break
            else: print("Waouh belle victoire")
            end= True
            break
     for i in range(1):
        if ((board[0][0]==board[1][1]) and (board[0][0]==board[2][2])) :
            if board[0][0]=="X":
                print("vous avez perdu cette partie")
                end=True
                break
            elif board[0][0]=="O":
                print("Wouah vous avez battu l'ordinateur")
                end =True
                break
        if ((board[0][2]==board[1][1]) and (board[0][2]==board[2][0])) :
            if board[0][2]=="X":
                print("vous avez perdu cette partie")
                end=True
                break
            elif board[0][2]=="O":
                print("Wouah vous avez battu l'ordinateur")
                end =True
                break
     
    #elif c:
        #end =True

print("bonjour nous vous défions à TIC TAC TOE : \nla règle est simple entrer le numéro identifiant la case \nou vous voulez que votre symbole soit plaçé \nle premier à aligner 3 symboles gagne la partie.","commençons (^-^):")
while True :
    board = [[1,2,3],[4,"X",6],[7,8,9]]
    great_board = [0,0,0,0,0,0,0,0,0]
    end=False
    
    print ("+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[0][0]," |"+" ",board[0][1]," "+"| ",board[0][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[1][0]," |"+" ",board[1][1]," "+"| ",board[1][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[2][0]," |"+" ",board[2][1]," "+"| ",board[2][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n")
    for i in range(4):
        
        try :user_play=int(input("entrer le n° que porte la case où vous souhaitez placez votre symbole"))
        except:
            print("entrée invalide")
            continue
        if user_play not in (1,2,3,4,5,6,7,8,9):
            print("entrée invalide")
            continue
        for i in range(3):
            great_board[i]=board[0][i]
        for i in range(3):
            great_board[i+3]=board[1][i]
        for i in range(3):
            great_board[i+6]=board[2][i]
        user_play-=1                                     
        
        if great_board[user_play] in ("O","X"):
            print("case dejà occupé ")
            continue                
        else: 
            great_board[user_play]="O"
           
        equal_column(board)
        if end==True:
            print ("+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[0][0]," |"+" ",board[0][1]," "+"| ",board[0][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[1][0]," |"+" ",board[1][1]," "+"| ",board[1][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[2][0]," |"+" ",board[2][1]," "+"| ",board[2][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n")
            break
        computer_play_position=sample(range(9),9)
        for i in range(9):
            a=computer_play_position[i]
            if great_board[a] not in ("O","X"):
              
               great_board[a]="X"
               break
        equal_column(board)
        if end==True:
            print ("+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[0][0]," |"+" ",board[0][1]," "+"| ",board[0][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[1][0]," |"+" ",board[1][1]," "+"| ",board[1][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[2][0]," |"+" ",board[2][1]," "+"| ",board[2][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n")
            break
        
        
        print ("+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[0][0]," |"+" ",board[0][1]," "+"| ",board[0][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[1][0]," |"+" ",board[1][1]," "+"| ",board[1][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n"+"|     |     |     |\n"+"| ",board[2][0]," |"+" ",board[2][1]," "+"| ",board[2][2]," |\n"+"|     |     |     |\n"+"+"+"-"*17+"+\n")
        
    
    if end==True:
        break
    else: continue
    
         

    

