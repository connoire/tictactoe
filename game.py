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


def printboard(state):

    print(f'{state[1]} | {state[2]} | {state[3]}')
    print('- - - - -')
    print(f'{state[4]} | {state[5]} | {state[6]}')
    print('- - - - -')
    print(f'{state[7]} | {state[8]} | {state[9]}')


def play():

    state = [None, '.', '.', '.', '.', '.', '.', '.', '.', '.']
    turn = 0
    printboard(state)

    while True:
        
        status = checkwin(state)

        if status == 'X':
            print('Player X Wins')
            return

        if status == 'O':
            print('Player O wins')
            return

        if turn == 9:
            print('Draw')
            return

        if status == None:

            if turn % 2 == 0:
                place = int(input("Player X's Turn: "))
                state[place] = 'X'

            else:
                place = int(input("Player O's Turn: "))
                state[place] = 'O'

            printboard(state)
            turn += 1


play()