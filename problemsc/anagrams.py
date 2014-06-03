import time

__author__ = 'Антон Брагин'

vovels = set(['a', 'e', 'i', 'o', 'u', 'y'])
anagrams = []
printed = set()

def create_anagrams(prefix, alphabet):
    if not alphabet:
        word = ''.join(prefix)
        if word not in printed:
            anagrams.append(word)
            printed.add(word)
        return

    index = len(prefix) - len(alphabet)

    for i, letter in enumerate(alphabet):
        if index == 0 or letter not in vovels or prefix[index - 1] not in vovels:
            prefix[index] = letter
            create_anagrams(prefix, alphabet[:i] + alphabet[i + 1:])

def run():
    #Execution
    time_start = time.time()

    with open('anagrams.in') as f:
        word = f.readline().strip()
        alphabet = sorted(list(word))

    prefix = [None for _ in range(len(alphabet))]

    create_anagrams(prefix, alphabet)

    with open('anagrams.out', 'w') as f:
        f.write('\n'.join(anagrams))

    time_elapsed = time.time() - time_start
    print('Elapsed time: {}, anagrams: {}'.format(time_elapsed, len(anagrams)))

if __name__ == '__main__':
    run()




