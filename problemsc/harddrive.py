__author__ = 'Антон Брагин'

def get_number_of_rounds(blocks):
    block_coords = {}
    for coord, block in enumerate(blocks):
        block_coords[block] = coord
    head = -1
    rounds = 0
    for i in range(len(blocks)):
        move = block_coords[i + 1]
        if move < head:
            rounds += 1
        head = move
    return rounds

if __name__ == '__main__':
    with open('harddrive.in') as f:
        n = int(f.readline())
        blocks = [int(x) for x in f.readline().split()]
    rounds = get_number_of_rounds(blocks)
    with open('harddrive.out', 'w') as f:
        f.write(str(rounds))
