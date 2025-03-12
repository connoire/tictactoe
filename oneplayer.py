from random import randint

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

def minimax(state, depth, ismax):

    status = checkwin(state)
    if status == 'X':
        return -10 + depth
    elif status == 'O':
        return 10 - depth
    elif depth == 9:
        return 0
    
    moves = generatemoves(state)

    if ismax:
        eval = -float('inf')

        for move in moves:
            temp = state.copy()
            temp[move] = 'O'
            eval = max(eval, minimax(temp, depth + 1, False))

        return eval
    
    else: 
        eval = float('inf')

        for move in moves:
            temp = state.copy()
            temp[move] = 'X'
            eval = min(eval, minimax(temp, depth + 1, True))

        return eval

def best_move(state):

    eval = -float('inf')
    best = None
    moves = generatemoves(state)

    for move in moves:
        temp = state.copy()
        temp[move] = 'O'
        curr = minimax(temp, 0, False)

        if curr > eval:
            eval = curr
            best = move

    return best

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

    printboard(state)

    while True:
        
        status = checkwin(state)

        if status == 'X':
            print('You Win') # lolololol surely this will happen
            return

        if status == 'O':
            print('You Lose')
            return

        if turn == 9:
            print('Draw')
            return

        if status == None:

            if (turn + rand) % 2 == 0:
                place = int(input("Your Turn: "))
                state[place] = 'X'

            else:
                print("Computer's Turn")
                place = best_move(state)
                state[place] = 'O'

            printboard(state)
            turn += 1

oneplayer()