def main():
    win_combinations = [(1, 5, 9), (1, 4, 7), (1, 2, 3), (2, 5, 8), (3, 6, 9), (3, 5, 7), (4, 5, 6), (7, 8, 9)]
    board = [None] + list(range(1,10))

    def drawBoard():
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print()


    def pickNumber():
        while True:
            try:
                a = int(input())
                if a in board:
                    return a
                else:
                    print("Invalid Move")
            except ValueError:
                print("That's not a number")

    def gameOver():
        for a, b, c in win_combinations:
            if board[a] == board[b] == board[c]:
                print("player {0} wins".format(board[a]))
                return True


    for player in 'XO' * 9:
        drawBoard()
        if gameOver():
            break
        print("Player {0} pick your move: ".format(player))
        board[pickNumber()] = player
        print()

while True:
    main()

        #if 9 ==sum((pos == 'S' or pos == ))




#for i in range(0 , 3):
   # place = raw_input('There are 9 places you can choose from. Please pick a number from 1-9:' )
    #num.append(place)
#print(num)


#place2 = raw_input("There are 9 places you can choose from. Please pick a number from 1-9")



