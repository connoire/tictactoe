from random import randint

def minimax(state, computer):

    status = checkwin(state)
    



    return

def checkwin(state):

    wincombo = [set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9]), set([1, 4, 7]), set([2, 5, 8]), set([3, 6, 9]), set([1, 5, 9]), set([3, 5, 7])]

    x = set()
    o = set()
    
    for i in range(1, 10):
        if state[i] == 'X':
            x.add(i)
        if state[i] == 'O':
            o.add(i)

    for combo in wincombo:
        if combo.issubset(x):
            return 'X'
        if combo.issubset(o):
            return 'O'
        
    return None

def generatemoves(state):

    moves = []
    for i in range(1, 10):
        if state[i] == '.':
            moves.append(i)

    return moves

def printboard(state):

    print(f'{state[1]} | {state[2]} | {state[3]}')
    print('- - - - -')
    print(f'{state[4]} | {state[5]} | {state[6]}')
    print('- - - - -')
    print(f'{state[7]} | {state[8]} | {state[9]}')

def oneplayer():
        
    state = [None, '.', '.', '.', '.', '.', '.', '.', '.', '.']
    turn = 0
    rand = randint(1, 2)
    
    if randint(1, 2) == 1:
        player = 'X'
        computer = 'O'
    else:
        computer = 'X'
        player = 'O'

    printboard(state)

    while True:
        
        status = checkwin(state)

        if status == player:
            print('You Win')
            return

        if status == computer:
            print('You Lose')
            return

        if turn == 9:
            print('Draw')
            return

        if status == 0:

            if (turn + rand) % 2 == 0:
                place = int(input("Where would you like to play: "))
                state[place] = player

            else:
                place = minimax(state, computer)
                state[place] = computer

            printboard(state)
            turn += 1
