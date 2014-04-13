__author__ = 'Антон Брагин'

def generate_next(permutation):
    #Find maximum decreasing suffix
    current_max = permutation[-1]
    max_decreasing_suffix = len(permutation) - 1
    for i in range(len(permutation)):
        current = permutation[len(permutation) - i - 2]
        if current > current_max:
            current_max = current
            max_decreasing_suffix = len(permutation) - i - 2
        else:
            break

    if max_decreasing_suffix == 0:
        return None

    prefix = permutation[:max_decreasing_suffix - 1]

    element = max(permutation[max_decreasing_suffix:])
    for x in permutation[max_decreasing_suffix:]:
        if x > permutation[max_decreasing_suffix - 1] and x < element:
            element = x

    suffix = permutation[max_decreasing_suffix:]
    suffix.remove(element)
    suffix.append(permutation[max_decreasing_suffix - 1])

    return prefix + [element] + sorted(suffix)

def generate_previous(permutation):
    #Find maximum increasing suffix
    current_min = permutation[-1]
    max_increasing_suffix = len(permutation) - 1
    for i in range(len(permutation)):
        current = permutation[len(permutation) - i - 2]
        if current < current_min:
            current_min = current
            max_increasing_suffix = len(permutation) - i - 2
        else:
            break

    if max_increasing_suffix == 0:
        return None

    prefix = permutation[:max_increasing_suffix - 1]

    element = min(permutation[max_increasing_suffix:])
    for x in permutation[max_increasing_suffix:]:
        if x < permutation[max_increasing_suffix - 1] and x > element:
            element = x

    suffix = permutation[max_increasing_suffix:]
    suffix.remove(element)
    suffix.append(permutation[max_increasing_suffix - 1])

    return prefix + [element] + sorted(suffix, reverse=True)

if __name__ == '__main__':
    #Read input
    with open('nextperm.in') as f:
        n = int(f.readline().strip())
        permutation = [int(x) for x in f.readline().split()]

    previous = generate_previous(permutation)
    if previous is None:
        previous = [0] * len(permutation)
    next = generate_next(permutation)
    if next is None:
        next = [0] * len(permutation)

    with open('nextperm.out', 'w') as f:
        f.write(' '.join(str(x) for x in previous))
        f.write('\n')
        f.write(' '.join(str(x) for x in next))
        f.write('\n')