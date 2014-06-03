__author__ = 'Антон Брагин'

def generate_next(n, k, choose):
    for i in range(k):
        if choose[len(choose) - i - 1] < n - i:
            choose[len(choose) - i - 1] += 1
            for j in range(len(choose) - i, len(choose)):
                choose[j] = choose[j - 1] + 1
            return choose
    return None

if __name__ == '__main__':

    with open('nextchoose.in') as f:
        n, k = [int(x) for x in f.readline().split()]
        choose = [int(x) for x in f.readline().split()]

    next = generate_next(n, k, choose)

    with open('nextchoose.out', 'w') as f:
        if next is None:
            f.write('-1')
        else:
            f.write(' '.join(str(x) for x in next))
        f.write('\n')
