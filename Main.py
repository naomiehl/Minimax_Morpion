#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:15:17 2021

@author: haliouanaomie
"""




#Cette fonction est utilisée pour dessiner l'état actuel du tableau à chaque fois que le tour de l'utilisateur arrive. 
def ConstBoard(board):
    print("Current State Of Board : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(board[i]==0):
            print("-",end=" ");
        if (board[i]==1):
            print("O ",end=" ");
        if(board[i]==-1):    
            print("X ",end=" ");
    print("\n\n");

#Cette fonction prend le mouvement de l'utilisateur en entrée et effectue les changements requis sur le plateau.
def UserTurn(board):
    pos=input("Enter X's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0) ;
    board[pos-1]=-1;

    
#MinMax fonction
def minimax(board,player):
    x=analyzeboard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minimax(board,(player*-1));
            if(score>value):
                value=score;
                pos=i;
            board[i]=0;

    if(pos==-1):
        return 0;
    return value;
    
#Cette fonction effectue le déplacement de l'ordinateur en utilisant l'algorithme minmax.

def ComputerTurn(board):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
 
    board[pos]=1;


#Cette fonction est utilisée pour analyser le jeu.
def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]];
    return 0;

#Fonction Main.
def main():
    
    board=[0,0,0,0,0,0,0,0,0];
    player= input("Enter 1 to play 1(st) or 2 to play 2(nd) :");
    player = int(player);
    for i in range (0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i+player)%2==0):
                ComputerTurn(board);
            else:
                ConstBoard(board);
                UserTurn(board);

    x=analyzeboard(board);
    if(x==0):
         ConstBoard(board);
         print("Draw!!!")
    if(x==-1):
         ConstBoard(board);
         print("X Wins!!! 0 Loose !!!")
    if(x==1):
         ConstBoard(board);
         print("X Loose!!! O Wins !!!!")
       

main()