teams = [
    ('Team Blue',[25,32,30]), 
    ('Team Red',[18,27,28]), 
    ('Team Yellow', [30,25,26])
]

ranking = []

for team, scores in teams:
    average = sum(scores) / len(scores)
    ranking.append((team, average))

ranking.sort(reverse=True)

print('Final Ranking')

for i, (team, average) in enumerate(ranking, 1):
    print(f'{i}- {team}: {average:.2f}')