candidates = {'Candidate A':0, 'Candidate B':0}

while True:
    print('Insert 1 for Candidate A or insert 2 for Candidate B!')
    print('Insert 0 for end the voting!')
    print('-'*30)


    vote = int(input('Insert your vote: '))

    if vote == 1:
        candidates['Candidate A'] += 1
    elif vote == 2:
        candidates['Candidate B'] += 1
    elif vote == 0:
        print('Voting ended!')
        break
    else:
        print('Insert a valid option!')
        print('-'*30)
        continue


print(candidates)