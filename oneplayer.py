from random import randint, shuffle

def checkstatus(state):

    '''
    finds the status of the game, returns 'X', 'O', 'D' if there is a result and None otherwise
    '''

    # all possible winning combinations
    wincombo = [set([1, 2, 3]), set([4, 5, 6]), set([7, 8, 9]), set([1, 4, 7]), set([2, 5, 8]), set([3, 6, 9]), set([1, 5, 9]), set([3, 5, 7])]

    # find where all Xs and Os are
    x = set()
    o = set()
    for i in range(1, 10):
        if state[i] == 'X':
            x.add(i)
        if state[i] == 'O':
            o.add(i)

    # use subset to find if there is a winner
    for combo in wincombo:
        if combo.issubset(x):
            return 'X'
        if combo.issubset(o):
            return 'O'
    
    # full board but no result means draw
    if '.' not in state:
        return 'D'
    
    # game not over
    return None

def generatemoves(state):

    '''
    generates all possible moves of the position
    '''

    # any empty space is a possible move
    moves = []
    for i in range(1, 10):
        if state[i] == '.':
            moves.append(i)

    # shuffle moves so game is different every time
    shuffle(moves)
    return moves

def minimax(state, ismax):

    '''
    minimax algorithm implementation for playing tic tac toe
    '''

    # end algorithm
    status = checkstatus(state)
    if status == 'X':
        return -10
    elif status == 'O':
        return 10
    elif status == 'D':
        return 0
    
    moves = generatemoves(state)

    # maximising player
    if ismax:
        eval = -float('inf')

        for move in moves:
            temp = state.copy()
            temp[move] = 'O'
            eval = max(eval, minimax(temp, False))

        return eval
    
    # minimising player
    else: 
        eval = float('inf')

        for move in moves:
            temp = state.copy()
            temp[move] = 'X'
            eval = min(eval, minimax(temp, True))

        return eval

def best_move(state):

    '''
    finds best move of the position
    '''

    eval = -float('inf')
    best = None

    # finds all possible moves
    moves = generatemoves(state)

    for move in moves:
        temp = state.copy()
        temp[move] = 'O'

        # uses minimax algorithm to find which is best
        curr = minimax(temp, False)

        if curr > eval:
            eval = curr
            best = move

    return best

def printboard(state, invert):

    '''
    prints out the current game board
    '''

    # regular board
    if invert == 1:
        print(f'{state[1]} | {state[2]} | {state[3]}')
        print('- - - - -')
        print(f'{state[4]} | {state[5]} | {state[6]}')
        print('- - - - -')
        print(f'{state[7]} | {state[8]} | {state[9]}')

    # inverted board
    else:
        invertstate = []
        for i in state:
            if i == None:
                invertstate.append(None)
            elif i == 'X':
                invertstate.append('O')
            elif i == 'O':
                invertstate.append('X')
            else:
                invertstate.append('.')

        print(f'{invertstate[1]} | {invertstate[2]} | {invertstate[3]}')
        print('- - - - -')
        print(f'{invertstate[4]} | {invertstate[5]} | {invertstate[6]}')
        print('- - - - -')
        print(f'{invertstate[7]} | {invertstate[8]} | {invertstate[9]}')

def oneplayer():
    
    '''
    play tic tac toe against a bot
    '''

    # initialise game
    state = [None, '.', '.', '.', '.', '.', '.', '.', '.', '.']
    turn = 0

    printboard(state, 1)
    rand1 = randint(1, 2)
    rand2 = randint(1, 2)

    while True:
        
        # check for game end
        status = checkstatus(state)

        if status == 'X':
            print('You Win') # lolololol surely this will happen
            return

        if status == 'O':
            print('You Lose')
            return

        if status == 'D':
            print('Draw')
            return

        if status == None:

            # player turn, random so player can play first or second
            if (turn + rand1) % 2 == 0:

                while True:
                    place = int(input("Your Turn: "))

                    if state[place] == '.':
                        break
                    else:
                        print('Invalid Move')

                state[place] = 'X'

            # computer turn
            else:
                print("Computer's Turn")
                place = best_move(state)
                state[place] = 'O'

            # can also print inverted board so player can play as both X and O
            printboard(state, rand2)
            turn += 1

oneplayer()