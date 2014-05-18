__author__ = 'Антон Брагин'

def calculate_fuel(plane_mass, alpha):
    if 1000 - alpha <= 0:
        return None
    else:
        return alpha * plane_mass / (1000 - alpha)

if __name__ == '__main__':
    with open('airplane.in') as f:
        plane, num_pass, alpha = [float(x) for x in f.readline().split()]
        passengers = [float(x) for x in f.readline().split()]

    fuel = calculate_fuel(plane + sum(passengers), alpha)

    with open('airplane.out', 'w') as f:
        if fuel:
            f.write(str(fuel))
        else:
            f.write('Impossible')