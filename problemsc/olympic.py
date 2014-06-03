__author__ = 'Антон Брагин'

from operator import itemgetter

def get_medals(stand):
    competitors = {}
    for competition in stand:
        for i, competitor in enumerate(competition):
            if competitor not in competitors:
                competitors[competitor] = [0, 0, 0, competitor]
            competitors[competitor][i] += 1
    return competitors

def get_winner(stand):
    competitors = get_medals(stand)
    #Sort by names
    winners = sorted(list(competitors.values()), key=itemgetter(3))
    #Sort by medals in reverse order. Since sorting is stable name order is preserved
    winners = sorted(winners, key=itemgetter(0, 1, 2), reverse=True)
    return winners[0][3]

if __name__ == '__main__':
    with open('olympic.in') as f:
        n = int(f.readline())
        stand = []
        for line in f:
            stand.append(line.split())
        winner = get_winner(stand)
    with open('olympic.out', 'w') as f:
        f.write(winner)

