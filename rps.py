import random

ps = 0
ss = 0
set1 = ('rock', 'paper', 'scissor')
# set2 = ('r', 'p', 's')

while True:

    # user input

    u = str(input('your choice: '))

    if u not in set1:
        print('input error')
        print('~~~~~~~~~~~~~~~~~~~~~~')
        continue

    # print('you chose:', u)

    # computer choice

    r = random.choice(set1)
    print('computer chose:', r)

    # win(r s , p r , s p)

    if (u == 'rock' and r == 'scissor') or (u == 'paper' and r == 'rock') or (u == 'scissor' and r == 'paper'):
        print('** you won **')
        ps += 1

    # lose(r p , p s , s r)

    elif (u == 'rock' and r == 'paper') or (u == 'paper' and r == 'scissor') or (u == 'scissor' and r == 'rock'):
        print('** you lost **')
        ss += 1

    else:
        print('** draw **')

    # output

    print('player score:', ps)
    print('computer score:', ss)
    print('~~~~~~~~~~~~~~~~~~~~~~')
