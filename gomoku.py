from game2dboard import Board

global variant
print("Сражение между какими игроками сейчас будет (1-3)?")
a=int(input())
while (a<1) or (a>3):
    print("Введите корректный ввод первого игрока: ")
    a=int(input())
b=int(input())
while (a==b) or (a<1) or (a>3):
    print("Введите корректный номер второго игрока: ")
    b=int(input())
print("Добро пожаловать игрок", a,"и игрок", b)
print("Выберите кем будет играть первый игрок (x или 0): ")
variant=input()
if (variant=="x"):
    previous_row=previous_col=hod=0
    match_count=1
    menuMSG="grsu --- ESC: Закрыть игру; F1: Начать сначала."

    def botZero():
        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[0][6]==game[0][7]==game[0][8]==game[0][9]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][0]==game[1][1]==game[1][2]==game[1][3]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[1][6]==game[1][7]==game[1][8]==game[1][9]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][0]==game[2][1]==game[2][2]==game[2][3]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) and (game[2][9]==None):
            game[2][9]=0
        elif (game[2][6]==game[2][7]==game[2][8]==game[2][9]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][0]==game[3][1]==game[3][2]==game[3][3]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[3][6]==game[3][7]==game[3][8]==game[3][9]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][0]==game[4][1]==game[4][2]==game[4][3]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[4][6]==game[4][7]==game[4][8]==game[4][9]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][0]==game[5][1]==game[5][2]==game[5][3]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[5][6]==game[5][7]==game[5][8]==game[5][9]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][0]==game[6][1]==game[6][2]==game[6][3]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[6][6]==game[6][7]==game[6][8]==game[6][9]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[7][0]==game[7][1]==game[7][2]==game[7][3]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[7][6]==game[7][7]==game[7][8]==game[7][9]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[8][0]==game[8][1]==game[8][2]==game[8][3]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[8][6]==game[8][7]==game[8][8]==game[8][9]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[9][0]==game[9][1]==game[9][2]==game[9][3]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[9][6]==game[9][7]==game[9][8]==game[9][9]==0) and (game[9][5]==None):
            game[9][5]=0


        elif (game[0][0]==game[1][0]==game[2][0]==game[3][0]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]==game[9][0]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[0][1]==game[1][1]==game[2][1]==game[3][1]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]==game[9][1]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[0][2]==game[1][2]==game[2][2]==game[3][2]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]==game[9][2]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[0][3]==game[1][3]==game[2][3]==game[3][3]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]==game[9][3]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[0][4]==game[1][4]==game[2][4]==game[3][4]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]==game[9][4]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[0][5]==game[1][5]==game[2][5]==game[3][5]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]==game[9][5]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[0][6]==game[1][6]==game[2][6]==game[3][6]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]==game[9][6]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[0][7]==game[1][7]==game[2][7]==game[3][7]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]==game[9][7]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[0][8]==game[1][8]==game[2][8]==game[3][8]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]==game[9][8]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[0][9]==game[1][9]==game[2][9]==game[3][9]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]==game[9][9]==0) and (game[5][9]==None):
            game[5][9]=0


        elif (game[5][0]==game[6][1]==game[7][2]==game[8][3]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[6][1]==game[7][2]==game[8][3]==game[9][4]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[4][0]==game[5][1]==game[6][2]==game[7][3]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][2]==game[7][3]==game[8][4]==game[9][5]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][0]==game[4][1]==game[5][2]==game[6][3]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[6][3]==game[7][4]==game[8][5]==game[9][6]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][0]==game[3][1]==game[4][2]==game[5][3]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[6][4]==game[7][5]==game[8][6]==game[9][7]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[1][0]==game[2][1]==game[3][2]==game[4][3]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[6][5]==game[7][6]==game[8][7]==game[9][8]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[0][0]==game[1][1]==game[2][2]==game[3][3]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[6][6]==game[7][7]==game[8][8]==game[9][9]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[0][1]==game[1][2]==game[2][3]==game[3][4]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[5][6]==game[6][7]==game[7][8]==game[8][9]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[0][2]==game[1][3]==game[2][4]==game[3][5]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[4][6]==game[5][7]==game[6][8]==game[7][9]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[0][3]==game[1][4]==game[2][5]==game[3][6]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[3][6]==game[4][7]==game[5][8]==game[6][9]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[0][4]==game[1][5]==game[2][6]==game[3][7]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[2][6]==game[3][7]==game[4][8]==game[5][9]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[0][5]==game[1][6]==game[2][7]==game[3][8]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[1][6]==game[2][7]==game[3][8]==game[4][9]==0) and (game[0][5]==None):
            game[0][5]=0


        elif (game[0][4]==game[1][3]==game[2][2]==game[3][1]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[1][3]==game[2][2]==game[3][1]==game[4][0]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[1][4]==game[2][3]==game[3][2]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[2][3]==game[3][2]==game[4][1]==game[5][0]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[0][6]==game[1][5]==game[2][4]==game[3][3]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[3][3]==game[4][2]==game[5][1]==game[6][0]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[0][7]==game[1][6]==game[2][5]==game[3][4]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[4][3]==game[5][2]==game[6][1]==game[7][0]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[0][8]==game[1][7]==game[2][6]==game[3][5]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[5][3]==game[6][2]==game[7][1]==game[8][0]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[0][9]==game[1][8]==game[2][7]==game[3][6]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[6][3]==game[7][2]==game[8][1]==game[9][0]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[1][9]==game[2][8]==game[3][7]==game[4][6]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[6][4]==game[7][3]==game[8][2]==game[9][1]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][9]==game[3][8]==game[4][7]==game[5][6]==0) and (game[6][5]==None):
            game[5][5]=0
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]==0) and (game[2][9]==None):
            game[1][9]=0
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]==0) and (game[7][4]==None):
            game[6][4]=0
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[6][5]==game[7][4]==game[8][3]==game[9][2]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][9]==game[4][8]==game[5][7]==game[6][6]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]==0) and (game[8][4]==None):
            game[7][4]=0
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[6][6]==game[7][5]==game[8][4]==game[9][3]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[4][9]==game[5][8]==game[6][7]==game[7][6]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]==0) and (game[9][4]==None):
            game[8][4]=0
        elif (game[6][7]==game[7][6]==game[8][5]==game[9][4]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][9]==game[6][8]==game[7][7]==game[8][6]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][8]==game[7][7]==game[8][6]==game[9][5]==0) and (game[5][9]==None):
            game[5][9]=0



        elif (game[0][0]==game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[0][6]==game[0][7]==game[0][8]==game[0][9]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][0]==game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[1][6]==game[1][7]==game[1][8]==game[1][9]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][0]==game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[2][6]==game[2][7]==game[2][8]==game[2][9]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][0]==game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[3][6]==game[3][7]==game[3][8]==game[3][9]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][0]==game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[4][6]==game[4][7]==game[4][8]==game[4][9]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][0]==game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[5][6]==game[5][7]==game[5][8]==game[5][9]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][0]==game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[6][6]==game[6][7]==game[6][8]==game[6][9]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[7][0]==game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[7][6]==game[7][7]==game[7][8]==game[7][9]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[8][0]==game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[8][6]==game[8][7]==game[8][8]==game[8][9]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[9][0]==game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[9][6]==game[9][7]==game[9][8]==game[9][9]=="x") and (game[9][5]==None):
            game[9][5]=0


        elif (game[0][0]==game[1][0]==game[2][0]==game[3][0]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]==game[9][0]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[0][1]==game[1][1]==game[2][1]==game[3][1]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]==game[9][1]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[0][2]==game[1][2]==game[2][2]==game[3][2]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]==game[9][2]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[0][3]==game[1][3]==game[2][3]==game[3][3]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]==game[9][3]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[0][4]==game[1][4]==game[2][4]==game[3][4]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]==game[9][4]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[0][5]==game[1][5]==game[2][5]==game[3][5]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]==game[9][5]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[0][6]==game[1][6]==game[2][6]==game[3][6]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]==game[9][6]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[0][7]==game[1][7]==game[2][7]==game[3][7]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]==game[9][7]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[0][8]==game[1][8]==game[2][8]==game[3][8]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]==game[9][8]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[0][9]==game[1][9]==game[2][9]==game[3][9]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]==game[9][9]=="x") and (game[5][9]==None):
            game[5][9]=0


        elif (game[5][0]==game[6][1]==game[7][2]==game[8][3]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[6][1]==game[7][2]==game[8][3]==game[9][4]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[4][0]==game[5][1]==game[6][2]==game[7][3]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][2]==game[7][3]==game[8][4]==game[9][5]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][0]==game[4][1]==game[5][2]==game[6][3]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[6][3]==game[7][4]==game[8][5]==game[9][6]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][0]==game[3][1]==game[4][2]==game[5][3]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[6][4]==game[7][5]==game[8][6]==game[9][7]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[1][0]==game[2][1]==game[3][2]==game[4][3]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[6][5]==game[7][6]==game[8][7]==game[9][8]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[0][0]==game[1][1]==game[2][2]==game[3][3]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[6][6]==game[7][7]==game[8][8]==game[9][9]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[0][1]==game[1][2]==game[2][3]==game[3][4]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[5][6]==game[6][7]==game[7][8]==game[8][9]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[0][2]==game[1][3]==game[2][4]==game[3][5]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[4][6]==game[5][7]==game[6][8]==game[7][9]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[0][3]==game[1][4]==game[2][5]==game[3][6]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[3][6]==game[4][7]==game[5][8]==game[6][9]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[0][4]==game[1][5]==game[2][6]==game[3][7]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[2][6]==game[3][7]==game[4][8]==game[5][9]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[0][5]==game[1][6]==game[2][7]==game[3][8]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[1][6]==game[2][7]==game[3][8]==game[4][9]=="x") and (game[0][5]==None):
            game[0][5]=0


        elif (game[0][4]==game[1][3]==game[2][2]==game[3][1]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[1][3]==game[2][2]==game[3][1]==game[4][0]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[1][4]==game[2][3]==game[3][2]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[2][3]==game[3][2]==game[4][1]==game[5][0]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[0][6]==game[1][5]==game[2][4]==game[3][3]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[3][3]==game[4][2]==game[5][1]==game[6][0]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[0][7]==game[1][6]==game[2][5]==game[3][4]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[4][3]==game[5][2]==game[6][1]==game[7][0]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[0][8]==game[1][7]==game[2][6]==game[3][5]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[5][3]==game[6][2]==game[7][1]==game[8][0]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[0][9]==game[1][8]==game[2][7]==game[3][6]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[6][3]==game[7][2]==game[8][1]==game[9][0]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[1][9]==game[2][8]==game[3][7]==game[4][6]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[6][4]==game[7][3]==game[8][2]==game[9][1]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[2][9]==game[3][8]==game[4][7]==game[5][6]=="x") and (game[6][5]==None):
            game[5][5]=0
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]=="x") and (game[2][9]==None):
            game[1][9]=0
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]=="x") and (game[7][4]==None):
            game[6][4]=0
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[6][5]==game[7][4]==game[8][3]==game[9][2]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][9]==game[4][8]==game[5][7]==game[6][6]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]=="x") and (game[8][4]==None):
            game[7][4]=0
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[6][6]==game[7][5]==game[8][4]==game[9][3]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[4][9]==game[5][8]==game[6][7]==game[7][6]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]=="x") and (game[9][4]==None):
            game[8][4]=0
        elif (game[6][7]==game[7][6]==game[8][5]==game[9][4]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][9]==game[6][8]==game[7][7]==game[8][6]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[6][8]==game[7][7]==game[8][6]==game[9][5]=="x") and (game[5][9]==None):
            game[5][9]=0



        elif (game[0][0]==game[0][1]==game[0][2]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[0][7]==game[0][8]==game[0][9]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][0]==game[1][1]==game[1][2]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[1][7]==game[1][8]==game[1][9]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][0]==game[2][1]==game[2][2]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[2][7]==game[2][8]==game[2][9]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][0]==game[3][1]==game[3][2]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[3][7]==game[3][8]==game[3][9]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][0]==game[4][1]==game[4][2]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[4][7]==game[4][8]==game[4][9]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][0]==game[5][1]==game[5][2]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[5][7]==game[5][8]==game[5][9]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][0]==game[6][1]==game[6][2]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[6][7]==game[6][8]==game[6][9]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[7][0]==game[7][1]==game[7][2]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[7][7]==game[7][8]==game[7][9]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[8][0]==game[8][1]==game[8][2]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[8][7]==game[8][8]==game[8][9]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[9][0]==game[9][1]==game[9][2]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[9][7]==game[9][8]==game[9][9]=="x") and (game[9][6]==None):
            game[9][6]=0


        elif (game[0][0]==game[1][0]==game[2][0]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[7][0]==game[8][0]==game[9][0]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[0][1]==game[1][1]==game[2][1]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[7][1]==game[8][1]==game[9][1]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[0][2]==game[1][2]==game[2][2]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[7][2]==game[8][2]==game[9][2]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[0][3]==game[1][3]==game[2][3]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[7][3]==game[8][3]==game[9][3]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[0][4]==game[1][4]==game[2][4]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[7][4]==game[8][4]==game[9][4]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[0][5]==game[1][5]==game[2][5]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[7][5]==game[8][5]==game[9][5]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[0][6]==game[1][6]==game[2][6]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[7][6]==game[8][6]==game[9][6]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[0][7]==game[1][7]==game[2][7]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[7][7]==game[8][7]==game[9][7]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[0][8]==game[1][8]==game[2][8]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[7][8]==game[8][8]==game[9][8]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[0][9]==game[1][9]==game[2][9]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[7][9]==game[8][9]==game[9][9]=="x") and (game[6][9]==None):
            game[6][9]=0


        elif (game[4][0]==game[5][1]==game[6][2]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][1]==game[6][2]==game[7][3]=="x") and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][1]==game[6][2]==game[7][3]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][2]==game[7][3]==game[8][4]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[6][2]==game[7][3]==game[8][4]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[7][3]==game[8][4]==game[9][5]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][0]==game[4][1]==game[5][2]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][1]==game[5][2]==game[6][3]=="x") and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][1]==game[5][2]==game[6][3]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][2]==game[6][3]==game[7][4]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][2]==game[6][3]==game[7][4]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][3]==game[7][4]==game[8][5]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[6][3]==game[7][4]==game[8][5]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[7][4]==game[8][5]==game[9][6]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[2][0]==game[3][1]==game[4][2]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][1]==game[4][2]==game[5][3]=="x") and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][1]==game[4][2]==game[5][3]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][2]==game[5][3]==game[6][4]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][2]==game[5][3]==game[6][4]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][3]==game[6][4]==game[7][5]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][3]==game[6][4]==game[7][5]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[6][4]==game[7][5]==game[8][6]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[6][4]==game[7][5]==game[8][6]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[7][5]==game[8][6]==game[9][7]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[1][0]==game[2][1]==game[3][2]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][1]==game[3][2]==game[4][3]=="x") and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][1]==game[3][2]==game[4][3]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][2]==game[4][3]==game[5][4]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][2]==game[4][3]==game[5][4]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][3]==game[5][4]==game[6][5]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][3]==game[5][4]==game[6][5]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][4]==game[6][5]==game[7][6]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][4]==game[6][5]==game[7][6]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[6][5]==game[7][6]==game[8][7]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][5]==game[7][6]==game[8][7]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[7][6]==game[8][7]==game[9][8]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[0][0]==game[1][1]==game[2][2]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][1]==game[2][2]==game[3][3]=="x") and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][1]==game[2][2]==game[3][3]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][2]==game[3][3]==game[4][4]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][2]==game[3][3]==game[4][4]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][3]==game[4][4]==game[5][5]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][3]==game[4][4]==game[5][5]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][4]==game[5][5]==game[6][6]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][4]==game[5][5]==game[6][6]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[5][5]==game[6][6]==game[7][7]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][5]==game[6][6]==game[7][7]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[6][6]==game[7][7]==game[8][8]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][6]==game[7][7]==game[8][8]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[7][7]==game[8][8]==game[9][9]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[0][1]==game[1][2]==game[2][3]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][2]==game[2][3]==game[3][4]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][2]==game[2][3]==game[3][4]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][3]==game[3][4]==game[4][5]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][3]==game[3][4]==game[4][5]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][4]==game[4][5]==game[5][6]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][4]==game[4][5]==game[5][6]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[4][5]==game[5][6]==game[6][7]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][5]==game[5][6]==game[6][7]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[5][6]==game[6][7]==game[7][8]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][6]==game[6][7]==game[7][8]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[6][7]==game[7][8]==game[8][9]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[0][2]==game[1][3]==game[2][4]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][3]==game[2][4]==game[3][5]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][3]==game[2][4]==game[3][5]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][4]==game[3][5]==game[4][6]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][4]==game[3][5]==game[4][6]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[3][5]==game[4][6]==game[5][7]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][5]==game[4][6]==game[5][7]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[4][6]==game[5][7]==game[6][8]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][6]==game[5][7]==game[6][8]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[5][7]==game[6][8]==game[7][9]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[0][3]==game[1][4]==game[2][5]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][4]==game[2][5]==game[3][6]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][4]==game[2][5]==game[3][6]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[2][5]==game[3][6]==game[4][7]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][5]==game[3][6]==game[4][7]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[3][6]==game[4][7]==game[5][8]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][6]==game[4][7]==game[5][8]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[4][7]==game[5][8]==game[6][9]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[0][4]==game[1][5]==game[2][6]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[1][5]==game[2][6]==game[3][7]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][5]==game[2][6]==game[3][7]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[2][6]==game[3][7]==game[4][8]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][6]==game[3][7]==game[4][8]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[3][7]==game[4][8]==game[5][9]=="x") and (game[2][6]==None):
            game[2][6]=0


        elif (game[0][5]==game[1][4]==game[2][3]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[1][4]==game[2][3]==game[3][2]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][4]==game[2][3]==game[3][2]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[2][3]==game[3][2]==game[4][1]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][3]==game[3][2]==game[4][1]=="x") and (game[5][0]==None):
            game[5][0]=0
        elif (game[3][2]==game[4][1]==game[5][0]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[0][6]==game[1][5]==game[2][4]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][5]==game[2][4]==game[3][3]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][5]==game[2][4]==game[3][3]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[2][4]==game[3][3]==game[4][2]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][4]==game[3][3]==game[4][2]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][3]==game[4][2]==game[5][1]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][3]==game[4][2]==game[5][1]=="x") and (game[6][0]==None):
            game[6][0]=0
        elif (game[4][2]==game[5][1]==game[6][0]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[0][7]==game[1][6]==game[2][5]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][6]==game[2][5]==game[3][4]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][6]==game[2][5]==game[3][4]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][5]==game[3][4]==game[4][3]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][5]==game[3][4]==game[4][3]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[3][4]==game[4][3]==game[5][2]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][4]==game[4][3]==game[5][2]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[4][3]==game[5][2]==game[6][1]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][3]==game[5][2]==game[6][1]=="x") and (game[7][0]==None):
            game[7][0]=0
        elif (game[5][2]==game[6][1]==game[7][0]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[0][8]==game[1][7]==game[2][6]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][7]==game[2][6]==game[3][5]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][7]==game[2][6]==game[3][5]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][6]==game[3][5]==game[4][4]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][6]==game[3][5]==game[4][4]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][5]==game[4][4]==game[5][3]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][5]==game[4][4]==game[5][3]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[4][4]==game[5][3]==game[6][2]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][4]==game[5][3]==game[6][2]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[5][3]==game[6][2]==game[7][1]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][3]==game[6][2]==game[7][1]=="x") and (game[8][0]==None):
            game[8][0]=0
        elif (game[6][2]==game[7][1]==game[8][0]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[0][9]==game[1][8]==game[2][7]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][8]==game[2][7]==game[3][6]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][8]==game[2][7]==game[3][6]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][7]==game[3][6]==game[4][5]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][7]==game[3][6]==game[4][5]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][6]==game[4][5]==game[5][4]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][6]==game[4][5]==game[5][4]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][5]==game[5][4]==game[6][3]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][5]==game[5][4]==game[6][3]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[5][4]==game[6][3]==game[7][2]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][4]==game[6][3]==game[7][2]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[6][3]==game[7][2]==game[8][1]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][3]==game[7][2]==game[8][1]=="x") and (game[9][0]==None):
            game[9][0]=0
        elif (game[7][2]==game[8][1]==game[9][0]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[1][9]==game[2][8]==game[3][7]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][8]==game[3][7]==game[4][6]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][8]==game[3][7]==game[4][6]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][7]==game[4][6]==game[5][5]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][7]==game[4][6]==game[5][5]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][6]==game[5][5]==game[6][4]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][6]==game[5][5]==game[6][4]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][5]==game[6][4]==game[7][3]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][5]==game[6][4]==game[7][3]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[6][4]==game[7][3]==game[8][2]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][4]==game[7][3]==game[8][2]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[7][3]==game[8][2]==game[9][1]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[2][9]==game[3][8]==game[4][7]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][8]==game[4][7]==game[5][6]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][8]==game[4][7]==game[5][6]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][7]==game[5][6]==game[6][5]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][7]==game[5][6]==game[6][5]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][6]==game[6][5]==game[7][4]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][6]==game[6][5]==game[7][4]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[6][5]==game[7][4]==game[8][3]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][5]==game[7][4]==game[8][3]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[7][4]==game[8][3]==game[9][2]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][9]==game[4][8]==game[5][7]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][8]==game[5][7]==game[6][6]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][8]==game[5][7]==game[6][6]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][7]==game[6][6]==game[7][5]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][7]==game[6][6]==game[7][5]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][6]==game[7][5]==game[8][4]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[6][6]==game[7][5]==game[8][4]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[7][5]==game[8][4]==game[9][3]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][9]==game[5][8]==game[6][7]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][8]==game[6][7]==game[7][6]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][8]==game[6][7]==game[7][6]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][7]==game[7][6]==game[8][5]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[6][7]==game[7][6]==game[8][5]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[7][6]==game[8][5]==game[9][4]=="x") and (game[6][7]==None):
            game[6][7]=0



        elif (game[0][0]==game[0][1]==game[0][2]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][1]==game[0][2]==game[0][3]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[0][1]==game[0][2]==game[0][3]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][2]==game[0][3]==game[0][4]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[0][2]==game[0][3]==game[0][4]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][3]==game[0][4]==game[0][5]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[0][3]==game[0][4]==game[0][5]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[0][4]==game[0][5]==game[0][6]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][4]==game[0][5]==game[0][6]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[0][5]==game[0][6]==game[0][7]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][5]==game[0][6]==game[0][7]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[0][6]==game[0][7]==game[0][8]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][6]==game[0][7]==game[0][8]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[0][7]==game[0][8]==game[0][9]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][0]==game[1][1]==game[1][2]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][1]==game[1][2]==game[1][3]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[1][1]==game[1][2]==game[1][3]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][2]==game[1][3]==game[1][4]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[1][2]==game[1][3]==game[1][4]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][3]==game[1][4]==game[1][5]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[1][3]==game[1][4]==game[1][5]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[1][4]==game[1][5]==game[1][6]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][4]==game[1][5]==game[1][6]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[1][5]==game[1][6]==game[1][7]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][5]==game[1][6]==game[1][7]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[1][6]==game[1][7]==game[1][8]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][6]==game[1][7]==game[1][8]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[1][7]==game[1][8]==game[1][9]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][0]==game[2][1]==game[2][2]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][1]==game[2][2]==game[2][3]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[2][1]==game[2][2]==game[2][3]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][2]==game[2][3]==game[2][4]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[2][2]==game[2][3]==game[2][4]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][3]==game[2][4]==game[2][5]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[2][3]==game[2][4]==game[2][5]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[2][4]==game[2][5]==game[2][6]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][4]==game[2][5]==game[2][6]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[2][5]==game[2][6]==game[2][7]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][5]==game[2][6]==game[2][7]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[2][6]==game[2][7]==game[2][8]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][6]==game[2][7]==game[2][8]==0) and (game[2][9]==None):
            game[2][9]=0
        elif (game[2][7]==game[2][8]==game[2][9]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][0]==game[3][1]==game[3][2]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][1]==game[3][2]==game[3][3]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[3][1]==game[3][2]==game[3][3]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][2]==game[3][3]==game[3][4]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[3][2]==game[3][3]==game[3][4]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][3]==game[3][4]==game[3][5]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[3][3]==game[3][4]==game[3][5]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[3][4]==game[3][5]==game[3][6]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][4]==game[3][5]==game[3][6]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[3][5]==game[3][6]==game[3][7]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][5]==game[3][6]==game[3][7]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[3][6]==game[3][7]==game[3][8]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][6]==game[3][7]==game[3][8]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[3][7]==game[3][8]==game[3][9]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][0]==game[4][1]==game[4][2]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][1]==game[4][2]==game[4][3]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[4][1]==game[4][2]==game[4][3]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][2]==game[4][3]==game[4][4]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[4][2]==game[4][3]==game[4][4]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][3]==game[4][4]==game[4][5]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[4][3]==game[4][4]==game[4][5]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[4][4]==game[4][5]==game[4][6]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][4]==game[4][5]==game[4][6]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[4][5]==game[4][6]==game[4][7]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][5]==game[4][6]==game[4][7]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[4][6]==game[4][7]==game[4][8]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][6]==game[4][7]==game[4][8]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[4][7]==game[4][8]==game[4][9]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][0]==game[5][1]==game[5][2]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][1]==game[5][2]==game[5][3]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[5][1]==game[5][2]==game[5][3]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][2]==game[5][3]==game[5][4]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[5][2]==game[5][3]==game[5][4]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][3]==game[5][4]==game[5][5]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[5][3]==game[5][4]==game[5][5]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[5][4]==game[5][5]==game[5][6]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][4]==game[5][5]==game[5][6]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[5][5]==game[5][6]==game[5][7]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][5]==game[5][6]==game[5][7]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][6]==game[5][7]==game[5][8]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][6]==game[5][7]==game[5][8]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[5][7]==game[5][8]==game[5][9]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][0]==game[6][1]==game[6][2]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][1]==game[6][2]==game[6][3]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[6][1]==game[6][2]==game[6][3]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][2]==game[6][3]==game[6][4]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[6][2]==game[6][3]==game[6][4]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][3]==game[6][4]==game[6][5]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[6][3]==game[6][4]==game[6][5]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[6][4]==game[6][5]==game[6][6]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][4]==game[6][5]==game[6][6]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[6][5]==game[6][6]==game[6][7]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][5]==game[6][6]==game[6][7]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[6][6]==game[6][7]==game[6][8]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][6]==game[6][7]==game[6][8]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[6][7]==game[6][8]==game[6][9]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[7][0]==game[7][1]==game[7][2]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][1]==game[7][2]==game[7][3]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[7][1]==game[7][2]==game[7][3]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][2]==game[7][3]==game[7][4]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[7][2]==game[7][3]==game[7][4]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][3]==game[7][4]==game[7][5]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[7][3]==game[7][4]==game[7][5]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[7][4]==game[7][5]==game[7][6]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][4]==game[7][5]==game[7][6]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[7][5]==game[7][6]==game[7][7]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][5]==game[7][6]==game[7][7]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[7][6]==game[7][7]==game[7][8]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][6]==game[7][7]==game[7][8]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[7][7]==game[7][8]==game[7][9]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[8][0]==game[8][1]==game[8][2]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][1]==game[8][2]==game[8][3]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[8][1]==game[8][2]==game[8][3]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][2]==game[8][3]==game[8][4]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[8][2]==game[8][3]==game[8][4]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][3]==game[8][4]==game[8][5]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[8][3]==game[8][4]==game[8][5]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[8][4]==game[8][5]==game[8][6]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][4]==game[8][5]==game[8][6]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[8][5]==game[8][6]==game[8][7]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][5]==game[8][6]==game[8][7]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[8][6]==game[8][7]==game[8][8]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][6]==game[8][7]==game[8][8]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[8][7]==game[8][8]==game[8][9]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[9][0]==game[9][1]==game[9][2]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][1]==game[9][2]==game[9][3]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[9][1]==game[9][2]==game[9][3]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][2]==game[9][3]==game[9][4]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[9][2]==game[9][3]==game[9][4]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][3]==game[9][4]==game[9][5]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[9][3]==game[9][4]==game[9][5]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[9][4]==game[9][5]==game[9][6]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][4]==game[9][5]==game[9][6]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[9][5]==game[9][6]==game[9][7]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][5]==game[9][6]==game[9][7]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[9][6]==game[9][7]==game[9][8]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][6]==game[9][7]==game[9][8]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[9][7]==game[9][8]==game[9][9]==0) and (game[9][6]==None):
            game[9][6]=0


        elif (game[0][0]==game[1][0]==game[2][0]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][0]==game[2][0]==game[3][0]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][0]==game[3][0]==game[4][0]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][0]==game[4][0]==game[5][0]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][0]==game[5][0]==game[6][0]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][0]==game[6][0]==game[7][0]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[6][0]==game[7][0]==game[8][0]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[7][0]==game[8][0]==game[9][0]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[0][1]==game[1][1]==game[2][1]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][1]==game[2][1]==game[3][1]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][1]==game[3][1]==game[4][1]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][1]==game[4][1]==game[5][1]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][1]==game[5][1]==game[6][1]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][1]==game[6][1]==game[7][1]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[6][1]==game[7][1]==game[8][1]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[7][1]==game[8][1]==game[9][1]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[0][2]==game[1][2]==game[2][2]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][2]==game[2][2]==game[3][2]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][2]==game[3][2]==game[4][2]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][2]==game[4][2]==game[5][2]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][2]==game[5][2]==game[6][2]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][2]==game[6][2]==game[7][2]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[6][2]==game[7][2]==game[8][2]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[7][2]==game[8][2]==game[9][2]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[0][3]==game[1][3]==game[2][3]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][3]==game[2][3]==game[3][3]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][3]==game[3][3]==game[4][3]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][3]==game[4][3]==game[5][3]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][3]==game[5][3]==game[6][3]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][3]==game[6][3]==game[7][3]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[6][3]==game[7][3]==game[8][3]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[7][3]==game[8][3]==game[9][3]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[0][4]==game[1][4]==game[2][4]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][4]==game[2][4]==game[3][4]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][4]==game[3][4]==game[4][4]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][4]==game[4][4]==game[5][4]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][4]==game[5][4]==game[6][4]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][4]==game[6][4]==game[7][4]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][4]==game[7][4]==game[8][4]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[7][4]==game[8][4]==game[9][4]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[0][5]==game[1][5]==game[2][5]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][5]==game[2][5]==game[3][5]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][5]==game[3][5]==game[4][5]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][5]==game[4][5]==game[5][5]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][5]==game[5][5]==game[6][5]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][5]==game[6][5]==game[7][5]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][5]==game[7][5]==game[8][5]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[7][5]==game[8][5]==game[9][5]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[0][6]==game[1][6]==game[2][6]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][6]==game[2][6]==game[3][6]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][6]==game[3][6]==game[4][6]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][6]==game[4][6]==game[5][6]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][6]==game[5][6]==game[6][6]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][6]==game[6][6]==game[7][6]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][6]==game[7][6]==game[8][6]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[7][6]==game[8][6]==game[9][6]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[0][7]==game[1][7]==game[2][7]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][7]==game[2][7]==game[3][7]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][7]==game[3][7]==game[4][7]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][7]==game[4][7]==game[5][7]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][7]==game[5][7]==game[6][7]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][7]==game[6][7]==game[7][7]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[6][7]==game[7][7]==game[8][7]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[7][7]==game[8][7]==game[9][7]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[0][8]==game[1][8]==game[2][8]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][8]==game[2][8]==game[3][8]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][8]==game[3][8]==game[4][8]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][8]==game[4][8]==game[5][8]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][8]==game[5][8]==game[6][8]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][8]==game[6][8]==game[7][8]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[6][8]==game[7][8]==game[8][8]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[7][8]==game[8][8]==game[9][8]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[0][9]==game[1][9]==game[2][9]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][9]==game[2][9]==game[3][9]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][9]==game[3][9]==game[4][9]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==0) and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][9]==game[4][9]==game[5][9]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][9]==game[5][9]==game[6][9]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][9]==game[6][9]==game[7][9]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[6][9]==game[7][9]==game[8][9]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[7][9]==game[8][9]==game[9][9]==0) and (game[6][9]==None):
            game[6][9]=0


        elif (game[4][0]==game[5][1]==game[6][2]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][1]==game[6][2]==game[7][3]==0) and (game[4][0]==None):
            game[4][0]=0
        elif (game[5][1]==game[6][2]==game[7][3]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][2]==game[7][3]==game[8][4]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[6][2]==game[7][3]==game[8][4]==0) and (game[9][5]==None):
            game[9][5]=0
        elif (game[7][3]==game[8][4]==game[9][5]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[3][0]==game[4][1]==game[5][2]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][1]==game[5][2]==game[6][3]==0) and (game[3][0]==None):
            game[3][0]=0
        elif (game[4][1]==game[5][2]==game[6][3]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][2]==game[6][3]==game[7][4]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[5][2]==game[6][3]==game[7][4]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][3]==game[7][4]==game[8][5]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[6][3]==game[7][4]==game[8][5]==0) and (game[9][6]==None):
            game[9][6]=0
        elif (game[7][4]==game[8][5]==game[9][6]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[2][0]==game[3][1]==game[4][2]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][1]==game[4][2]==game[5][3]==0) and (game[2][0]==None):
            game[2][0]=0
        elif (game[3][1]==game[4][2]==game[5][3]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][2]==game[5][3]==game[6][4]==0) and (game[3][1]==None):
            game[3][1]=0
        elif (game[4][2]==game[5][3]==game[6][4]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][3]==game[6][4]==game[7][5]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[5][3]==game[6][4]==game[7][5]==0) and (game[8][6]==None):
            game[8][6]=0
        elif (game[6][4]==game[7][5]==game[8][6]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[6][4]==game[7][5]==game[8][6]==0) and (game[9][7]==None):
            game[9][7]=0
        elif (game[7][5]==game[8][6]==game[9][7]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[1][0]==game[2][1]==game[3][2]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][1]==game[3][2]==game[4][3]==0) and (game[1][0]==None):
            game[1][0]=0
        elif (game[2][1]==game[3][2]==game[4][3]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][2]==game[4][3]==game[5][4]==0) and (game[2][1]==None):
            game[2][1]=0
        elif (game[3][2]==game[4][3]==game[5][4]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][3]==game[5][4]==game[6][5]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[4][3]==game[5][4]==game[6][5]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][4]==game[6][5]==game[7][6]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[5][4]==game[6][5]==game[7][6]==0) and (game[8][7]==None):
            game[8][7]=0
        elif (game[6][5]==game[7][6]==game[8][7]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][5]==game[7][6]==game[8][7]==0) and (game[9][8]==None):
            game[9][8]=0
        elif (game[7][6]==game[8][7]==game[9][8]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[0][0]==game[1][1]==game[2][2]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][1]==game[2][2]==game[3][3]==0) and (game[0][0]==None):
            game[0][0]=0
        elif (game[1][1]==game[2][2]==game[3][3]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][2]==game[3][3]==game[4][4]==0) and (game[1][1]==None):
            game[1][1]=0
        elif (game[2][2]==game[3][3]==game[4][4]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][3]==game[4][4]==game[5][5]==0) and (game[2][2]==None):
            game[2][2]=0
        elif (game[3][3]==game[4][4]==game[5][5]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][4]==game[5][5]==game[6][6]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[4][4]==game[5][5]==game[6][6]==0) and (game[7][7]==None):
            game[7][7]=0
        elif (game[5][5]==game[6][6]==game[7][7]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][5]==game[6][6]==game[7][7]==0) and (game[8][8]==None):
            game[8][8]=0
        elif (game[6][6]==game[7][7]==game[8][8]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][6]==game[7][7]==game[8][8]==0) and (game[9][9]==None):
            game[9][9]=0
        elif (game[7][7]==game[8][8]==game[9][9]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[0][1]==game[1][2]==game[2][3]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][2]==game[2][3]==game[3][4]==0) and (game[0][1]==None):
            game[0][1]=0
        elif (game[1][2]==game[2][3]==game[3][4]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][3]==game[3][4]==game[4][5]==0) and (game[1][2]==None):
            game[1][2]=0
        elif (game[2][3]==game[3][4]==game[4][5]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][4]==game[4][5]==game[5][6]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[3][4]==game[4][5]==game[5][6]==0) and (game[6][7]==None):
            game[6][7]=0
        elif (game[4][5]==game[5][6]==game[6][7]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][5]==game[5][6]==game[6][7]==0) and (game[7][8]==None):
            game[7][8]=0
        elif (game[5][6]==game[6][7]==game[7][8]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][6]==game[6][7]==game[7][8]==0) and (game[8][9]==None):
            game[8][9]=0
        elif (game[6][7]==game[7][8]==game[8][9]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[0][2]==game[1][3]==game[2][4]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][3]==game[2][4]==game[3][5]==0) and (game[0][2]==None):
            game[0][2]=0
        elif (game[1][3]==game[2][4]==game[3][5]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][4]==game[3][5]==game[4][6]==0) and (game[1][3]==None):
            game[1][3]=0
        elif (game[2][4]==game[3][5]==game[4][6]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[3][5]==game[4][6]==game[5][7]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][5]==game[4][6]==game[5][7]==0) and (game[6][8]==None):
            game[6][8]=0
        elif (game[4][6]==game[5][7]==game[6][8]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][6]==game[5][7]==game[6][8]==0) and (game[7][9]==None):
            game[7][9]=0
        elif (game[5][7]==game[6][8]==game[7][9]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[0][3]==game[1][4]==game[2][5]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][4]==game[2][5]==game[3][6]==0) and (game[0][3]==None):
            game[0][3]=0
        elif (game[1][4]==game[2][5]==game[3][6]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[2][5]==game[3][6]==game[4][7]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][5]==game[3][6]==game[4][7]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[3][6]==game[4][7]==game[5][8]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][6]==game[4][7]==game[5][8]==0) and (game[6][9]==None):
            game[6][9]=0
        elif (game[4][7]==game[5][8]==game[6][9]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[0][4]==game[1][5]==game[2][6]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[1][5]==game[2][6]==game[3][7]==0) and (game[0][4]==None):
            game[0][4]=0
        elif (game[1][5]==game[2][6]==game[3][7]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[2][6]==game[3][7]==game[4][8]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][6]==game[3][7]==game[4][8]==0) and (game[5][9]==None):
            game[5][9]=0
        elif (game[3][7]==game[4][8]==game[5][9]==0) and (game[2][6]==None):
            game[2][6]=0


        elif (game[0][5]==game[1][4]==game[2][3]==0) and (game[3][2]==None):
            game[3][2]=0
        elif (game[1][4]==game[2][3]==game[3][2]==0) and (game[0][5]==None):
            game[0][5]=0
        elif (game[1][4]==game[2][3]==game[3][2]==0) and (game[4][1]==None):
            game[4][1]=0
        elif (game[2][3]==game[3][2]==game[4][1]==0) and (game[1][4]==None):
            game[1][4]=0
        elif (game[2][3]==game[3][2]==game[4][1]==0) and (game[5][0]==None):
            game[5][0]=0
        elif (game[3][2]==game[4][1]==game[5][0]==0) and (game[2][3]==None):
            game[2][3]=0
        elif (game[0][6]==game[1][5]==game[2][4]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[1][5]==game[2][4]==game[3][3]==0) and (game[0][6]==None):
            game[0][6]=0
        elif (game[1][5]==game[2][4]==game[3][3]==0) and (game[4][2]==None):
            game[4][2]=0
        elif (game[2][4]==game[3][3]==game[4][2]==0) and (game[1][5]==None):
            game[1][5]=0
        elif (game[2][4]==game[3][3]==game[4][2]==0) and (game[5][1]==None):
            game[5][1]=0
        elif (game[3][3]==game[4][2]==game[5][1]==0) and (game[2][4]==None):
            game[2][4]=0
        elif (game[3][3]==game[4][2]==game[5][1]==0) and (game[6][0]==None):
            game[6][0]=0
        elif (game[4][2]==game[5][1]==game[6][0]==0) and (game[3][3]==None):
            game[3][3]=0
        elif (game[0][7]==game[1][6]==game[2][5]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[1][6]==game[2][5]==game[3][4]==0) and (game[0][7]==None):
            game[0][7]=0
        elif (game[1][6]==game[2][5]==game[3][4]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[2][5]==game[3][4]==game[4][3]==0) and (game[1][6]==None):
            game[1][6]=0
        elif (game[2][5]==game[3][4]==game[4][3]==0) and (game[5][2]==None):
            game[5][2]=0
        elif (game[3][4]==game[4][3]==game[5][2]==0) and (game[2][5]==None):
            game[2][5]=0
        elif (game[3][4]==game[4][3]==game[5][2]==0) and (game[6][1]==None):
            game[6][1]=0
        elif (game[4][3]==game[5][2]==game[6][1]==0) and (game[3][4]==None):
            game[3][4]=0
        elif (game[4][3]==game[5][2]==game[6][1]==0) and (game[7][0]==None):
            game[7][0]=0
        elif (game[5][2]==game[6][1]==game[7][0]==0) and (game[4][3]==None):
            game[4][3]=0
        elif (game[0][8]==game[1][7]==game[2][6]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[1][7]==game[2][6]==game[3][5]==0) and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][7]==game[2][6]==game[3][5]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[2][6]==game[3][5]==game[4][4]==0) and (game[1][7]==None):
            game[1][7]=0
        elif (game[2][6]==game[3][5]==game[4][4]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[3][5]==game[4][4]==game[5][3]==0) and (game[2][6]==None):
            game[2][6]=0
        elif (game[3][5]==game[4][4]==game[5][3]==0) and (game[6][2]==None):
            game[6][2]=0
        elif (game[4][4]==game[5][3]==game[6][2]==0) and (game[3][5]==None):
            game[3][5]=0
        elif (game[4][4]==game[5][3]==game[6][2]==0) and (game[7][1]==None):
            game[7][1]=0
        elif (game[5][3]==game[6][2]==game[7][1]==0) and (game[4][4]==None):
            game[4][4]=0
        elif (game[5][3]==game[6][2]==game[7][1]==0) and (game[8][0]==None):
            game[8][0]=0
        elif (game[6][2]==game[7][1]==game[8][0]==0) and (game[5][3]==None):
            game[5][3]=0
        elif (game[0][9]==game[1][8]==game[2][7]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[1][8]==game[2][7]==game[3][6]==0) and (game[0][9]==None):
            game[0][9]=0
        elif (game[1][8]==game[2][7]==game[3][6]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[2][7]==game[3][6]==game[4][5]==0) and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][7]==game[3][6]==game[4][5]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[3][6]==game[4][5]==game[5][4]==0) and (game[2][7]==None):
            game[2][7]=0
        elif (game[3][6]==game[4][5]==game[5][4]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[4][5]==game[5][4]==game[6][3]==0) and (game[3][6]==None):
            game[3][6]=0
        elif (game[4][5]==game[5][4]==game[6][3]==0) and (game[7][2]==None):
            game[7][2]=0
        elif (game[5][4]==game[6][3]==game[7][2]==0) and (game[4][5]==None):
            game[4][5]=0
        elif (game[5][4]==game[6][3]==game[7][2]==0) and (game[8][1]==None):
            game[8][1]=0
        elif (game[6][3]==game[7][2]==game[8][1]==0) and (game[5][4]==None):
            game[5][4]=0
        elif (game[6][3]==game[7][2]==game[8][1]==0) and (game[9][0]==None):
            game[9][0]=0
        elif (game[7][2]==game[8][1]==game[9][0]==0) and (game[6][3]==None):
            game[6][3]=0
        elif (game[1][9]==game[2][8]==game[3][7]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[2][8]==game[3][7]==game[4][6]==0) and (game[1][9]==None):
            game[1][9]=0
        elif (game[2][8]==game[3][7]==game[4][6]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[3][7]==game[4][6]==game[5][5]==0) and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][7]==game[4][6]==game[5][5]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[4][6]==game[5][5]==game[6][4]==0) and (game[3][7]==None):
            game[3][7]=0
        elif (game[4][6]==game[5][5]==game[6][4]==0) and (game[7][3]==None):
            game[7][3]=0
        elif (game[5][5]==game[6][4]==game[7][3]==0) and (game[4][6]==None):
            game[4][6]=0
        elif (game[5][5]==game[6][4]==game[7][3]==0) and (game[8][2]==None):
            game[8][2]=0
        elif (game[6][4]==game[7][3]==game[8][2]==0) and (game[5][5]==None):
            game[5][5]=0
        elif (game[6][4]==game[7][3]==game[8][2]==0) and (game[9][1]==None):
            game[9][1]=0
        elif (game[7][3]==game[8][2]==game[9][1]==0) and (game[6][4]==None):
            game[6][4]=0
        elif (game[2][9]==game[3][8]==game[4][7]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[3][8]==game[4][7]==game[5][6]==0) and (game[2][9]==None):
            game[2][9]=0
        elif (game[3][8]==game[4][7]==game[5][6]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[4][7]==game[5][6]==game[6][5]==0) and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][7]==game[5][6]==game[6][5]==0) and (game[7][4]==None):
            game[7][4]=0
        elif (game[5][6]==game[6][5]==game[7][4]==0) and (game[4][7]==None):
            game[4][7]=0
        elif (game[5][6]==game[6][5]==game[7][4]==0) and (game[8][3]==None):
            game[8][3]=0
        elif (game[6][5]==game[7][4]==game[8][3]==0) and (game[5][6]==None):
            game[5][6]=0
        elif (game[6][5]==game[7][4]==game[8][3]==0) and (game[9][2]==None):
            game[9][2]=0
        elif (game[7][4]==game[8][3]==game[9][2]==0) and (game[6][5]==None):
            game[6][5]=0
        elif (game[3][9]==game[4][8]==game[5][7]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][8]==game[5][7]==game[6][6]==0) and (game[3][9]==None):
            game[3][9]=0
        elif (game[4][8]==game[5][7]==game[6][6]==0) and (game[7][5]==None):
            game[7][5]=0
        elif (game[5][7]==game[6][6]==game[7][5]==0) and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][7]==game[6][6]==game[7][5]==0) and (game[8][4]==None):
            game[8][4]=0
        elif (game[6][6]==game[7][5]==game[8][4]==0) and (game[5][7]==None):
            game[5][7]=0
        elif (game[6][6]==game[7][5]==game[8][4]==0) and (game[9][3]==None):
            game[9][3]=0
        elif (game[7][5]==game[8][4]==game[9][3]==0) and (game[6][6]==None):
            game[6][6]=0
        elif (game[4][9]==game[5][8]==game[6][7]==0) and (game[7][6]==None):
            game[7][6]=0
        elif (game[5][8]==game[6][7]==game[7][6]==0) and (game[4][9]==None):
            game[4][9]=0
        elif (game[5][8]==game[6][7]==game[7][6]==0) and (game[8][5]==None):
            game[8][5]=0
        elif (game[6][7]==game[7][6]==game[8][5]==0) and (game[5][8]==None):
            game[5][8]=0
        elif (game[6][7]==game[7][6]==game[8][5]==0) and (game[9][4]==None):
            game[9][4]=0
        elif (game[7][6]==game[8][5]==game[9][4]==0) and (game[6][7]==None):
            game[6][7]=0



        elif (game[0][0]=="x") and (game[0][1]==None):
            game[0][1]=0
        elif (game[0][1]=="x") and (game[0][2]==None):
            game[0][2]=0
        elif (game[0][2]=="x") and (game[0][3]==None):
            game[0][3]=0
        elif (game[0][3]=="x") and (game[0][4]==None):
            game[0][4]=0
        elif (game[0][4]=="x") and (game[0][5]==None):
            game[0][5]=0
        elif (game[0][5]=="x") and (game[0][6]==None):
            game[0][6]=0
        elif (game[0][6]=="x") and (game[0][7]==None):
            game[0][7]=0
        elif (game[0][7]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[0][8]=="x") and (game[0][9]==None):
            game[0][9]=0
        elif (game[0][9]=="x") and (game[0][8]==None):
            game[0][8]=0
        elif (game[1][0]=="x") and (game[1][1]==None):
            game[1][1]=0
        elif (game[1][1]=="x") and (game[1][2]==None):
            game[1][2]=0
        elif (game[1][2]=="x") and (game[1][3]==None):
            game[1][3]=0
        elif (game[1][3]=="x") and (game[1][4]==None):
            game[1][4]=0
        elif (game[1][4]=="x") and (game[1][5]==None):
            game[1][5]=0
        elif (game[1][5]=="x") and (game[1][6]==None):
            game[1][6]=0
        elif (game[1][6]=="x") and (game[1][7]==None):
            game[1][7]=0
        elif (game[1][7]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[1][8]=="x") and (game[1][9]==None):
            game[1][9]=0
        elif (game[1][9]=="x") and (game[1][8]==None):
            game[1][8]=0
        elif (game[2][0]=="x") and (game[2][1]==None):
            game[2][1]=0
        elif (game[2][1]=="x") and (game[2][2]==None):
            game[2][2]=0
        elif (game[2][2]=="x") and (game[2][3]==None):
            game[2][3]=0
        elif (game[2][3]=="x") and (game[2][4]==None):
            game[2][4]=0
        elif (game[2][4]=="x") and (game[2][5]==None):
            game[2][5]=0
        elif (game[2][5]=="x") and (game[2][6]==None):
            game[2][6]=0
        elif (game[2][6]=="x") and (game[2][7]==None):
            game[2][7]=0
        elif (game[2][7]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[2][8]=="x") and (game[2][9]==None):
            game[2][9]=0
        elif (game[2][9]=="x") and (game[2][8]==None):
            game[2][8]=0
        elif (game[3][0]=="x") and (game[3][1]==None):
            game[3][1]=0
        elif (game[3][1]=="x") and (game[3][2]==None):
            game[3][2]=0
        elif (game[3][2]=="x") and (game[3][3]==None):
            game[3][3]=0
        elif (game[3][3]=="x") and (game[3][4]==None):
            game[3][4]=0
        elif (game[3][4]=="x") and (game[3][5]==None):
            game[3][5]=0
        elif (game[3][5]=="x") and (game[3][6]==None):
            game[3][6]=0
        elif (game[3][6]=="x") and (game[3][7]==None):
            game[3][7]=0
        elif (game[3][7]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[3][8]=="x") and (game[3][9]==None):
            game[3][9]=0
        elif (game[3][9]=="x") and (game[3][8]==None):
            game[3][8]=0
        elif (game[4][0]=="x") and (game[4][1]==None):
            game[4][1]=0
        elif (game[4][1]=="x") and (game[4][2]==None):
            game[4][2]=0
        elif (game[4][2]=="x") and (game[4][3]==None):
            game[4][3]=0
        elif (game[4][3]=="x") and (game[4][4]==None):
            game[4][4]=0
        elif (game[4][4]=="x") and (game[4][5]==None):
            game[4][5]=0
        elif (game[4][5]=="x") and (game[4][6]==None):
            game[4][6]=0
        elif (game[4][6]=="x") and (game[4][7]==None):
            game[4][7]=0
        elif (game[4][7]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[4][8]=="x") and (game[4][9]==None):
            game[4][9]=0
        elif (game[4][9]=="x") and (game[4][8]==None):
            game[4][8]=0
        elif (game[5][0]=="x") and (game[5][1]==None):
            game[5][1]=0
        elif (game[5][1]=="x") and (game[5][2]==None):
            game[5][2]=0
        elif (game[5][2]=="x") and (game[5][3]==None):
            game[5][3]=0
        elif (game[5][3]=="x") and (game[5][4]==None):
            game[5][4]=0
        elif (game[5][4]=="x") and (game[5][5]==None):
            game[5][5]=0
        elif (game[5][5]=="x") and (game[5][6]==None):
            game[5][6]=0
        elif (game[5][6]=="x") and (game[5][7]==None):
            game[5][7]=0
        elif (game[5][7]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[5][8]=="x") and (game[5][9]==None):
            game[5][9]=0
        elif (game[5][9]=="x") and (game[5][8]==None):
            game[5][8]=0
        elif (game[6][0]=="x") and (game[6][1]==None):
            game[6][1]=0
        elif (game[6][1]=="x") and (game[6][2]==None):
            game[6][2]=0
        elif (game[6][2]=="x") and (game[6][3]==None):
            game[6][3]=0
        elif (game[6][3]=="x") and (game[6][4]==None):
            game[6][4]=0
        elif (game[6][4]=="x") and (game[6][5]==None):
            game[6][5]=0
        elif (game[6][5]=="x") and (game[6][6]==None):
            game[6][6]=0
        elif (game[6][6]=="x") and (game[6][7]==None):
            game[6][7]=0
        elif (game[6][7]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[6][8]=="x") and (game[6][9]==None):
            game[6][9]=0
        elif (game[6][9]=="x") and (game[6][8]==None):
            game[6][8]=0
        elif (game[7][0]=="x") and (game[7][1]==None):
            game[7][1]=0
        elif (game[7][1]=="x") and (game[7][2]==None):
            game[7][2]=0
        elif (game[7][2]=="x") and (game[7][3]==None):
            game[7][3]=0
        elif (game[7][3]=="x") and (game[7][4]==None):
            game[7][4]=0
        elif (game[7][4]=="x") and (game[7][5]==None):
            game[7][5]=0
        elif (game[7][5]=="x") and (game[7][6]==None):
            game[7][6]=0
        elif (game[7][6]=="x") and (game[7][7]==None):
            game[7][7]=0
        elif (game[7][7]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[7][8]=="x") and (game[7][9]==None):
            game[7][9]=0
        elif (game[7][9]=="x") and (game[7][8]==None):
            game[7][8]=0
        elif (game[8][0]=="x") and (game[8][1]==None):
            game[8][1]=0
        elif (game[8][1]=="x") and (game[8][2]==None):
            game[8][2]=0
        elif (game[8][2]=="x") and (game[8][3]==None):
            game[8][3]=0
        elif (game[8][3]=="x") and (game[8][4]==None):
            game[8][4]=0
        elif (game[8][4]=="x") and (game[8][5]==None):
            game[8][5]=0
        elif (game[8][5]=="x") and (game[8][6]==None):
            game[8][6]=0
        elif (game[8][6]=="x") and (game[8][7]==None):
            game[8][7]=0
        elif (game[8][7]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[8][8]=="x") and (game[8][9]==None):
            game[8][9]=0
        elif (game[8][9]=="x") and (game[8][8]==None):
            game[8][8]=0
        elif (game[9][0]=="x") and (game[9][1]==None):
            game[9][1]=0
        elif (game[9][1]=="x") and (game[9][2]==None):
            game[9][2]=0
        elif (game[9][2]=="x") and (game[9][3]==None):
            game[9][3]=0
        elif (game[9][3]=="x") and (game[9][4]==None):
            game[9][4]=0
        elif (game[9][4]=="x") and (game[9][5]==None):
            game[9][5]=0
        elif (game[9][5]=="x") and (game[9][6]==None):
            game[9][6]=0
        elif (game[9][6]=="x") and (game[9][7]==None):
            game[9][7]=0
        elif (game[9][7]=="x") and (game[9][8]==None):
            game[9][8]=0
        elif (game[9][8]=="x") and (game[9][9]==None):
            game[9][9]=0
        elif (game[9][9]=="x") and (game[9][8]==None):
            game[9][8]=0



        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) or (game[0][1]==game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) or (game[0][2]==game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) or (game[0][3]==game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) or (game[0][4]==game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) or (game[0][5]==game[0][6]==game[0][7]==game[0][8]==game[0][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[1][0]==game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) or (game[1][1]==game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) or (game[1][2]==game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) or (game[1][3]==game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) or (game[1][4]==game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) or (game[1][5]==game[1][6]==game[1][7]==game[1][8]==game[1][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[2][0]==game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) or (game[2][1]==game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) or (game[2][2]==game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) or (game[2][3]==game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) or (game[2][4]==game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) or (game[2][5]==game[2][6]==game[2][7]==game[2][8]==game[2][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[3][0]==game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) or (game[3][1]==game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) or (game[3][2]==game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) or (game[3][3]==game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) or (game[3][4]==game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) or (game[3][5]==game[3][6]==game[3][7]==game[3][8]==game[3][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[4][0]==game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) or (game[4][1]==game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) or (game[4][2]==game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) or (game[4][3]==game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) or (game[4][4]==game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) or (game[4][5]==game[4][6]==game[4][7]==game[4][8]==game[4][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[5][0]==game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) or (game[5][1]==game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) or (game[5][2]==game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) or (game[5][3]==game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) or (game[5][4]==game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) or (game[5][5]==game[5][6]==game[5][7]==game[5][8]==game[5][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[6][0]==game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) or (game[6][1]==game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) or (game[6][2]==game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) or (game[6][3]==game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) or (game[6][4]==game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) or (game[6][5]==game[6][6]==game[6][7]==game[6][8]==game[6][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[7][0]==game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) or (game[7][1]==game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) or (game[7][2]==game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) or (game[7][3]==game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) or (game[7][4]==game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) or (game[7][5]==game[7][6]==game[7][7]==game[7][8]==game[7][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[8][0]==game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) or (game[8][1]==game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) or (game[8][2]==game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) or (game[8][3]==game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) or (game[8][4]==game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) or (game[8][5]==game[8][6]==game[8][7]==game[8][8]==game[8][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[9][0]==game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) or (game[9][1]==game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) or (game[9][2]==game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) or (game[9][3]==game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) or (game[9][4]==game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) or (game[9][5]==game[9][6]==game[9][7]==game[9][8]==game[9][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[5][0]==game[6][1]==game[7][2]==game[8][3]==game[9][4]==0) or (game[4][0]==game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) or (game[5][1]==game[6][2]==game[7][3]==game[8][4]==game[9][5]==0) or (game[3][0]==game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) or (game[4][1]==game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) or (game[5][2]==game[6][3]==game[7][4]==game[8][5]==game[9][6]==0) or (game[2][0]==game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) or (game[3][1]==game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) or (game[4][2]==game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) or (game[5][3]==game[6][4]==game[7][5]==game[8][6]==game[9][7]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[1][0]==game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) or (game[2][1]==game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) or (game[3][2]==game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) or (game[4][3]==game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) or (game[5][4]==game[6][5]==game[7][6]==game[8][7]==game[9][8]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][0]==game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) or (game[1][1]==game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) or (game[2][2]==game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) or (game[3][3]==game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) or (game[4][4]==game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) or (game[5][5]==game[6][6]==game[7][7]==game[8][8]==game[9][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][1]==game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) or (game[1][2]==game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) or (game[2][3]==game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) or (game[3][4]==game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) or (game[4][5]==game[5][6]==game[6][7]==game[7][8]==game[8][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][2]==game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) or (game[1][3]==game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) or (game[2][4]==game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) or (game[3][5]==game[4][6]==game[5][7]==game[6][8]==game[7][9]==0) or (game[0][3]==game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) or (game[1][4]==game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) or (game[2][5]==game[3][6]==game[4][7]==game[5][8]==game[6][9]==0) or (game[0][4]==game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) or (game[1][5]==game[2][6]==game[3][7]==game[4][8]==game[5][9]==0) or (game[0][5]==game[1][6]==game[2][7]==game[3][8]==game[4][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[4][0]==game[3][1]==game[2][2]==game[1][3]==game[0][4]==0) or (game[5][0]==game[4][1]==game[3][2]==game[2][3]==game[1][4]==0) or (game[4][1]==game[3][2]==game[2][3]==game[1][4]==game[0][5]==0) or (game[6][0]==game[5][1]==game[4][2]==game[3][3]==game[2][4]==0) or (game[5][1]==game[4][2]==game[3][3]==game[2][4]==game[1][5]==0) or (game[4][2]==game[3][3]==game[2][4]==game[1][5]==game[0][6]==0) or (game[7][0]==game[6][1]==game[5][2]==game[4][3]==game[3][4]==0) or (game[6][1]==game[5][2]==game[4][3]==game[3][4]==game[2][5]==0) or (game[5][2]==game[4][3]==game[3][4]==game[2][5]==game[1][6]==0) or (game[4][3]==game[3][4]==game[2][5]==game[1][6]==game[0][7]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[8][0]==game[7][1]==game[6][2]==game[5][3]==game[4][4]==0) or (game[7][1]==game[6][2]==game[5][3]==game[4][4]==game[3][5]==0) or (game[6][2]==game[5][3]==game[4][4]==game[3][5]==game[2][6]==0) or (game[5][3]==game[4][4]==game[3][5]==game[2][6]==game[1][7]==0) or (game[4][4]==game[3][5]==game[2][6]==game[1][7]==game[0][8]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[9][0]==game[8][1]==game[7][2]==game[6][3]==game[5][4]==0) or (game[8][1]==game[7][2]==game[6][3]==game[5][4]==game[4][5]==0) or (game[7][2]==game[6][3]==game[5][4]==game[4][5]==game[3][6]==0) or (game[6][3]==game[5][4]==game[4][5]==game[3][6]==game[2][7]==0) or (game[5][4]==game[4][5]==game[3][6]==game[2][7]==game[1][8]==0) or (game[4][5]==game[3][6]==game[2][7]==game[1][8]==game[0][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[9][1]==game[8][2]==game[7][3]==game[6][4]==game[5][5]==0) or (game[8][2]==game[7][3]==game[6][4]==game[5][5]==game[4][6]==0) or (game[7][3]==game[6][4]==game[5][5]==game[4][6]==game[3][7]==0) or (game[6][4]==game[5][5]==game[4][6]==game[3][7]==game[2][8]==0) or (game[5][5]==game[4][6]==game[3][7]==game[2][8]==game[1][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[9][2]==game[8][3]==game[7][4]==game[6][5]==game[5][6]==0) or (game[8][3]==game[7][4]==game[6][5]==game[5][6]==game[4][7]==0) or (game[7][4]==game[6][5]==game[5][6]==game[4][7]==game[3][8]==0) or (game[6][5]==game[5][6]==game[4][7]==game[3][8]==game[2][9]==0) or (game[9][3]==game[8][4]==game[7][5]==game[6][6]==game[5][7]==0) or (game[8][4]==game[7][5]==game[6][6]==game[5][7]==game[4][8]==0) or (game[7][5]==game[6][6]==game[5][7]==game[4][8]==game[3][9]==0) or (game[9][4]==game[8][5]==game[7][6]==game[6][7]==game[5][8]==0) or (game[8][5]==game[7][6]==game[6][7]==game[5][8]==game[4][9]==0) or (game[9][5]==game[8][6]==game[7][7]==game[6][8]==game[5][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][0]==game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) or (game[1][0]==game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) or (game[2][0]==game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) or (game[3][0]==game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) or (game[4][0]==game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) or (game[5][0]==game[6][0]==game[7][0]==game[8][0]==game[9][0]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][1]==game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) or (game[1][1]==game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) or (game[2][1]==game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) or (game[3][1]==game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) or (game[4][1]==game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) or (game[5][1]==game[6][1]==game[7][1]==game[8][1]==game[9][1]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][2]==game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) or (game[1][2]==game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) or (game[2][2]==game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) or (game[3][2]==game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) or (game[4][2]==game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) or (game[5][2]==game[6][2]==game[7][2]==game[8][2]==game[9][2]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][3]==game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) or (game[1][3]==game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) or (game[2][3]==game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) or (game[3][3]==game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) or (game[4][3]==game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) or (game[5][3]==game[6][3]==game[7][3]==game[8][3]==game[9][3]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][4]==game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) or (game[1][4]==game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) or (game[2][4]==game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) or (game[3][4]==game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) or (game[4][4]==game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) or (game[5][4]==game[6][4]==game[7][4]==game[8][4]==game[9][4]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][5]==game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) or (game[1][5]==game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) or (game[2][5]==game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) or (game[3][5]==game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) or (game[4][5]==game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) or (game[5][5]==game[6][5]==game[7][5]==game[8][5]==game[9][5]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][6]==game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) or (game[1][6]==game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) or (game[2][6]==game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) or (game[3][6]==game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) or (game[4][6]==game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) or (game[5][6]==game[6][6]==game[7][6]==game[8][6]==game[9][6]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][7]==game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) or (game[1][7]==game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) or (game[2][7]==game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) or (game[3][7]==game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) or (game[4][7]==game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) or (game[5][7]==game[6][7]==game[7][7]==game[8][7]==game[9][7]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][8]==game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) or (game[1][8]==game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) or (game[2][8]==game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) or (game[3][8]==game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) or (game[4][8]==game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) or (game[5][8]==game[6][8]==game[7][8]==game[8][8]==game[9][8]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)
        if (game[0][9]==game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) or (game[1][9]==game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) or (game[2][9]==game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) or (game[3][9]==game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) or (game[4][9]==game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) or (game[5][9]==game[6][9]==game[7][9]==game[8][9]==game[9][9]==0):
            game.print("Победа ноликов!!!                                      Ход: ", hod)

    def menu(key):
        if key=="Escape":
            game.close()
        elif key=="F1":
            restart()
        elif key=="F2":
            pass
        elif key=="F3":
            pass

    def mouse_click(button,rows,columns):
        global hod,match_count
        if game[rows][columns]==None:
            game[rows][columns]="x"
        hod += 1
        game.print(menuMSG, "                                        Ход:", hod)
        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") or (game[0][1]==game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") or (game[0][2]==game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") or (game[0][3]==game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") or (game[0][4]==game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") or (game[0][5]==game[0][6]==game[0][7]==game[0][8]==game[0][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[1][0]==game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") or (game[1][1]==game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") or (game[1][2]==game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") or (game[1][3]==game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") or (game[1][4]==game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") or (game[1][5]==game[1][6]==game[1][7]==game[1][8]==game[1][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[2][0]==game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") or (game[2][1]==game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") or (game[2][2]==game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") or (game[2][3]==game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") or (game[2][4]==game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") or (game[2][5]==game[2][6]==game[2][7]==game[2][8]==game[2][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[3][0]==game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") or (game[3][1]==game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") or (game[3][2]==game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") or (game[3][3]==game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") or (game[3][4]==game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") or (game[3][5]==game[3][6]==game[3][7]==game[3][8]==game[3][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[4][0]==game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") or (game[4][1]==game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") or (game[4][2]==game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") or (game[4][3]==game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") or (game[4][4]==game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") or (game[4][5]==game[4][6]==game[4][7]==game[4][8]==game[4][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[5][0]==game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") or (game[5][1]==game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") or (game[5][2]==game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") or (game[5][3]==game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") or (game[5][4]==game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") or (game[5][5]==game[5][6]==game[5][7]==game[5][8]==game[5][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[6][0]==game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") or (game[6][1]==game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") or (game[6][2]==game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") or (game[6][3]==game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") or (game[6][4]==game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") or (game[6][5]==game[6][6]==game[6][7]==game[6][8]==game[6][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[7][0]==game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") or (game[7][1]==game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") or (game[7][2]==game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") or (game[7][3]==game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") or (game[7][4]==game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") or (game[7][5]==game[7][6]==game[7][7]==game[7][8]==game[7][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[8][0]==game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") or (game[8][1]==game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") or (game[8][2]==game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") or (game[8][3]==game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") or (game[8][4]==game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") or (game[8][5]==game[8][6]==game[8][7]==game[8][8]==game[8][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[9][0]==game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") or (game[9][1]==game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") or (game[9][2]==game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") or (game[9][3]==game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") or (game[9][4]==game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") or (game[9][5]==game[9][6]==game[9][7]==game[9][8]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[5][0]==game[6][1]==game[7][2]==game[8][3]==game[9][4]=="x") or (game[4][0]==game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") or (game[5][1]==game[6][2]==game[7][3]==game[8][4]==game[9][5]=="x") or (game[3][0]==game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") or (game[4][1]==game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") or (game[5][2]==game[6][3]==game[7][4]==game[8][5]==game[9][6]=="x") or (game[2][0]==game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") or (game[3][1]==game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") or (game[4][2]==game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") or (game[5][3]==game[6][4]==game[7][5]==game[8][6]==game[9][7]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[1][0]==game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") or (game[2][1]==game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") or (game[3][2]==game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") or (game[4][3]==game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") or (game[5][4]==game[6][5]==game[7][6]==game[8][7]==game[9][8]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][0]==game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") or (game[1][1]==game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") or (game[2][2]==game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") or (game[3][3]==game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") or (game[4][4]==game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") or (game[5][5]==game[6][6]==game[7][7]==game[8][8]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][1]==game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") or (game[1][2]==game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") or (game[2][3]==game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") or (game[3][4]==game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") or (game[4][5]==game[5][6]==game[6][7]==game[7][8]==game[8][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][2]==game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") or (game[1][3]==game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") or (game[2][4]==game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") or (game[3][5]==game[4][6]==game[5][7]==game[6][8]==game[7][9]=="x") or (game[0][3]==game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") or (game[1][4]==game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") or (game[2][5]==game[3][6]==game[4][7]==game[5][8]==game[6][9]=="x") or (game[0][4]==game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") or (game[1][5]==game[2][6]==game[3][7]==game[4][8]==game[5][9]=="x") or (game[0][5]==game[1][6]==game[2][7]==game[3][8]==game[4][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[4][0]==game[3][1]==game[2][2]==game[1][3]==game[0][4]=="x") or (game[5][0]==game[4][1]==game[3][2]==game[2][3]==game[1][4]=="x") or (game[4][1]==game[3][2]==game[2][3]==game[1][4]==game[0][5]=="x") or (game[6][0]==game[5][1]==game[4][2]==game[3][3]==game[2][4]=="x") or (game[5][1]==game[4][2]==game[3][3]==game[2][4]==game[1][5]=="x") or (game[4][2]==game[3][3]==game[2][4]==game[1][5]==game[0][6]=="x") or (game[7][0]==game[6][1]==game[5][2]==game[4][3]==game[3][4]=="x") or (game[6][1]==game[5][2]==game[4][3]==game[3][4]==game[2][5]=="x") or (game[5][2]==game[4][3]==game[3][4]==game[2][5]==game[1][6]=="x") or (game[4][3]==game[3][4]==game[2][5]==game[1][6]==game[0][7]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[8][0]==game[7][1]==game[6][2]==game[5][3]==game[4][4]=="x") or (game[7][1]==game[6][2]==game[5][3]==game[4][4]==game[3][5]=="x") or (game[6][2]==game[5][3]==game[4][4]==game[3][5]==game[2][6]=="x") or (game[5][3]==game[4][4]==game[3][5]==game[2][6]==game[1][7]=="x") or (game[4][4]==game[3][5]==game[2][6]==game[1][7]==game[0][8]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[9][0]==game[8][1]==game[7][2]==game[6][3]==game[5][4]=="x") or (game[8][1]==game[7][2]==game[6][3]==game[5][4]==game[4][5]=="x") or (game[7][2]==game[6][3]==game[5][4]==game[4][5]==game[3][6]=="x") or (game[6][3]==game[5][4]==game[4][5]==game[3][6]==game[2][7]=="x") or (game[5][4]==game[4][5]==game[3][6]==game[2][7]==game[1][8]=="x") or (game[4][5]==game[3][6]==game[2][7]==game[1][8]==game[0][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[9][1]==game[8][2]==game[7][3]==game[6][4]==game[5][5]=="x") or (game[8][2]==game[7][3]==game[6][4]==game[5][5]==game[4][6]=="x") or (game[7][3]==game[6][4]==game[5][5]==game[4][6]==game[3][7]=="x") or (game[6][4]==game[5][5]==game[4][6]==game[3][7]==game[2][8]=="x") or (game[5][5]==game[4][6]==game[3][7]==game[2][8]==game[1][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[9][2]==game[8][3]==game[7][4]==game[6][5]==game[5][6]=="x") or (game[8][3]==game[7][4]==game[6][5]==game[5][6]==game[4][7]=="x") or (game[7][4]==game[6][5]==game[5][6]==game[4][7]==game[3][8]=="x") or (game[6][5]==game[5][6]==game[4][7]==game[3][8]==game[2][9]=="x") or (game[9][3]==game[8][4]==game[7][5]==game[6][6]==game[5][7]=="x") or (game[8][4]==game[7][5]==game[6][6]==game[5][7]==game[4][8]=="x") or (game[7][5]==game[6][6]==game[5][7]==game[4][8]==game[3][9]=="x") or (game[9][4]==game[8][5]==game[7][6]==game[6][7]==game[5][8]=="x") or (game[8][5]==game[7][6]==game[6][7]==game[5][8]==game[4][9]=="x") or (game[9][5]==game[8][6]==game[7][7]==game[6][8]==game[5][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][0]==game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") or (game[1][0]==game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") or (game[2][0]==game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") or (game[3][0]==game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") or (game[4][0]==game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") or (game[5][0]==game[6][0]==game[7][0]==game[8][0]==game[9][0]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][1]==game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") or (game[1][1]==game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") or (game[2][1]==game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") or (game[3][1]==game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") or (game[4][1]==game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") or (game[5][1]==game[6][1]==game[7][1]==game[8][1]==game[9][1]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][2]==game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") or (game[1][2]==game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") or (game[2][2]==game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") or (game[3][2]==game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") or (game[4][2]==game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") or (game[5][2]==game[6][2]==game[7][2]==game[8][2]==game[9][2]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][3]==game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") or (game[1][3]==game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") or (game[2][3]==game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") or (game[3][3]==game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") or (game[4][3]==game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") or (game[5][3]==game[6][3]==game[7][3]==game[8][3]==game[9][3]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][4]==game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") or (game[1][4]==game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") or (game[2][4]==game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") or (game[3][4]==game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") or (game[4][4]==game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") or (game[5][4]==game[6][4]==game[7][4]==game[8][4]==game[9][4]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][5]==game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") or (game[1][5]==game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") or (game[2][5]==game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") or (game[3][5]==game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") or (game[4][5]==game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") or (game[5][5]==game[6][5]==game[7][5]==game[8][5]==game[9][5]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][6]==game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") or (game[1][6]==game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") or (game[2][6]==game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") or (game[3][6]==game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") or (game[4][6]==game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") or (game[5][6]==game[6][6]==game[7][6]==game[8][6]==game[9][6]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][7]==game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") or (game[1][7]==game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") or (game[2][7]==game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") or (game[3][7]==game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") or (game[4][7]==game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") or (game[5][7]==game[6][7]==game[7][7]==game[8][7]==game[9][7]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][8]==game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") or (game[1][8]==game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") or (game[2][8]==game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") or (game[3][8]==game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") or (game[4][8]==game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") or (game[5][8]==game[6][8]==game[7][8]==game[8][8]==game[9][8]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        if (game[0][9]==game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") or (game[1][9]==game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") or (game[2][9]==game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") or (game[3][9]==game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") or (game[4][9]==game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") or (game[5][9]==game[6][9]==game[7][9]==game[8][9]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                        Ход: ", hod)
        botZero()
        if hod>100:
            game.print("Ничья!!!                                               Ход: ", hod)

    def restart():
        global previous_row,previous_col,hod,match_count
        previous_row=previous_col=hod=0
        game.clear()
        match_count+=1
        game.print(menuMSG, "Матч: ", match_count)

    game=Board(10, 10)
    game.title="Gomoku"
    game.cell_size=50
    game.cell_color="lightblue"
    game.create_output(background_color="wheat4", color="white")
    game.on_mouse_click=mouse_click
    game.on_key_press = menu
    game.print(menuMSG)
    game.show()
if (variant=="0"):
    previous_row=previous_col=hod=0
    match_count=1
    menuMSG="ESC: Закрыть игру; F1: Начать сначала."

    def botZero():
        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[0][6]==game[0][7]==game[0][8]==game[0][9]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][0]==game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[1][6]==game[1][7]==game[1][8]==game[1][9]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][0]==game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][9]==None):
            game[2][9]="x"
        elif (game[2][6]==game[2][7]==game[2][8]==game[2][9]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][0]==game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[3][6]==game[3][7]==game[3][8]==game[3][9]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][0]==game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[4][6]==game[4][7]==game[4][8]==game[4][9]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][0]==game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[5][6]==game[5][7]==game[5][8]==game[5][9]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][0]==game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[6][6]==game[6][7]==game[6][8]==game[6][9]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[7][0]==game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[7][6]==game[7][7]==game[7][8]==game[7][9]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[8][0]==game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[8][6]==game[8][7]==game[8][8]==game[8][9]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[9][0]==game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[9][6]==game[9][7]==game[9][8]==game[9][9]=="x") and (game[9][5]==None):
            game[9][5]="x"


        elif (game[0][0]==game[1][0]==game[2][0]==game[3][0]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]==game[9][0]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[0][1]==game[1][1]==game[2][1]==game[3][1]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]==game[9][1]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[0][2]==game[1][2]==game[2][2]==game[3][2]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]==game[9][2]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[0][3]==game[1][3]==game[2][3]==game[3][3]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]==game[9][3]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[0][4]==game[1][4]==game[2][4]==game[3][4]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]==game[9][4]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[0][5]==game[1][5]==game[2][5]==game[3][5]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]==game[9][5]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[0][6]==game[1][6]==game[2][6]==game[3][6]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]==game[9][6]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[0][7]==game[1][7]==game[2][7]==game[3][7]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]==game[9][7]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[0][8]==game[1][8]==game[2][8]==game[3][8]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]==game[9][8]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[0][9]==game[1][9]==game[2][9]==game[3][9]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]==game[9][9]=="x") and (game[5][9]==None):
            game[5][9]="x"


        elif (game[5][0]==game[6][1]==game[7][2]==game[8][3]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[6][1]==game[7][2]==game[8][3]==game[9][4]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[4][0]==game[5][1]==game[6][2]==game[7][3]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][2]==game[7][3]==game[8][4]==game[9][5]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][0]==game[4][1]==game[5][2]==game[6][3]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[6][3]==game[7][4]==game[8][5]==game[9][6]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][0]==game[3][1]==game[4][2]==game[5][3]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[6][4]==game[7][5]==game[8][6]==game[9][7]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[1][0]==game[2][1]==game[3][2]==game[4][3]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[6][5]==game[7][6]==game[8][7]==game[9][8]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[0][0]==game[1][1]==game[2][2]==game[3][3]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[6][6]==game[7][7]==game[8][8]==game[9][9]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[0][1]==game[1][2]==game[2][3]==game[3][4]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[5][6]==game[6][7]==game[7][8]==game[8][9]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[0][2]==game[1][3]==game[2][4]==game[3][5]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[4][6]==game[5][7]==game[6][8]==game[7][9]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[0][3]==game[1][4]==game[2][5]==game[3][6]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[3][6]==game[4][7]==game[5][8]==game[6][9]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[0][4]==game[1][5]==game[2][6]==game[3][7]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[2][6]==game[3][7]==game[4][8]==game[5][9]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[0][5]==game[1][6]==game[2][7]==game[3][8]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[1][6]==game[2][7]==game[3][8]==game[4][9]=="x") and (game[0][5]==None):
            game[0][5]="x"


        elif (game[0][4]==game[1][3]==game[2][2]==game[3][1]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[1][3]==game[2][2]==game[3][1]==game[4][0]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[1][4]==game[2][3]==game[3][2]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[2][3]==game[3][2]==game[4][1]==game[5][0]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[0][6]==game[1][5]==game[2][4]==game[3][3]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[3][3]==game[4][2]==game[5][1]==game[6][0]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[0][7]==game[1][6]==game[2][5]==game[3][4]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[4][3]==game[5][2]==game[6][1]==game[7][0]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[0][8]==game[1][7]==game[2][6]==game[3][5]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[5][3]==game[6][2]==game[7][1]==game[8][0]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[0][9]==game[1][8]==game[2][7]==game[3][6]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[6][3]==game[7][2]==game[8][1]==game[9][0]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[1][9]==game[2][8]==game[3][7]==game[4][6]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[6][4]==game[7][3]==game[8][2]==game[9][1]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][9]==game[3][8]==game[4][7]==game[5][6]=="x") and (game[6][5]==None):
            game[5][5]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]=="x") and (game[2][9]==None):
            game[1][9]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]=="x") and (game[7][4]==None):
            game[6][4]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[6][5]==game[7][4]==game[8][3]==game[9][2]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][9]==game[4][8]==game[5][7]==game[6][6]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]=="x") and (game[8][4]==None):
            game[7][4]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[6][6]==game[7][5]==game[8][4]==game[9][3]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[4][9]==game[5][8]==game[6][7]==game[7][6]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]=="x") and (game[9][4]==None):
            game[8][4]="x"
        elif (game[6][7]==game[7][6]==game[8][5]==game[9][4]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][9]==game[6][8]==game[7][7]==game[8][6]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][8]==game[7][7]==game[8][6]==game[9][5]=="x") and (game[5][9]==None):
            game[5][9]="x"



        elif (game[0][0]==game[0][1]==game[0][2]==game[0][3]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[0][6]==game[0][7]==game[0][8]==game[0][9]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][0]==game[1][1]==game[1][2]==game[1][3]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[1][6]==game[1][7]==game[1][8]==game[1][9]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][0]==game[2][1]==game[2][2]==game[2][3]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[2][6]==game[2][7]==game[2][8]==game[2][9]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][0]==game[3][1]==game[3][2]==game[3][3]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[3][6]==game[3][7]==game[3][8]==game[3][9]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][0]==game[4][1]==game[4][2]==game[4][3]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[4][6]==game[4][7]==game[4][8]==game[4][9]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][0]==game[5][1]==game[5][2]==game[5][3]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[5][6]==game[5][7]==game[5][8]==game[5][9]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][0]==game[6][1]==game[6][2]==game[6][3]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[6][6]==game[6][7]==game[6][8]==game[6][9]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[7][0]==game[7][1]==game[7][2]==game[7][3]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[7][6]==game[7][7]==game[7][8]==game[7][9]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[8][0]==game[8][1]==game[8][2]==game[8][3]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[8][6]==game[8][7]==game[8][8]==game[8][9]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[9][0]==game[9][1]==game[9][2]==game[9][3]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[9][6]==game[9][7]==game[9][8]==game[9][9]==0) and (game[9][5]==None):
            game[9][5]="x"


        elif (game[0][0]==game[1][0]==game[2][0]==game[3][0]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]==game[9][0]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[0][1]==game[1][1]==game[2][1]==game[3][1]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]==game[9][1]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[0][2]==game[1][2]==game[2][2]==game[3][2]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]==game[9][2]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[0][3]==game[1][3]==game[2][3]==game[3][3]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]==game[9][3]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[0][4]==game[1][4]==game[2][4]==game[3][4]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]==game[9][4]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[0][5]==game[1][5]==game[2][5]==game[3][5]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]==game[9][5]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[0][6]==game[1][6]==game[2][6]==game[3][6]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]==game[9][6]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[0][7]==game[1][7]==game[2][7]==game[3][7]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]==game[9][7]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[0][8]==game[1][8]==game[2][8]==game[3][8]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]==game[9][8]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[0][9]==game[1][9]==game[2][9]==game[3][9]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]==game[9][9]==0) and (game[5][9]==None):
            game[5][9]="x"


        elif (game[5][0]==game[6][1]==game[7][2]==game[8][3]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[6][1]==game[7][2]==game[8][3]==game[9][4]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[4][0]==game[5][1]==game[6][2]==game[7][3]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][2]==game[7][3]==game[8][4]==game[9][5]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][0]==game[4][1]==game[5][2]==game[6][3]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[6][3]==game[7][4]==game[8][5]==game[9][6]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][0]==game[3][1]==game[4][2]==game[5][3]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[6][4]==game[7][5]==game[8][6]==game[9][7]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[1][0]==game[2][1]==game[3][2]==game[4][3]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[6][5]==game[7][6]==game[8][7]==game[9][8]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[0][0]==game[1][1]==game[2][2]==game[3][3]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[6][6]==game[7][7]==game[8][8]==game[9][9]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[0][1]==game[1][2]==game[2][3]==game[3][4]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[5][6]==game[6][7]==game[7][8]==game[8][9]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[0][2]==game[1][3]==game[2][4]==game[3][5]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[4][6]==game[5][7]==game[6][8]==game[7][9]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[0][3]==game[1][4]==game[2][5]==game[3][6]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[3][6]==game[4][7]==game[5][8]==game[6][9]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[0][4]==game[1][5]==game[2][6]==game[3][7]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[2][6]==game[3][7]==game[4][8]==game[5][9]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[0][5]==game[1][6]==game[2][7]==game[3][8]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[1][6]==game[2][7]==game[3][8]==game[4][9]==0) and (game[0][5]==None):
            game[0][5]="x"


        elif (game[0][4]==game[1][3]==game[2][2]==game[3][1]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[1][3]==game[2][2]==game[3][1]==game[4][0]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[1][4]==game[2][3]==game[3][2]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==game[4][1]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[2][3]==game[3][2]==game[4][1]==game[5][0]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[0][6]==game[1][5]==game[2][4]==game[3][3]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==game[4][2]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==game[5][1]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[3][3]==game[4][2]==game[5][1]==game[6][0]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[0][7]==game[1][6]==game[2][5]==game[3][4]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==game[4][3]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==game[5][2]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==game[6][1]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[4][3]==game[5][2]==game[6][1]==game[7][0]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[0][8]==game[1][7]==game[2][6]==game[3][5]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==game[4][4]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==game[5][3]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==game[6][2]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==game[7][1]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[5][3]==game[6][2]==game[7][1]==game[8][0]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[0][9]==game[1][8]==game[2][7]==game[3][6]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==game[4][5]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==game[5][4]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==game[6][3]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==game[7][2]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==game[8][1]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[6][3]==game[7][2]==game[8][1]==game[9][0]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[1][9]==game[2][8]==game[3][7]==game[4][6]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==game[5][5]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==game[6][4]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==game[7][3]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==game[8][2]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[6][4]==game[7][3]==game[8][2]==game[9][1]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[2][9]==game[3][8]==game[4][7]==game[5][6]==0) and (game[6][5]==None):
            game[5][5]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]==0) and (game[2][9]==None):
            game[1][9]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==game[6][5]==0) and (game[7][4]==None):
            game[6][4]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==game[7][4]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==game[8][3]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[6][5]==game[7][4]==game[8][3]==game[9][2]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][9]==game[4][8]==game[5][7]==game[6][6]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==game[7][5]==0) and (game[8][4]==None):
            game[7][4]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==game[8][4]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[6][6]==game[7][5]==game[8][4]==game[9][3]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[4][9]==game[5][8]==game[6][7]==game[7][6]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==game[8][5]==0) and (game[9][4]==None):
            game[8][4]="x"
        elif (game[6][7]==game[7][6]==game[8][5]==game[9][4]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][9]==game[6][8]==game[7][7]==game[8][6]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[6][8]==game[7][7]==game[8][6]==game[9][5]==0) and (game[5][9]==None):
            game[5][9]="x"




        elif (game[0][0]==game[0][1]==game[0][2]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[0][1]==game[0][2]==game[0][3]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[0][2]==game[0][3]==game[0][4]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[0][3]==game[0][4]==game[0][5]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][4]==game[0][5]==game[0][6]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[0][6]==game[0][7]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][6]==game[0][7]==game[0][8]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[0][7]==game[0][8]==game[0][9]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][0]==game[1][1]==game[1][2]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[1][1]==game[1][2]==game[1][3]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[1][2]==game[1][3]==game[1][4]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[1][3]==game[1][4]==game[1][5]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][4]==game[1][5]==game[1][6]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][5]==game[1][6]==game[1][7]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][6]==game[1][7]==game[1][8]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[1][7]==game[1][8]==game[1][9]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][0]==game[2][1]==game[2][2]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[2][1]==game[2][2]==game[2][3]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[2][2]==game[2][3]==game[2][4]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[2][3]==game[2][4]==game[2][5]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][4]==game[2][5]==game[2][6]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][5]==game[2][6]==game[2][7]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][6]==game[2][7]==game[2][8]=="x") and (game[2][9]==None):
            game[2][9]="x"
        elif (game[2][7]==game[2][8]==game[2][9]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][0]==game[3][1]==game[3][2]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[3][1]==game[3][2]==game[3][3]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[3][2]==game[3][3]==game[3][4]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[3][3]==game[3][4]==game[3][5]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][4]==game[3][5]==game[3][6]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][5]==game[3][6]==game[3][7]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][6]==game[3][7]==game[3][8]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[3][7]==game[3][8]==game[3][9]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][0]==game[4][1]==game[4][2]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[4][1]==game[4][2]==game[4][3]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[4][2]==game[4][3]==game[4][4]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[4][3]==game[4][4]==game[4][5]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][4]==game[4][5]==game[4][6]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][5]==game[4][6]==game[4][7]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][6]==game[4][7]==game[4][8]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[4][7]==game[4][8]==game[4][9]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][0]==game[5][1]==game[5][2]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[5][1]==game[5][2]==game[5][3]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[5][2]==game[5][3]==game[5][4]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[5][3]==game[5][4]==game[5][5]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][4]==game[5][5]==game[5][6]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][5]==game[5][6]==game[5][7]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][6]==game[5][7]==game[5][8]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[5][7]==game[5][8]==game[5][9]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][0]==game[6][1]==game[6][2]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[6][1]==game[6][2]==game[6][3]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[6][2]==game[6][3]==game[6][4]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[6][3]==game[6][4]==game[6][5]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][4]==game[6][5]==game[6][6]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][5]==game[6][6]==game[6][7]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][6]==game[6][7]==game[6][8]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[6][7]==game[6][8]==game[6][9]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[7][0]==game[7][1]==game[7][2]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[7][1]==game[7][2]==game[7][3]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[7][2]==game[7][3]==game[7][4]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[7][3]==game[7][4]==game[7][5]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][4]==game[7][5]==game[7][6]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][5]==game[7][6]==game[7][7]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][6]==game[7][7]==game[7][8]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[7][7]==game[7][8]==game[7][9]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[8][0]==game[8][1]==game[8][2]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[8][1]==game[8][2]==game[8][3]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[8][2]==game[8][3]==game[8][4]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[8][3]==game[8][4]==game[8][5]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][4]==game[8][5]==game[8][6]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][5]==game[8][6]==game[8][7]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][6]==game[8][7]==game[8][8]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[8][7]==game[8][8]==game[8][9]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[9][0]==game[9][1]==game[9][2]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[9][1]==game[9][2]==game[9][3]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[9][2]==game[9][3]==game[9][4]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[9][3]==game[9][4]==game[9][5]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][4]==game[9][5]==game[9][6]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][5]==game[9][6]==game[9][7]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][6]==game[9][7]==game[9][8]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[9][7]==game[9][8]==game[9][9]=="x") and (game[9][6]==None):
            game[9][6]="x"


        elif (game[0][0]==game[1][0]==game[2][0]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[7][0]==game[8][0]==game[9][0]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[0][1]==game[1][1]==game[2][1]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[7][1]==game[8][1]==game[9][1]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[0][2]==game[1][2]==game[2][2]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[7][2]==game[8][2]==game[9][2]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[0][3]==game[1][3]==game[2][3]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[7][3]==game[8][3]==game[9][3]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[0][4]==game[1][4]==game[2][4]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[7][4]==game[8][4]==game[9][4]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[0][5]==game[1][5]==game[2][5]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[7][5]==game[8][5]==game[9][5]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[0][6]==game[1][6]==game[2][6]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[7][6]==game[8][6]==game[9][6]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[0][7]==game[1][7]==game[2][7]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[7][7]==game[8][7]==game[9][7]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[0][8]==game[1][8]==game[2][8]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[7][8]==game[8][8]==game[9][8]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[0][9]==game[1][9]==game[2][9]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]=="x") and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[7][9]==game[8][9]==game[9][9]=="x") and (game[6][9]==None):
            game[6][9]="x"


        elif (game[4][0]==game[5][1]==game[6][2]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][1]==game[6][2]==game[7][3]=="x") and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][1]==game[6][2]==game[7][3]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][2]==game[7][3]==game[8][4]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[6][2]==game[7][3]==game[8][4]=="x") and (game[9][5]==None):
            game[9][5]="x"
        elif (game[7][3]==game[8][4]==game[9][5]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][0]==game[4][1]==game[5][2]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][1]==game[5][2]==game[6][3]=="x") and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][1]==game[5][2]==game[6][3]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][2]==game[6][3]==game[7][4]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][2]==game[6][3]==game[7][4]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][3]==game[7][4]==game[8][5]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[6][3]==game[7][4]==game[8][5]=="x") and (game[9][6]==None):
            game[9][6]="x"
        elif (game[7][4]==game[8][5]==game[9][6]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[2][0]==game[3][1]==game[4][2]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][1]==game[4][2]==game[5][3]=="x") and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][1]==game[4][2]==game[5][3]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][2]==game[5][3]==game[6][4]=="x") and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][2]==game[5][3]==game[6][4]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][3]==game[6][4]==game[7][5]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][3]==game[6][4]==game[7][5]=="x") and (game[8][6]==None):
            game[8][6]="x"
        elif (game[6][4]==game[7][5]==game[8][6]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[6][4]==game[7][5]==game[8][6]=="x") and (game[9][7]==None):
            game[9][7]="x"
        elif (game[7][5]==game[8][6]==game[9][7]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[1][0]==game[2][1]==game[3][2]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][1]==game[3][2]==game[4][3]=="x") and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][1]==game[3][2]==game[4][3]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][2]==game[4][3]==game[5][4]=="x") and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][2]==game[4][3]==game[5][4]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][3]==game[5][4]==game[6][5]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][3]==game[5][4]==game[6][5]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][4]==game[6][5]==game[7][6]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][4]==game[6][5]==game[7][6]=="x") and (game[8][7]==None):
            game[8][7]="x"
        elif (game[6][5]==game[7][6]==game[8][7]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][5]==game[7][6]==game[8][7]=="x") and (game[9][8]==None):
            game[9][8]="x"
        elif (game[7][6]==game[8][7]==game[9][8]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[0][0]==game[1][1]==game[2][2]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][1]==game[2][2]==game[3][3]=="x") and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][1]==game[2][2]==game[3][3]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][2]==game[3][3]==game[4][4]=="x") and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][2]==game[3][3]==game[4][4]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][3]==game[4][4]==game[5][5]=="x") and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][3]==game[4][4]==game[5][5]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][4]==game[5][5]==game[6][6]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][4]==game[5][5]==game[6][6]=="x") and (game[7][7]==None):
            game[7][7]="x"
        elif (game[5][5]==game[6][6]==game[7][7]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][5]==game[6][6]==game[7][7]=="x") and (game[8][8]==None):
            game[8][8]="x"
        elif (game[6][6]==game[7][7]==game[8][8]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][6]==game[7][7]==game[8][8]=="x") and (game[9][9]==None):
            game[9][9]="x"
        elif (game[7][7]==game[8][8]==game[9][9]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[0][1]==game[1][2]==game[2][3]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][2]==game[2][3]==game[3][4]=="x") and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][2]==game[2][3]==game[3][4]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][3]==game[3][4]==game[4][5]=="x") and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][3]==game[3][4]==game[4][5]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][4]==game[4][5]==game[5][6]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][4]==game[4][5]==game[5][6]=="x") and (game[6][7]==None):
            game[6][7]="x"
        elif (game[4][5]==game[5][6]==game[6][7]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][5]==game[5][6]==game[6][7]=="x") and (game[7][8]==None):
            game[7][8]="x"
        elif (game[5][6]==game[6][7]==game[7][8]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][6]==game[6][7]==game[7][8]=="x") and (game[8][9]==None):
            game[8][9]="x"
        elif (game[6][7]==game[7][8]==game[8][9]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[0][2]==game[1][3]==game[2][4]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][3]==game[2][4]==game[3][5]=="x") and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][3]==game[2][4]==game[3][5]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][4]==game[3][5]==game[4][6]=="x") and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][4]==game[3][5]==game[4][6]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[3][5]==game[4][6]==game[5][7]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][5]==game[4][6]==game[5][7]=="x") and (game[6][8]==None):
            game[6][8]="x"
        elif (game[4][6]==game[5][7]==game[6][8]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][6]==game[5][7]==game[6][8]=="x") and (game[7][9]==None):
            game[7][9]="x"
        elif (game[5][7]==game[6][8]==game[7][9]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[0][3]==game[1][4]==game[2][5]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][4]==game[2][5]==game[3][6]=="x") and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][4]==game[2][5]==game[3][6]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[2][5]==game[3][6]==game[4][7]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][5]==game[3][6]==game[4][7]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[3][6]==game[4][7]==game[5][8]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][6]==game[4][7]==game[5][8]=="x") and (game[6][9]==None):
            game[6][9]="x"
        elif (game[4][7]==game[5][8]==game[6][9]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[0][4]==game[1][5]==game[2][6]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[1][5]==game[2][6]==game[3][7]=="x") and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][5]==game[2][6]==game[3][7]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[2][6]==game[3][7]==game[4][8]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][6]==game[3][7]==game[4][8]=="x") and (game[5][9]==None):
            game[5][9]="x"
        elif (game[3][7]==game[4][8]==game[5][9]=="x") and (game[2][6]==None):
            game[2][6]="x"


        elif (game[0][5]==game[1][4]==game[2][3]=="x") and (game[3][2]==None):
            game[3][2]="x"
        elif (game[1][4]==game[2][3]==game[3][2]=="x") and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][4]==game[2][3]==game[3][2]=="x") and (game[4][1]==None):
            game[4][1]="x"
        elif (game[2][3]==game[3][2]==game[4][1]=="x") and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][3]==game[3][2]==game[4][1]=="x") and (game[5][0]==None):
            game[5][0]="x"
        elif (game[3][2]==game[4][1]==game[5][0]=="x") and (game[2][3]==None):
            game[2][3]="x"
        elif (game[0][6]==game[1][5]==game[2][4]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][5]==game[2][4]==game[3][3]=="x") and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][5]==game[2][4]==game[3][3]=="x") and (game[4][2]==None):
            game[4][2]="x"
        elif (game[2][4]==game[3][3]==game[4][2]=="x") and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][4]==game[3][3]==game[4][2]=="x") and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][3]==game[4][2]==game[5][1]=="x") and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][3]==game[4][2]==game[5][1]=="x") and (game[6][0]==None):
            game[6][0]="x"
        elif (game[4][2]==game[5][1]==game[6][0]=="x") and (game[3][3]==None):
            game[3][3]="x"
        elif (game[0][7]==game[1][6]==game[2][5]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][6]==game[2][5]==game[3][4]=="x") and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][6]==game[2][5]==game[3][4]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][5]==game[3][4]==game[4][3]=="x") and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][5]==game[3][4]==game[4][3]=="x") and (game[5][2]==None):
            game[5][2]="x"
        elif (game[3][4]==game[4][3]==game[5][2]=="x") and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][4]==game[4][3]==game[5][2]=="x") and (game[6][1]==None):
            game[6][1]="x"
        elif (game[4][3]==game[5][2]==game[6][1]=="x") and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][3]==game[5][2]==game[6][1]=="x") and (game[7][0]==None):
            game[7][0]="x"
        elif (game[5][2]==game[6][1]==game[7][0]=="x") and (game[4][3]==None):
            game[4][3]="x"
        elif (game[0][8]==game[1][7]==game[2][6]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][7]==game[2][6]==game[3][5]=="x") and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][7]==game[2][6]==game[3][5]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][6]==game[3][5]==game[4][4]=="x") and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][6]==game[3][5]==game[4][4]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][5]==game[4][4]==game[5][3]=="x") and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][5]==game[4][4]==game[5][3]=="x") and (game[6][2]==None):
            game[6][2]="x"
        elif (game[4][4]==game[5][3]==game[6][2]=="x") and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][4]==game[5][3]==game[6][2]=="x") and (game[7][1]==None):
            game[7][1]="x"
        elif (game[5][3]==game[6][2]==game[7][1]=="x") and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][3]==game[6][2]==game[7][1]=="x") and (game[8][0]==None):
            game[8][0]="x"
        elif (game[6][2]==game[7][1]==game[8][0]=="x") and (game[5][3]==None):
            game[5][3]="x"
        elif (game[0][9]==game[1][8]==game[2][7]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][8]==game[2][7]==game[3][6]=="x") and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][8]==game[2][7]==game[3][6]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][7]==game[3][6]==game[4][5]=="x") and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][7]==game[3][6]==game[4][5]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][6]==game[4][5]==game[5][4]=="x") and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][6]==game[4][5]==game[5][4]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][5]==game[5][4]==game[6][3]=="x") and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][5]==game[5][4]==game[6][3]=="x") and (game[7][2]==None):
            game[7][2]="x"
        elif (game[5][4]==game[6][3]==game[7][2]=="x") and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][4]==game[6][3]==game[7][2]=="x") and (game[8][1]==None):
            game[8][1]="x"
        elif (game[6][3]==game[7][2]==game[8][1]=="x") and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][3]==game[7][2]==game[8][1]=="x") and (game[9][0]==None):
            game[9][0]="x"
        elif (game[7][2]==game[8][1]==game[9][0]=="x") and (game[6][3]==None):
            game[6][3]="x"
        elif (game[1][9]==game[2][8]==game[3][7]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][8]==game[3][7]==game[4][6]=="x") and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][8]==game[3][7]==game[4][6]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][7]==game[4][6]==game[5][5]=="x") and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][7]==game[4][6]==game[5][5]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][6]==game[5][5]==game[6][4]=="x") and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][6]==game[5][5]==game[6][4]=="x") and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][5]==game[6][4]==game[7][3]=="x") and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][5]==game[6][4]==game[7][3]=="x") and (game[8][2]==None):
            game[8][2]="x"
        elif (game[6][4]==game[7][3]==game[8][2]=="x") and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][4]==game[7][3]==game[8][2]=="x") and (game[9][1]==None):
            game[9][1]="x"
        elif (game[7][3]==game[8][2]==game[9][1]=="x") and (game[6][4]==None):
            game[6][4]="x"
        elif (game[2][9]==game[3][8]==game[4][7]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][8]==game[4][7]==game[5][6]=="x") and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][8]==game[4][7]==game[5][6]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][7]==game[5][6]==game[6][5]=="x") and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][7]==game[5][6]==game[6][5]=="x") and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][6]==game[6][5]==game[7][4]=="x") and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][6]==game[6][5]==game[7][4]=="x") and (game[8][3]==None):
            game[8][3]="x"
        elif (game[6][5]==game[7][4]==game[8][3]=="x") and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][5]==game[7][4]==game[8][3]=="x") and (game[9][2]==None):
            game[9][2]="x"
        elif (game[7][4]==game[8][3]==game[9][2]=="x") and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][9]==game[4][8]==game[5][7]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][8]==game[5][7]==game[6][6]=="x") and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][8]==game[5][7]==game[6][6]=="x") and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][7]==game[6][6]==game[7][5]=="x") and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][7]==game[6][6]==game[7][5]=="x") and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][6]==game[7][5]==game[8][4]=="x") and (game[5][7]==None):
            game[5][7]="x"
        elif (game[6][6]==game[7][5]==game[8][4]=="x") and (game[9][3]==None):
            game[9][3]="x"
        elif (game[7][5]==game[8][4]==game[9][3]=="x") and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][9]==game[5][8]==game[6][7]=="x") and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][8]==game[6][7]==game[7][6]=="x") and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][8]==game[6][7]==game[7][6]=="x") and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][7]==game[7][6]==game[8][5]=="x") and (game[5][8]==None):
            game[5][8]="x"
        elif (game[6][7]==game[7][6]==game[8][5]=="x") and (game[9][4]==None):
            game[9][4]="x"
        elif (game[7][6]==game[8][5]==game[9][4]=="x") and (game[6][7]==None):
            game[6][7]="x"



        elif (game[0][0]==game[0][1]==game[0][2]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[0][1]==game[0][2]==game[0][3]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[0][2]==game[0][3]==game[0][4]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[0][3]==game[0][4]==game[0][5]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][4]==game[0][5]==game[0][6]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][5]==game[0][6]==game[0][7]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[0][6]==game[0][7]==game[0][8]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][6]==game[0][7]==game[0][8]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[0][7]==game[0][8]==game[0][9]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][0]==game[1][1]==game[1][2]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[1][1]==game[1][2]==game[1][3]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[1][2]==game[1][3]==game[1][4]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[1][3]==game[1][4]==game[1][5]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][4]==game[1][5]==game[1][6]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][5]==game[1][6]==game[1][7]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[1][6]==game[1][7]==game[1][8]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][6]==game[1][7]==game[1][8]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[1][7]==game[1][8]==game[1][9]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][0]==game[2][1]==game[2][2]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[2][1]==game[2][2]==game[2][3]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[2][2]==game[2][3]==game[2][4]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[2][3]==game[2][4]==game[2][5]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][4]==game[2][5]==game[2][6]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][5]==game[2][6]==game[2][7]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[2][6]==game[2][7]==game[2][8]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][6]==game[2][7]==game[2][8]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[2][7]==game[2][8]==game[2][9]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][0]==game[3][1]==game[3][2]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[3][1]==game[3][2]==game[3][3]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[3][2]==game[3][3]==game[3][4]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[3][3]==game[3][4]==game[3][5]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][4]==game[3][5]==game[3][6]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][5]==game[3][6]==game[3][7]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[3][6]==game[3][7]==game[3][8]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][6]==game[3][7]==game[3][8]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[3][7]==game[3][8]==game[3][9]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][0]==game[4][1]==game[4][2]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[4][1]==game[4][2]==game[4][3]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[4][2]==game[4][3]==game[4][4]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[4][3]==game[4][4]==game[4][5]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][4]==game[4][5]==game[4][6]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][5]==game[4][6]==game[4][7]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[4][6]==game[4][7]==game[4][8]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][6]==game[4][7]==game[4][8]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[4][7]==game[4][8]==game[4][9]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][0]==game[5][1]==game[5][2]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[5][1]==game[5][2]==game[5][3]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[5][2]==game[5][3]==game[5][4]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[5][3]==game[5][4]==game[5][5]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][4]==game[5][5]==game[5][6]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][5]==game[5][6]==game[5][7]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][6]==game[5][7]==game[5][8]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][6]==game[5][7]==game[5][8]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[5][7]==game[5][8]==game[5][9]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][0]==game[6][1]==game[6][2]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[6][1]==game[6][2]==game[6][3]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[6][2]==game[6][3]==game[6][4]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[6][3]==game[6][4]==game[6][5]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][4]==game[6][5]==game[6][6]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][5]==game[6][6]==game[6][7]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[6][6]==game[6][7]==game[6][8]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][6]==game[6][7]==game[6][8]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[6][7]==game[6][8]==game[6][9]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[7][0]==game[7][1]==game[7][2]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[7][1]==game[7][2]==game[7][3]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[7][2]==game[7][3]==game[7][4]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[7][3]==game[7][4]==game[7][5]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][4]==game[7][5]==game[7][6]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][5]==game[7][6]==game[7][7]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[7][6]==game[7][7]==game[7][8]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][6]==game[7][7]==game[7][8]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[7][7]==game[7][8]==game[7][9]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[8][0]==game[8][1]==game[8][2]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[8][1]==game[8][2]==game[8][3]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[8][2]==game[8][3]==game[8][4]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[8][3]==game[8][4]==game[8][5]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][4]==game[8][5]==game[8][6]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][5]==game[8][6]==game[8][7]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[8][6]==game[8][7]==game[8][8]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][6]==game[8][7]==game[8][8]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[8][7]==game[8][8]==game[8][9]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[9][0]==game[9][1]==game[9][2]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[9][1]==game[9][2]==game[9][3]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[9][2]==game[9][3]==game[9][4]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[9][3]==game[9][4]==game[9][5]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][4]==game[9][5]==game[9][6]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][5]==game[9][6]==game[9][7]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[9][6]==game[9][7]==game[9][8]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][6]==game[9][7]==game[9][8]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[9][7]==game[9][8]==game[9][9]==0) and (game[9][6]==None):
            game[9][6]="x"


        elif (game[0][0]==game[1][0]==game[2][0]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][0]==game[2][0]==game[3][0]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][0]==game[3][0]==game[4][0]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][0]==game[4][0]==game[5][0]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][0]==game[5][0]==game[6][0]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][0]==game[6][0]==game[7][0]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[6][0]==game[7][0]==game[8][0]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[7][0]==game[8][0]==game[9][0]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[0][1]==game[1][1]==game[2][1]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][1]==game[2][1]==game[3][1]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][1]==game[3][1]==game[4][1]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][1]==game[4][1]==game[5][1]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][1]==game[5][1]==game[6][1]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][1]==game[6][1]==game[7][1]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[6][1]==game[7][1]==game[8][1]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[7][1]==game[8][1]==game[9][1]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[0][2]==game[1][2]==game[2][2]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][2]==game[2][2]==game[3][2]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][2]==game[3][2]==game[4][2]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][2]==game[4][2]==game[5][2]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][2]==game[5][2]==game[6][2]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][2]==game[6][2]==game[7][2]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[6][2]==game[7][2]==game[8][2]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[7][2]==game[8][2]==game[9][2]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[0][3]==game[1][3]==game[2][3]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][3]==game[2][3]==game[3][3]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][3]==game[3][3]==game[4][3]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][3]==game[4][3]==game[5][3]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][3]==game[5][3]==game[6][3]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][3]==game[6][3]==game[7][3]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[6][3]==game[7][3]==game[8][3]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[7][3]==game[8][3]==game[9][3]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[0][4]==game[1][4]==game[2][4]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][4]==game[2][4]==game[3][4]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][4]==game[3][4]==game[4][4]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][4]==game[4][4]==game[5][4]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][4]==game[5][4]==game[6][4]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][4]==game[6][4]==game[7][4]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][4]==game[7][4]==game[8][4]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[7][4]==game[8][4]==game[9][4]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[0][5]==game[1][5]==game[2][5]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][5]==game[2][5]==game[3][5]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][5]==game[3][5]==game[4][5]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][5]==game[4][5]==game[5][5]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][5]==game[5][5]==game[6][5]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][5]==game[6][5]==game[7][5]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][5]==game[7][5]==game[8][5]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[7][5]==game[8][5]==game[9][5]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[0][6]==game[1][6]==game[2][6]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][6]==game[2][6]==game[3][6]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][6]==game[3][6]==game[4][6]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][6]==game[4][6]==game[5][6]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][6]==game[5][6]==game[6][6]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][6]==game[6][6]==game[7][6]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][6]==game[7][6]==game[8][6]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[7][6]==game[8][6]==game[9][6]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[0][7]==game[1][7]==game[2][7]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][7]==game[2][7]==game[3][7]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][7]==game[3][7]==game[4][7]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][7]==game[4][7]==game[5][7]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][7]==game[5][7]==game[6][7]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][7]==game[6][7]==game[7][7]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[6][7]==game[7][7]==game[8][7]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[7][7]==game[8][7]==game[9][7]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[0][8]==game[1][8]==game[2][8]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][8]==game[2][8]==game[3][8]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][8]==game[3][8]==game[4][8]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][8]==game[4][8]==game[5][8]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][8]==game[5][8]==game[6][8]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][8]==game[6][8]==game[7][8]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[6][8]==game[7][8]==game[8][8]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[7][8]==game[8][8]==game[9][8]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[0][9]==game[1][9]==game[2][9]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][9]==game[2][9]==game[3][9]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][9]==game[3][9]==game[4][9]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][9]==game[4][9]==game[5][9]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][9]==game[5][9]==game[6][9]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][9]==game[6][9]==game[7][9]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[6][9]==game[7][9]==game[8][9]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[7][9]==game[8][9]==game[9][9]==0) and (game[6][9]==None):
            game[6][9]="x"


        elif (game[4][0]==game[5][1]==game[6][2]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==0) and (game[4][0]==None):
            game[4][0]="x"
        elif (game[5][1]==game[6][2]==game[7][3]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][2]==game[7][3]==game[8][4]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[6][2]==game[7][3]==game[8][4]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[7][3]==game[8][4]==game[9][5]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[3][0]==game[4][1]==game[5][2]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==0) and (game[3][0]==None):
            game[3][0]="x"
        elif (game[4][1]==game[5][2]==game[6][3]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[5][2]==game[6][3]==game[7][4]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][3]==game[7][4]==game[8][5]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[6][3]==game[7][4]==game[8][5]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[7][4]==game[8][5]==game[9][6]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[2][0]==game[3][1]==game[4][2]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==0) and (game[2][0]==None):
            game[2][0]="x"
        elif (game[3][1]==game[4][2]==game[5][3]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[4][2]==game[5][3]==game[6][4]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[5][3]==game[6][4]==game[7][5]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[6][4]==game[7][5]==game[8][6]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[6][4]==game[7][5]==game[8][6]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[7][5]==game[8][6]==game[9][7]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[1][0]==game[2][1]==game[3][2]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==0) and (game[1][0]==None):
            game[1][0]="x"
        elif (game[2][1]==game[3][2]==game[4][3]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[3][2]==game[4][3]==game[5][4]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[4][3]==game[5][4]==game[6][5]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[5][4]==game[6][5]==game[7][6]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[6][5]==game[7][6]==game[8][7]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][5]==game[7][6]==game[8][7]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[7][6]==game[8][7]==game[9][8]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[0][0]==game[1][1]==game[2][2]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==0) and (game[0][0]==None):
            game[0][0]="x"
        elif (game[1][1]==game[2][2]==game[3][3]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[2][2]==game[3][3]==game[4][4]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[3][3]==game[4][4]==game[5][5]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[4][4]==game[5][5]==game[6][6]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][5]==game[6][6]==game[7][7]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[6][6]==game[7][7]==game[8][8]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][6]==game[7][7]==game[8][8]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[7][7]==game[8][8]==game[9][9]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[0][1]==game[1][2]==game[2][3]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[1][2]==game[2][3]==game[3][4]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[2][3]==game[3][4]==game[4][5]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[3][4]==game[4][5]==game[5][6]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][5]==game[5][6]==game[6][7]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[5][6]==game[6][7]==game[7][8]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][6]==game[6][7]==game[7][8]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[6][7]==game[7][8]==game[8][9]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[0][2]==game[1][3]==game[2][4]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[1][3]==game[2][4]==game[3][5]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[2][4]==game[3][5]==game[4][6]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][5]==game[4][6]==game[5][7]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[4][6]==game[5][7]==game[6][8]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][6]==game[5][7]==game[6][8]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[5][7]==game[6][8]==game[7][9]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[0][3]==game[1][4]==game[2][5]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[1][4]==game[2][5]==game[3][6]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][5]==game[3][6]==game[4][7]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[3][6]==game[4][7]==game[5][8]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][6]==game[4][7]==game[5][8]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[4][7]==game[5][8]==game[6][9]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[0][4]==game[1][5]==game[2][6]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[1][5]==game[2][6]==game[3][7]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[2][6]==game[3][7]==game[4][8]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][6]==game[3][7]==game[4][8]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[3][7]==game[4][8]==game[5][9]==0) and (game[2][6]==None):
            game[2][6]="x"


        elif (game[0][5]==game[1][4]==game[2][3]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[1][4]==game[2][3]==game[3][2]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[2][3]==game[3][2]==game[4][1]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[2][3]==game[3][2]==game[4][1]==0) and (game[5][0]==None):
            game[5][0]="x"
        elif (game[3][2]==game[4][1]==game[5][0]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[0][6]==game[1][5]==game[2][4]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[1][5]==game[2][4]==game[3][3]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[2][4]==game[3][3]==game[4][2]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[3][3]==game[4][2]==game[5][1]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[3][3]==game[4][2]==game[5][1]==0) and (game[6][0]==None):
            game[6][0]="x"
        elif (game[4][2]==game[5][1]==game[6][0]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[0][7]==game[1][6]==game[2][5]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[1][6]==game[2][5]==game[3][4]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[2][5]==game[3][4]==game[4][3]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[3][4]==game[4][3]==game[5][2]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[4][3]==game[5][2]==game[6][1]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[4][3]==game[5][2]==game[6][1]==0) and (game[7][0]==None):
            game[7][0]="x"
        elif (game[5][2]==game[6][1]==game[7][0]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[0][8]==game[1][7]==game[2][6]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][7]==game[2][6]==game[3][5]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[2][6]==game[3][5]==game[4][4]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[3][5]==game[4][4]==game[5][3]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[4][4]==game[5][3]==game[6][2]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[5][3]==game[6][2]==game[7][1]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[5][3]==game[6][2]==game[7][1]==0) and (game[8][0]==None):
            game[8][0]="x"
        elif (game[6][2]==game[7][1]==game[8][0]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[0][9]==game[1][8]==game[2][7]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[1][8]==game[2][7]==game[3][6]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][7]==game[3][6]==game[4][5]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[3][6]==game[4][5]==game[5][4]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[4][5]==game[5][4]==game[6][3]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[5][4]==game[6][3]==game[7][2]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[6][3]==game[7][2]==game[8][1]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[6][3]==game[7][2]==game[8][1]==0) and (game[9][0]==None):
            game[9][0]="x"
        elif (game[7][2]==game[8][1]==game[9][0]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[1][9]==game[2][8]==game[3][7]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[2][8]==game[3][7]==game[4][6]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][7]==game[4][6]==game[5][5]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[4][6]==game[5][5]==game[6][4]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[5][5]==game[6][4]==game[7][3]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[6][4]==game[7][3]==game[8][2]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[6][4]==game[7][3]==game[8][2]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[7][3]==game[8][2]==game[9][1]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[2][9]==game[3][8]==game[4][7]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[3][8]==game[4][7]==game[5][6]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][7]==game[5][6]==game[6][5]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[5][6]==game[6][5]==game[7][4]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[6][5]==game[7][4]==game[8][3]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[6][5]==game[7][4]==game[8][3]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[7][4]==game[8][3]==game[9][2]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[3][9]==game[4][8]==game[5][7]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[4][8]==game[5][7]==game[6][6]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][7]==game[6][6]==game[7][5]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[6][6]==game[7][5]==game[8][4]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[6][6]==game[7][5]==game[8][4]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[7][5]==game[8][4]==game[9][3]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[4][9]==game[5][8]==game[6][7]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[5][8]==game[6][7]==game[7][6]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[6][7]==game[7][6]==game[8][5]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[6][7]==game[7][6]==game[8][5]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[7][6]==game[8][5]==game[9][4]==0) and (game[6][7]==None):
            game[6][7]="x"



        elif (game[0][0]==0) and (game[0][1]==None):
            game[0][1]="x"
        elif (game[0][1]==0) and (game[0][2]==None):
            game[0][2]="x"
        elif (game[0][2]==0) and (game[0][3]==None):
            game[0][3]="x"
        elif (game[0][3]==0) and (game[0][4]==None):
            game[0][4]="x"
        elif (game[0][4]==0) and (game[0][5]==None):
            game[0][5]="x"
        elif (game[0][5]==0) and (game[0][6]==None):
            game[0][6]="x"
        elif (game[0][6]==0) and (game[0][7]==None):
            game[0][7]="x"
        elif (game[0][7]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[0][8]==0) and (game[0][9]==None):
            game[0][9]="x"
        elif (game[0][9]==0) and (game[0][8]==None):
            game[0][8]="x"
        elif (game[1][0]==0) and (game[1][1]==None):
            game[1][1]="x"
        elif (game[1][1]==0) and (game[1][2]==None):
            game[1][2]="x"
        elif (game[1][2]==0) and (game[1][3]==None):
            game[1][3]="x"
        elif (game[1][3]==0) and (game[1][4]==None):
            game[1][4]="x"
        elif (game[1][4]==0) and (game[1][5]==None):
            game[1][5]="x"
        elif (game[1][5]==0) and (game[1][6]==None):
            game[1][6]="x"
        elif (game[1][6]==0) and (game[1][7]==None):
            game[1][7]="x"
        elif (game[1][7]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[1][8]==0) and (game[1][9]==None):
            game[1][9]="x"
        elif (game[1][9]==0) and (game[1][8]==None):
            game[1][8]="x"
        elif (game[2][0]==0) and (game[2][1]==None):
            game[2][1]="x"
        elif (game[2][1]==0) and (game[2][2]==None):
            game[2][2]="x"
        elif (game[2][2]==0) and (game[2][3]==None):
            game[2][3]="x"
        elif (game[2][3]==0) and (game[2][4]==None):
            game[2][4]="x"
        elif (game[2][4]==0) and (game[2][5]==None):
            game[2][5]="x"
        elif (game[2][5]==0) and (game[2][6]==None):
            game[2][6]="x"
        elif (game[2][6]==0) and (game[2][7]==None):
            game[2][7]="x"
        elif (game[2][7]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[2][8]==0) and (game[2][9]==None):
            game[2][9]="x"
        elif (game[2][9]==0) and (game[2][8]==None):
            game[2][8]="x"
        elif (game[3][0]==0) and (game[3][1]==None):
            game[3][1]="x"
        elif (game[3][1]==0) and (game[3][2]==None):
            game[3][2]="x"
        elif (game[3][2]==0) and (game[3][3]==None):
            game[3][3]="x"
        elif (game[3][3]==0) and (game[3][4]==None):
            game[3][4]="x"
        elif (game[3][4]==0) and (game[3][5]==None):
            game[3][5]="x"
        elif (game[3][5]==0) and (game[3][6]==None):
            game[3][6]="x"
        elif (game[3][6]==0) and (game[3][7]==None):
            game[3][7]="x"
        elif (game[3][7]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[3][8]==0) and (game[3][9]==None):
            game[3][9]="x"
        elif (game[3][9]==0) and (game[3][8]==None):
            game[3][8]="x"
        elif (game[4][0]==0) and (game[4][1]==None):
            game[4][1]="x"
        elif (game[4][1]==0) and (game[4][2]==None):
            game[4][2]="x"
        elif (game[4][2]==0) and (game[4][3]==None):
            game[4][3]="x"
        elif (game[4][3]==0) and (game[4][4]==None):
            game[4][4]="x"
        elif (game[4][4]==0) and (game[4][5]==None):
            game[4][5]="x"
        elif (game[4][5]==0) and (game[4][6]==None):
            game[4][6]="x"
        elif (game[4][6]==0) and (game[4][7]==None):
            game[4][7]="x"
        elif (game[4][7]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[4][8]==0) and (game[4][9]==None):
            game[4][9]="x"
        elif (game[4][9]==0) and (game[4][8]==None):
            game[4][8]="x"
        elif (game[5][0]==0) and (game[5][1]==None):
            game[5][1]="x"
        elif (game[5][1]==0) and (game[5][2]==None):
            game[5][2]="x"
        elif (game[5][2]==0) and (game[5][3]==None):
            game[5][3]="x"
        elif (game[5][3]==0) and (game[5][4]==None):
            game[5][4]="x"
        elif (game[5][4]==0) and (game[5][5]==None):
            game[5][5]="x"
        elif (game[5][5]==0) and (game[5][6]==None):
            game[5][6]="x"
        elif (game[5][6]==0) and (game[5][7]==None):
            game[5][7]="x"
        elif (game[5][7]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[5][8]==0) and (game[5][9]==None):
            game[5][9]="x"
        elif (game[5][9]==0) and (game[5][8]==None):
            game[5][8]="x"
        elif (game[6][0]==0) and (game[6][1]==None):
            game[6][1]="x"
        elif (game[6][1]==0) and (game[6][2]==None):
            game[6][2]="x"
        elif (game[6][2]==0) and (game[6][3]==None):
            game[6][3]="x"
        elif (game[6][3]==0) and (game[6][4]==None):
            game[6][4]="x"
        elif (game[6][4]==0) and (game[6][5]==None):
            game[6][5]="x"
        elif (game[6][5]==0) and (game[6][6]==None):
            game[6][6]="x"
        elif (game[6][6]==0) and (game[6][7]==None):
            game[6][7]="x"
        elif (game[6][7]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[6][8]==0) and (game[6][9]==None):
            game[6][9]="x"
        elif (game[6][9]==0) and (game[6][8]==None):
            game[6][8]="x"
        elif (game[7][0]==0) and (game[7][1]==None):
            game[7][1]="x"
        elif (game[7][1]==0) and (game[7][2]==None):
            game[7][2]="x"
        elif (game[7][2]==0) and (game[7][3]==None):
            game[7][3]="x"
        elif (game[7][3]==0) and (game[7][4]==None):
            game[7][4]="x"
        elif (game[7][4]==0) and (game[7][5]==None):
            game[7][5]="x"
        elif (game[7][5]==0) and (game[7][6]==None):
            game[7][6]="x"
        elif (game[7][6]==0) and (game[7][7]==None):
            game[7][7]="x"
        elif (game[7][7]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[7][8]==0) and (game[7][9]==None):
            game[7][9]="x"
        elif (game[7][9]==0) and (game[7][8]==None):
            game[7][8]="x"
        elif (game[8][0]==0) and (game[8][1]==None):
            game[8][1]="x"
        elif (game[8][1]==0) and (game[8][2]==None):
            game[8][2]="x"
        elif (game[8][2]==0) and (game[8][3]==None):
            game[8][3]="x"
        elif (game[8][3]==0) and (game[8][4]==None):
            game[8][4]="x"
        elif (game[8][4]==0) and (game[8][5]==None):
            game[8][5]="x"
        elif (game[8][5]==0) and (game[8][6]==None):
            game[8][6]="x"
        elif (game[8][6]==0) and (game[8][7]==None):
            game[8][7]="x"
        elif (game[8][7]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[8][8]==0) and (game[8][9]==None):
            game[8][9]="x"
        elif (game[8][9]==0) and (game[8][8]==None):
            game[8][8]="x"
        elif (game[9][0]==0) and (game[9][1]==None):
            game[9][1]="x"
        elif (game[9][1]==0) and (game[9][2]==None):
            game[9][2]="x"
        elif (game[9][2]==0) and (game[9][3]==None):
            game[9][3]="x"
        elif (game[9][3]==0) and (game[9][4]==None):
            game[9][4]="x"
        elif (game[9][4]==0) and (game[9][5]==None):
            game[9][5]="x"
        elif (game[9][5]==0) and (game[9][6]==None):
            game[9][6]="x"
        elif (game[9][6]==0) and (game[9][7]==None):
            game[9][7]="x"
        elif (game[9][7]==0) and (game[9][8]==None):
            game[9][8]="x"
        elif (game[9][8]==0) and (game[9][9]==None):
            game[9][9]="x"
        elif (game[9][9]==0) and (game[9][8]==None):
            game[9][8]="x"



        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]==game[0][4]=="x") or (game[0][1]==game[0][2]==game[0][3]==game[0][4]==game[0][5]=="x") or (game[0][2]==game[0][3]==game[0][4]==game[0][5]==game[0][6]=="x") or (game[0][3]==game[0][4]==game[0][5]==game[0][6]==game[0][7]=="x") or (game[0][4]==game[0][5]==game[0][6]==game[0][7]==game[0][8]=="x") or (game[0][5]==game[0][6]==game[0][7]==game[0][8]==game[0][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[1][0]==game[1][1]==game[1][2]==game[1][3]==game[1][4]=="x") or (game[1][1]==game[1][2]==game[1][3]==game[1][4]==game[1][5]=="x") or (game[1][2]==game[1][3]==game[1][4]==game[1][5]==game[1][6]=="x") or (game[1][3]==game[1][4]==game[1][5]==game[1][6]==game[1][7]=="x") or (game[1][4]==game[1][5]==game[1][6]==game[1][7]==game[1][8]=="x") or (game[1][5]==game[1][6]==game[1][7]==game[1][8]==game[1][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[2][0]==game[2][1]==game[2][2]==game[2][3]==game[2][4]=="x") or (game[2][1]==game[2][2]==game[2][3]==game[2][4]==game[2][5]=="x") or (game[2][2]==game[2][3]==game[2][4]==game[2][5]==game[2][6]=="x") or (game[2][3]==game[2][4]==game[2][5]==game[2][6]==game[2][7]=="x") or (game[2][4]==game[2][5]==game[2][6]==game[2][7]==game[2][8]=="x") or (game[2][5]==game[2][6]==game[2][7]==game[2][8]==game[2][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[3][0]==game[3][1]==game[3][2]==game[3][3]==game[3][4]=="x") or (game[3][1]==game[3][2]==game[3][3]==game[3][4]==game[3][5]=="x") or (game[3][2]==game[3][3]==game[3][4]==game[3][5]==game[3][6]=="x") or (game[3][3]==game[3][4]==game[3][5]==game[3][6]==game[3][7]=="x") or (game[3][4]==game[3][5]==game[3][6]==game[3][7]==game[3][8]=="x") or (game[3][5]==game[3][6]==game[3][7]==game[3][8]==game[3][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[4][0]==game[4][1]==game[4][2]==game[4][3]==game[4][4]=="x") or (game[4][1]==game[4][2]==game[4][3]==game[4][4]==game[4][5]=="x") or (game[4][2]==game[4][3]==game[4][4]==game[4][5]==game[4][6]=="x") or (game[4][3]==game[4][4]==game[4][5]==game[4][6]==game[4][7]=="x") or (game[4][4]==game[4][5]==game[4][6]==game[4][7]==game[4][8]=="x") or (game[4][5]==game[4][6]==game[4][7]==game[4][8]==game[4][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[5][0]==game[5][1]==game[5][2]==game[5][3]==game[5][4]=="x") or (game[5][1]==game[5][2]==game[5][3]==game[5][4]==game[5][5]=="x") or (game[5][2]==game[5][3]==game[5][4]==game[5][5]==game[5][6]=="x") or (game[5][3]==game[5][4]==game[5][5]==game[5][6]==game[5][7]=="x") or (game[5][4]==game[5][5]==game[5][6]==game[5][7]==game[5][8]=="x") or (game[5][5]==game[5][6]==game[5][7]==game[5][8]==game[5][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[6][0]==game[6][1]==game[6][2]==game[6][3]==game[6][4]=="x") or (game[6][1]==game[6][2]==game[6][3]==game[6][4]==game[6][5]=="x") or (game[6][2]==game[6][3]==game[6][4]==game[6][5]==game[6][6]=="x") or (game[6][3]==game[6][4]==game[6][5]==game[6][6]==game[6][7]=="x") or (game[6][4]==game[6][5]==game[6][6]==game[6][7]==game[6][8]=="x") or (game[6][5]==game[6][6]==game[6][7]==game[6][8]==game[6][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[7][0]==game[7][1]==game[7][2]==game[7][3]==game[7][4]=="x") or (game[7][1]==game[7][2]==game[7][3]==game[7][4]==game[7][5]=="x") or (game[7][2]==game[7][3]==game[7][4]==game[7][5]==game[7][6]=="x") or (game[7][3]==game[7][4]==game[7][5]==game[7][6]==game[7][7]=="x") or (game[7][4]==game[7][5]==game[7][6]==game[7][7]==game[7][8]=="x") or (game[7][5]==game[7][6]==game[7][7]==game[7][8]==game[7][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[8][0]==game[8][1]==game[8][2]==game[8][3]==game[8][4]=="x") or (game[8][1]==game[8][2]==game[8][3]==game[8][4]==game[8][5]=="x") or (game[8][2]==game[8][3]==game[8][4]==game[8][5]==game[8][6]=="x") or (game[8][3]==game[8][4]==game[8][5]==game[8][6]==game[8][7]=="x") or (game[8][4]==game[8][5]==game[8][6]==game[8][7]==game[8][8]=="x") or (game[8][5]==game[8][6]==game[8][7]==game[8][8]==game[8][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[9][0]==game[9][1]==game[9][2]==game[9][3]==game[9][4]=="x") or (game[9][1]==game[9][2]==game[9][3]==game[9][4]==game[9][5]=="x") or (game[9][2]==game[9][3]==game[9][4]==game[9][5]==game[9][6]=="x") or (game[9][3]==game[9][4]==game[9][5]==game[9][6]==game[9][7]=="x") or (game[9][4]==game[9][5]==game[9][6]==game[9][7]==game[9][8]=="x") or (game[9][5]==game[9][6]==game[9][7]==game[9][8]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[5][0]==game[6][1]==game[7][2]==game[8][3]==game[9][4]=="x") or (game[4][0]==game[5][1]==game[6][2]==game[7][3]==game[8][4]=="x") or (game[5][1]==game[6][2]==game[7][3]==game[8][4]==game[9][5]=="x") or (game[3][0]==game[4][1]==game[5][2]==game[6][3]==game[7][4]=="x") or (game[4][1]==game[5][2]==game[6][3]==game[7][4]==game[8][5]=="x") or (game[5][2]==game[6][3]==game[7][4]==game[8][5]==game[9][6]=="x") or (game[2][0]==game[3][1]==game[4][2]==game[5][3]==game[6][4]=="x") or (game[3][1]==game[4][2]==game[5][3]==game[6][4]==game[7][5]=="x") or (game[4][2]==game[5][3]==game[6][4]==game[7][5]==game[8][6]=="x") or (game[5][3]==game[6][4]==game[7][5]==game[8][6]==game[9][7]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[1][0]==game[2][1]==game[3][2]==game[4][3]==game[5][4]=="x") or (game[2][1]==game[3][2]==game[4][3]==game[5][4]==game[6][5]=="x") or (game[3][2]==game[4][3]==game[5][4]==game[6][5]==game[7][6]=="x") or (game[4][3]==game[5][4]==game[6][5]==game[7][6]==game[8][7]=="x") or (game[5][4]==game[6][5]==game[7][6]==game[8][7]==game[9][8]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][0]==game[1][1]==game[2][2]==game[3][3]==game[4][4]=="x") or (game[1][1]==game[2][2]==game[3][3]==game[4][4]==game[5][5]=="x") or (game[2][2]==game[3][3]==game[4][4]==game[5][5]==game[6][6]=="x") or (game[3][3]==game[4][4]==game[5][5]==game[6][6]==game[7][7]=="x") or (game[4][4]==game[5][5]==game[6][6]==game[7][7]==game[8][8]=="x") or (game[5][5]==game[6][6]==game[7][7]==game[8][8]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][1]==game[1][2]==game[2][3]==game[3][4]==game[4][5]=="x") or (game[1][2]==game[2][3]==game[3][4]==game[4][5]==game[5][6]=="x") or (game[2][3]==game[3][4]==game[4][5]==game[5][6]==game[6][7]=="x") or (game[3][4]==game[4][5]==game[5][6]==game[6][7]==game[7][8]=="x") or (game[4][5]==game[5][6]==game[6][7]==game[7][8]==game[8][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][2]==game[1][3]==game[2][4]==game[3][5]==game[4][6]=="x") or (game[1][3]==game[2][4]==game[3][5]==game[4][6]==game[5][7]=="x") or (game[2][4]==game[3][5]==game[4][6]==game[5][7]==game[6][8]=="x") or (game[3][5]==game[4][6]==game[5][7]==game[6][8]==game[7][9]=="x") or (game[0][3]==game[1][4]==game[2][5]==game[3][6]==game[4][7]=="x") or (game[1][4]==game[2][5]==game[3][6]==game[4][7]==game[5][8]=="x") or (game[2][5]==game[3][6]==game[4][7]==game[5][8]==game[6][9]=="x") or (game[0][4]==game[1][5]==game[2][6]==game[3][7]==game[4][8]=="x") or (game[1][5]==game[2][6]==game[3][7]==game[4][8]==game[5][9]=="x") or (game[0][5]==game[1][6]==game[2][7]==game[3][8]==game[4][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[4][0]==game[3][1]==game[2][2]==game[1][3]==game[0][4]=="x") or (game[5][0]==game[4][1]==game[3][2]==game[2][3]==game[1][4]=="x") or (game[4][1]==game[3][2]==game[2][3]==game[1][4]==game[0][5]=="x") or (game[6][0]==game[5][1]==game[4][2]==game[3][3]==game[2][4]=="x") or (game[5][1]==game[4][2]==game[3][3]==game[2][4]==game[1][5]=="x") or (game[4][2]==game[3][3]==game[2][4]==game[1][5]==game[0][6]=="x") or (game[7][0]==game[6][1]==game[5][2]==game[4][3]==game[3][4]=="x") or (game[6][1]==game[5][2]==game[4][3]==game[3][4]==game[2][5]=="x") or (game[5][2]==game[4][3]==game[3][4]==game[2][5]==game[1][6]=="x") or (game[4][3]==game[3][4]==game[2][5]==game[1][6]==game[0][7]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[8][0]==game[7][1]==game[6][2]==game[5][3]==game[4][4]=="x") or (game[7][1]==game[6][2]==game[5][3]==game[4][4]==game[3][5]=="x") or (game[6][2]==game[5][3]==game[4][4]==game[3][5]==game[2][6]=="x") or (game[5][3]==game[4][4]==game[3][5]==game[2][6]==game[1][7]=="x") or (game[4][4]==game[3][5]==game[2][6]==game[1][7]==game[0][8]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[9][0]==game[8][1]==game[7][2]==game[6][3]==game[5][4]=="x") or (game[8][1]==game[7][2]==game[6][3]==game[5][4]==game[4][5]=="x") or (game[7][2]==game[6][3]==game[5][4]==game[4][5]==game[3][6]=="x") or (game[6][3]==game[5][4]==game[4][5]==game[3][6]==game[2][7]=="x") or (game[5][4]==game[4][5]==game[3][6]==game[2][7]==game[1][8]=="x") or (game[4][5]==game[3][6]==game[2][7]==game[1][8]==game[0][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[9][1]==game[8][2]==game[7][3]==game[6][4]==game[5][5]=="x") or (game[8][2]==game[7][3]==game[6][4]==game[5][5]==game[4][6]=="x") or (game[7][3]==game[6][4]==game[5][5]==game[4][6]==game[3][7]=="x") or (game[6][4]==game[5][5]==game[4][6]==game[3][7]==game[2][8]=="x") or (game[5][5]==game[4][6]==game[3][7]==game[2][8]==game[1][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[9][2]==game[8][3]==game[7][4]==game[6][5]==game[5][6]=="x") or (game[8][3]==game[7][4]==game[6][5]==game[5][6]==game[4][7]=="x") or (game[7][4]==game[6][5]==game[5][6]==game[4][7]==game[3][8]=="x") or (game[6][5]==game[5][6]==game[4][7]==game[3][8]==game[2][9]=="x") or (game[9][3]==game[8][4]==game[7][5]==game[6][6]==game[5][7]=="x") or (game[8][4]==game[7][5]==game[6][6]==game[5][7]==game[4][8]=="x") or (game[7][5]==game[6][6]==game[5][7]==game[4][8]==game[3][9]=="x") or (game[9][4]==game[8][5]==game[7][6]==game[6][7]==game[5][8]=="x") or (game[8][5]==game[7][6]==game[6][7]==game[5][8]==game[4][9]=="x") or (game[9][5]==game[8][6]==game[7][7]==game[6][8]==game[5][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][0]==game[1][0]==game[2][0]==game[3][0]==game[4][0]=="x") or (game[1][0]==game[2][0]==game[3][0]==game[4][0]==game[5][0]=="x") or (game[2][0]==game[3][0]==game[4][0]==game[5][0]==game[6][0]=="x") or (game[3][0]==game[4][0]==game[5][0]==game[6][0]==game[7][0]=="x") or (game[4][0]==game[5][0]==game[6][0]==game[7][0]==game[8][0]=="x") or (game[5][0]==game[6][0]==game[7][0]==game[8][0]==game[9][0]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][1]==game[1][1]==game[2][1]==game[3][1]==game[4][1]=="x") or (game[1][1]==game[2][1]==game[3][1]==game[4][1]==game[5][1]=="x") or (game[2][1]==game[3][1]==game[4][1]==game[5][1]==game[6][1]=="x") or (game[3][1]==game[4][1]==game[5][1]==game[6][1]==game[7][1]=="x") or (game[4][1]==game[5][1]==game[6][1]==game[7][1]==game[8][1]=="x") or (game[5][1]==game[6][1]==game[7][1]==game[8][1]==game[9][1]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][2]==game[1][2]==game[2][2]==game[3][2]==game[4][2]=="x") or (game[1][2]==game[2][2]==game[3][2]==game[4][2]==game[5][2]=="x") or (game[2][2]==game[3][2]==game[4][2]==game[5][2]==game[6][2]=="x") or (game[3][2]==game[4][2]==game[5][2]==game[6][2]==game[7][2]=="x") or (game[4][2]==game[5][2]==game[6][2]==game[7][2]==game[8][2]=="x") or (game[5][2]==game[6][2]==game[7][2]==game[8][2]==game[9][2]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][3]==game[1][3]==game[2][3]==game[3][3]==game[4][3]=="x") or (game[1][3]==game[2][3]==game[3][3]==game[4][3]==game[5][3]=="x") or (game[2][3]==game[3][3]==game[4][3]==game[5][3]==game[6][3]=="x") or (game[3][3]==game[4][3]==game[5][3]==game[6][3]==game[7][3]=="x") or (game[4][3]==game[5][3]==game[6][3]==game[7][3]==game[8][3]=="x") or (game[5][3]==game[6][3]==game[7][3]==game[8][3]==game[9][3]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][4]==game[1][4]==game[2][4]==game[3][4]==game[4][4]=="x") or (game[1][4]==game[2][4]==game[3][4]==game[4][4]==game[5][4]=="x") or (game[2][4]==game[3][4]==game[4][4]==game[5][4]==game[6][4]=="x") or (game[3][4]==game[4][4]==game[5][4]==game[6][4]==game[7][4]=="x") or (game[4][4]==game[5][4]==game[6][4]==game[7][4]==game[8][4]=="x") or (game[5][4]==game[6][4]==game[7][4]==game[8][4]==game[9][4]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][5]==game[1][5]==game[2][5]==game[3][5]==game[4][5]=="x") or (game[1][5]==game[2][5]==game[3][5]==game[4][5]==game[5][5]=="x") or (game[2][5]==game[3][5]==game[4][5]==game[5][5]==game[6][5]=="x") or (game[3][5]==game[4][5]==game[5][5]==game[6][5]==game[7][5]=="x") or (game[4][5]==game[5][5]==game[6][5]==game[7][5]==game[8][5]=="x") or (game[5][5]==game[6][5]==game[7][5]==game[8][5]==game[9][5]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][6]==game[1][6]==game[2][6]==game[3][6]==game[4][6]=="x") or (game[1][6]==game[2][6]==game[3][6]==game[4][6]==game[5][6]=="x") or (game[2][6]==game[3][6]==game[4][6]==game[5][6]==game[6][6]=="x") or (game[3][6]==game[4][6]==game[5][6]==game[6][6]==game[7][6]=="x") or (game[4][6]==game[5][6]==game[6][6]==game[7][6]==game[8][6]=="x") or (game[5][6]==game[6][6]==game[7][6]==game[8][6]==game[9][6]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][7]==game[1][7]==game[2][7]==game[3][7]==game[4][7]=="x") or (game[1][7]==game[2][7]==game[3][7]==game[4][7]==game[5][7]=="x") or (game[2][7]==game[3][7]==game[4][7]==game[5][7]==game[6][7]=="x") or (game[3][7]==game[4][7]==game[5][7]==game[6][7]==game[7][7]=="x") or (game[4][7]==game[5][7]==game[6][7]==game[7][7]==game[8][7]=="x") or (game[5][7]==game[6][7]==game[7][7]==game[8][7]==game[9][7]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][8]==game[1][8]==game[2][8]==game[3][8]==game[4][8]=="x") or (game[1][8]==game[2][8]==game[3][8]==game[4][8]==game[5][8]=="x") or (game[2][8]==game[3][8]==game[4][8]==game[5][8]==game[6][8]=="x") or (game[3][8]==game[4][8]==game[5][8]==game[6][8]==game[7][8]=="x") or (game[4][8]==game[5][8]==game[6][8]==game[7][8]==game[8][8]=="x") or (game[5][8]==game[6][8]==game[7][8]==game[8][8]==game[9][8]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)
        if (game[0][9]==game[1][9]==game[2][9]==game[3][9]==game[4][9]=="x") or (game[1][9]==game[2][9]==game[3][9]==game[4][9]==game[5][9]=="x") or (game[2][9]==game[3][9]==game[4][9]==game[5][9]==game[6][9]=="x") or (game[3][9]==game[4][9]==game[5][9]==game[6][9]==game[7][9]=="x") or (game[4][9]==game[5][9]==game[6][9]==game[7][9]==game[8][9]=="x") or (game[5][9]==game[6][9]==game[7][9]==game[8][9]==game[9][9]=="x"):
            game.print("Победа крестиков!!!                                    Ход: ", hod)

    def menu(key):
        if key=="Escape":
            game.close()
        elif key=="F1":
            restart()
        elif key=="F2":
            pass
        elif key=="F3":
            pass

    def mouse_click(button,rows,columns):
        global hod,match_count
        if game[rows][columns]==None:
            game[rows][columns]=0
        hod += 1
        game.print(menuMSG, "                                        Ход:", hod)

        if (game[0][0]==game[0][1]==game[0][2]==game[0][3]==game[0][4]==0) or (game[0][1]==game[0][2]==game[0][3]==game[0][4]==game[0][5]==0) or (game[0][2]==game[0][3]==game[0][4]==game[0][5]==game[0][6]==0) or (game[0][3]==game[0][4]==game[0][5]==game[0][6]==game[0][7]==0) or (game[0][4]==game[0][5]==game[0][6]==game[0][7]==game[0][8]==0) or (game[0][5]==game[0][6]==game[0][7]==game[0][8]==game[0][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[1][0]==game[1][1]==game[1][2]==game[1][3]==game[1][4]==0) or (game[1][1]==game[1][2]==game[1][3]==game[1][4]==game[1][5]==0) or (game[1][2]==game[1][3]==game[1][4]==game[1][5]==game[1][6]==0) or (game[1][3]==game[1][4]==game[1][5]==game[1][6]==game[1][7]==0) or (game[1][4]==game[1][5]==game[1][6]==game[1][7]==game[1][8]==0) or (game[1][5]==game[1][6]==game[1][7]==game[1][8]==game[1][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[2][0]==game[2][1]==game[2][2]==game[2][3]==game[2][4]==0) or (game[2][1]==game[2][2]==game[2][3]==game[2][4]==game[2][5]==0) or (game[2][2]==game[2][3]==game[2][4]==game[2][5]==game[2][6]==0) or (game[2][3]==game[2][4]==game[2][5]==game[2][6]==game[2][7]==0) or (game[2][4]==game[2][5]==game[2][6]==game[2][7]==game[2][8]==0) or (game[2][5]==game[2][6]==game[2][7]==game[2][8]==game[2][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[3][0]==game[3][1]==game[3][2]==game[3][3]==game[3][4]==0) or (game[3][1]==game[3][2]==game[3][3]==game[3][4]==game[3][5]==0) or (game[3][2]==game[3][3]==game[3][4]==game[3][5]==game[3][6]==0) or (game[3][3]==game[3][4]==game[3][5]==game[3][6]==game[3][7]==0) or (game[3][4]==game[3][5]==game[3][6]==game[3][7]==game[3][8]==0) or (game[3][5]==game[3][6]==game[3][7]==game[3][8]==game[3][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[4][0]==game[4][1]==game[4][2]==game[4][3]==game[4][4]==0) or (game[4][1]==game[4][2]==game[4][3]==game[4][4]==game[4][5]==0) or (game[4][2]==game[4][3]==game[4][4]==game[4][5]==game[4][6]==0) or (game[4][3]==game[4][4]==game[4][5]==game[4][6]==game[4][7]==0) or (game[4][4]==game[4][5]==game[4][6]==game[4][7]==game[4][8]==0) or (game[4][5]==game[4][6]==game[4][7]==game[4][8]==game[4][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[5][0]==game[5][1]==game[5][2]==game[5][3]==game[5][4]==0) or (game[5][1]==game[5][2]==game[5][3]==game[5][4]==game[5][5]==0) or (game[5][2]==game[5][3]==game[5][4]==game[5][5]==game[5][6]==0) or (game[5][3]==game[5][4]==game[5][5]==game[5][6]==game[5][7]==0) or (game[5][4]==game[5][5]==game[5][6]==game[5][7]==game[5][8]==0) or (game[5][5]==game[5][6]==game[5][7]==game[5][8]==game[5][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[6][0]==game[6][1]==game[6][2]==game[6][3]==game[6][4]==0) or (game[6][1]==game[6][2]==game[6][3]==game[6][4]==game[6][5]==0) or (game[6][2]==game[6][3]==game[6][4]==game[6][5]==game[6][6]==0) or (game[6][3]==game[6][4]==game[6][5]==game[6][6]==game[6][7]==0) or (game[6][4]==game[6][5]==game[6][6]==game[6][7]==game[6][8]==0) or (game[6][5]==game[6][6]==game[6][7]==game[6][8]==game[6][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[7][0]==game[7][1]==game[7][2]==game[7][3]==game[7][4]==0) or (game[7][1]==game[7][2]==game[7][3]==game[7][4]==game[7][5]==0) or (game[7][2]==game[7][3]==game[7][4]==game[7][5]==game[7][6]==0) or (game[7][3]==game[7][4]==game[7][5]==game[7][6]==game[7][7]==0) or (game[7][4]==game[7][5]==game[7][6]==game[7][7]==game[7][8]==0) or (game[7][5]==game[7][6]==game[7][7]==game[7][8]==game[7][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[8][0]==game[8][1]==game[8][2]==game[8][3]==game[8][4]==0) or (game[8][1]==game[8][2]==game[8][3]==game[8][4]==game[8][5]==0) or (game[8][2]==game[8][3]==game[8][4]==game[8][5]==game[8][6]==0) or (game[8][3]==game[8][4]==game[8][5]==game[8][6]==game[8][7]==0) or (game[8][4]==game[8][5]==game[8][6]==game[8][7]==game[8][8]==0) or (game[8][5]==game[8][6]==game[8][7]==game[8][8]==game[8][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[9][0]==game[9][1]==game[9][2]==game[9][3]==game[9][4]==0) or (game[9][1]==game[9][2]==game[9][3]==game[9][4]==game[9][5]==0) or (game[9][2]==game[9][3]==game[9][4]==game[9][5]==game[9][6]==0) or (game[9][3]==game[9][4]==game[9][5]==game[9][6]==game[9][7]==0) or (game[9][4]==game[9][5]==game[9][6]==game[9][7]==game[9][8]==0) or (game[9][5]==game[9][6]==game[9][7]==game[9][8]==game[9][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[5][0]==game[6][1]==game[7][2]==game[8][3]==game[9][4]==0) or (game[4][0]==game[5][1]==game[6][2]==game[7][3]==game[8][4]==0) or (game[5][1]==game[6][2]==game[7][3]==game[8][4]==game[9][5]==0) or (game[3][0]==game[4][1]==game[5][2]==game[6][3]==game[7][4]==0) or (game[4][1]==game[5][2]==game[6][3]==game[7][4]==game[8][5]==0) or (game[5][2]==game[6][3]==game[7][4]==game[8][5]==game[9][6]==0) or (game[2][0]==game[3][1]==game[4][2]==game[5][3]==game[6][4]==0) or (game[3][1]==game[4][2]==game[5][3]==game[6][4]==game[7][5]==0) or (game[4][2]==game[5][3]==game[6][4]==game[7][5]==game[8][6]==0) or (game[5][3]==game[6][4]==game[7][5]==game[8][6]==game[9][7]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[1][0]==game[2][1]==game[3][2]==game[4][3]==game[5][4]==0) or (game[2][1]==game[3][2]==game[4][3]==game[5][4]==game[6][5]==0) or (game[3][2]==game[4][3]==game[5][4]==game[6][5]==game[7][6]==0) or (game[4][3]==game[5][4]==game[6][5]==game[7][6]==game[8][7]==0) or (game[5][4]==game[6][5]==game[7][6]==game[8][7]==game[9][8]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][0]==game[1][1]==game[2][2]==game[3][3]==game[4][4]==0) or (game[1][1]==game[2][2]==game[3][3]==game[4][4]==game[5][5]==0) or (game[2][2]==game[3][3]==game[4][4]==game[5][5]==game[6][6]==0) or (game[3][3]==game[4][4]==game[5][5]==game[6][6]==game[7][7]==0) or (game[4][4]==game[5][5]==game[6][6]==game[7][7]==game[8][8]==0) or (game[5][5]==game[6][6]==game[7][7]==game[8][8]==game[9][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][1]==game[1][2]==game[2][3]==game[3][4]==game[4][5]==0) or (game[1][2]==game[2][3]==game[3][4]==game[4][5]==game[5][6]==0) or (game[2][3]==game[3][4]==game[4][5]==game[5][6]==game[6][7]==0) or (game[3][4]==game[4][5]==game[5][6]==game[6][7]==game[7][8]==0) or (game[4][5]==game[5][6]==game[6][7]==game[7][8]==game[8][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][2]==game[1][3]==game[2][4]==game[3][5]==game[4][6]==0) or (game[1][3]==game[2][4]==game[3][5]==game[4][6]==game[5][7]==0) or (game[2][4]==game[3][5]==game[4][6]==game[5][7]==game[6][8]==0) or (game[3][5]==game[4][6]==game[5][7]==game[6][8]==game[7][9]==0) or (game[0][3]==game[1][4]==game[2][5]==game[3][6]==game[4][7]==0) or (game[1][4]==game[2][5]==game[3][6]==game[4][7]==game[5][8]==0) or (game[2][5]==game[3][6]==game[4][7]==game[5][8]==game[6][9]==0) or (game[0][4]==game[1][5]==game[2][6]==game[3][7]==game[4][8]==0) or (game[1][5]==game[2][6]==game[3][7]==game[4][8]==game[5][9]==0) or (game[0][5]==game[1][6]==game[2][7]==game[3][8]==game[4][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[4][0]==game[3][1]==game[2][2]==game[1][3]==game[0][4]==0) or (game[5][0]==game[4][1]==game[3][2]==game[2][3]==game[1][4]==0) or (game[4][1]==game[3][2]==game[2][3]==game[1][4]==game[0][5]==0) or (game[6][0]==game[5][1]==game[4][2]==game[3][3]==game[2][4]==0) or (game[5][1]==game[4][2]==game[3][3]==game[2][4]==game[1][5]==0) or (game[4][2]==game[3][3]==game[2][4]==game[1][5]==game[0][6]==0) or (game[7][0]==game[6][1]==game[5][2]==game[4][3]==game[3][4]==0) or (game[6][1]==game[5][2]==game[4][3]==game[3][4]==game[2][5]==0) or (game[5][2]==game[4][3]==game[3][4]==game[2][5]==game[1][6]==0) or (game[4][3]==game[3][4]==game[2][5]==game[1][6]==game[0][7]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[8][0]==game[7][1]==game[6][2]==game[5][3]==game[4][4]==0) or (game[7][1]==game[6][2]==game[5][3]==game[4][4]==game[3][5]==0) or (game[6][2]==game[5][3]==game[4][4]==game[3][5]==game[2][6]==0) or (game[5][3]==game[4][4]==game[3][5]==game[2][6]==game[1][7]==0) or (game[4][4]==game[3][5]==game[2][6]==game[1][7]==game[0][8]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[9][0]==game[8][1]==game[7][2]==game[6][3]==game[5][4]==0) or (game[8][1]==game[7][2]==game[6][3]==game[5][4]==game[4][5]==0) or (game[7][2]==game[6][3]==game[5][4]==game[4][5]==game[3][6]==0) or (game[6][3]==game[5][4]==game[4][5]==game[3][6]==game[2][7]==0) or (game[5][4]==game[4][5]==game[3][6]==game[2][7]==game[1][8]==0) or (game[4][5]==game[3][6]==game[2][7]==game[1][8]==game[0][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[9][1]==game[8][2]==game[7][3]==game[6][4]==game[5][5]==0) or (game[8][2]==game[7][3]==game[6][4]==game[5][5]==game[4][6]==0) or (game[7][3]==game[6][4]==game[5][5]==game[4][6]==game[3][7]==0) or (game[6][4]==game[5][5]==game[4][6]==game[3][7]==game[2][8]==0) or (game[5][5]==game[4][6]==game[3][7]==game[2][8]==game[1][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[9][2]==game[8][3]==game[7][4]==game[6][5]==game[5][6]==0) or (game[8][3]==game[7][4]==game[6][5]==game[5][6]==game[4][7]==0) or (game[7][4]==game[6][5]==game[5][6]==game[4][7]==game[3][8]==0) or (game[6][5]==game[5][6]==game[4][7]==game[3][8]==game[2][9]==0) or (game[9][3]==game[8][4]==game[7][5]==game[6][6]==game[5][7]==0) or (game[8][4]==game[7][5]==game[6][6]==game[5][7]==game[4][8]==0) or (game[7][5]==game[6][6]==game[5][7]==game[4][8]==game[3][9]==0) or (game[9][4]==game[8][5]==game[7][6]==game[6][7]==game[5][8]==0) or (game[8][5]==game[7][6]==game[6][7]==game[5][8]==game[4][9]==0) or (game[9][5]==game[8][6]==game[7][7]==game[6][8]==game[5][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][0]==game[1][0]==game[2][0]==game[3][0]==game[4][0]==0) or (game[1][0]==game[2][0]==game[3][0]==game[4][0]==game[5][0]==0) or (game[2][0]==game[3][0]==game[4][0]==game[5][0]==game[6][0]==0) or (game[3][0]==game[4][0]==game[5][0]==game[6][0]==game[7][0]==0) or (game[4][0]==game[5][0]==game[6][0]==game[7][0]==game[8][0]==0) or (game[5][0]==game[6][0]==game[7][0]==game[8][0]==game[9][0]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][1]==game[1][1]==game[2][1]==game[3][1]==game[4][1]==0) or (game[1][1]==game[2][1]==game[3][1]==game[4][1]==game[5][1]==0) or (game[2][1]==game[3][1]==game[4][1]==game[5][1]==game[6][1]==0) or (game[3][1]==game[4][1]==game[5][1]==game[6][1]==game[7][1]==0) or (game[4][1]==game[5][1]==game[6][1]==game[7][1]==game[8][1]==0) or (game[5][1]==game[6][1]==game[7][1]==game[8][1]==game[9][1]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][2]==game[1][2]==game[2][2]==game[3][2]==game[4][2]==0) or (game[1][2]==game[2][2]==game[3][2]==game[4][2]==game[5][2]==0) or (game[2][2]==game[3][2]==game[4][2]==game[5][2]==game[6][2]==0) or (game[3][2]==game[4][2]==game[5][2]==game[6][2]==game[7][2]==0) or (game[4][2]==game[5][2]==game[6][2]==game[7][2]==game[8][2]==0) or (game[5][2]==game[6][2]==game[7][2]==game[8][2]==game[9][2]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][3]==game[1][3]==game[2][3]==game[3][3]==game[4][3]==0) or (game[1][3]==game[2][3]==game[3][3]==game[4][3]==game[5][3]==0) or (game[2][3]==game[3][3]==game[4][3]==game[5][3]==game[6][3]==0) or (game[3][3]==game[4][3]==game[5][3]==game[6][3]==game[7][3]==0) or (game[4][3]==game[5][3]==game[6][3]==game[7][3]==game[8][3]==0) or (game[5][3]==game[6][3]==game[7][3]==game[8][3]==game[9][3]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][4]==game[1][4]==game[2][4]==game[3][4]==game[4][4]==0) or (game[1][4]==game[2][4]==game[3][4]==game[4][4]==game[5][4]==0) or (game[2][4]==game[3][4]==game[4][4]==game[5][4]==game[6][4]==0) or (game[3][4]==game[4][4]==game[5][4]==game[6][4]==game[7][4]==0) or (game[4][4]==game[5][4]==game[6][4]==game[7][4]==game[8][4]==0) or (game[5][4]==game[6][4]==game[7][4]==game[8][4]==game[9][4]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][5]==game[1][5]==game[2][5]==game[3][5]==game[4][5]==0) or (game[1][5]==game[2][5]==game[3][5]==game[4][5]==game[5][5]==0) or (game[2][5]==game[3][5]==game[4][5]==game[5][5]==game[6][5]==0) or (game[3][5]==game[4][5]==game[5][5]==game[6][5]==game[7][5]==0) or (game[4][5]==game[5][5]==game[6][5]==game[7][5]==game[8][5]==0) or (game[5][5]==game[6][5]==game[7][5]==game[8][5]==game[9][5]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][6]==game[1][6]==game[2][6]==game[3][6]==game[4][6]==0) or (game[1][6]==game[2][6]==game[3][6]==game[4][6]==game[5][6]==0) or (game[2][6]==game[3][6]==game[4][6]==game[5][6]==game[6][6]==0) or (game[3][6]==game[4][6]==game[5][6]==game[6][6]==game[7][6]==0) or (game[4][6]==game[5][6]==game[6][6]==game[7][6]==game[8][6]==0) or (game[5][6]==game[6][6]==game[7][6]==game[8][6]==game[9][6]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][7]==game[1][7]==game[2][7]==game[3][7]==game[4][7]==0) or (game[1][7]==game[2][7]==game[3][7]==game[4][7]==game[5][7]==0) or (game[2][7]==game[3][7]==game[4][7]==game[5][7]==game[6][7]==0) or (game[3][7]==game[4][7]==game[5][7]==game[6][7]==game[7][7]==0) or (game[4][7]==game[5][7]==game[6][7]==game[7][7]==game[8][7]==0) or (game[5][7]==game[6][7]==game[7][7]==game[8][7]==game[9][7]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][8]==game[1][8]==game[2][8]==game[3][8]==game[4][8]==0) or (game[1][8]==game[2][8]==game[3][8]==game[4][8]==game[5][8]==0) or (game[2][8]==game[3][8]==game[4][8]==game[5][8]==game[6][8]==0) or (game[3][8]==game[4][8]==game[5][8]==game[6][8]==game[7][8]==0) or (game[4][8]==game[5][8]==game[6][8]==game[7][8]==game[8][8]==0) or (game[5][8]==game[6][8]==game[7][8]==game[8][8]==game[9][8]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        if (game[0][9]==game[1][9]==game[2][9]==game[3][9]==game[4][9]==0) or (game[1][9]==game[2][9]==game[3][9]==game[4][9]==game[5][9]==0) or (game[2][9]==game[3][9]==game[4][9]==game[5][9]==game[6][9]==0) or (game[3][9]==game[4][9]==game[5][9]==game[6][9]==game[7][9]==0) or (game[4][9]==game[5][9]==game[6][9]==game[7][9]==game[8][9]==0) or (game[5][9]==game[6][9]==game[7][9]==game[8][9]==game[9][9]==0):
            game.print("Победа ноликов!!!                                        Ход: ", hod)
        botZero()
        if hod>100:
            game.print("Ничья!!!                                            Ход: ", hod)

    def restart():
        global previous_row,previous_col,hod,match_count
        previous_row=previous_col=hod=0
        game.clear()
        match_count+=1
        game.print(menuMSG, "Матч: ", match_count)

    game=Board(10, 10)
    game.title="Gomoku"
    game.cell_size=50
    game.cell_color="lightblue"
    game.create_output(background_color="wheat4", color="white")
    game.on_mouse_click=mouse_click
    game.on_key_press = menu
    game.print(menuMSG)
    game.show()