import math
from random import uniform

# Constants
# -----------------------------

DIST_MIN = 20      # in meters
DIST_MAX = 100
ANGLE_MIN = 0      # in degrees
ANGLE_MAX = 15

# Functions
# -----------------------------

def distance():
	# Returns a random distance between a min and max range
	return uniform(DIST_MIN, DIST_MAX)

def distance_from_normal(L):
	# Returns a random distance from the normal between a min and max angle
	theta = math.radians(uniform(ANGLE_MIN, ANGLE_MAX))
	return L * math.tan(theta)

def generate_positions(N):
	# Returns a list of N positions in tuples of the form: (label, distance, distance_from_normal)
	positions = []
	for i in range(N):
		L = distance()
		x = distance_from_normal(L)
		label = 'Photo ' + str(i + 1)
		positions.append(
			[label, L, x]
		)
	return positions

def sort_positions(positions):
	# Sorts a list of positions by their distances
	return sorted(positions, key=lambda x: x[1])

def generate_individuals(M, N):
	# Returns a list of position lists for M individuals (where each positions list is of size N)
	individuals = []
	for i in range(M):
		P = generate_positions(N)
		P = sort_positions(P)
		label = 'Individual ' + str(i + 1)
		individuals.append(
			[label, P]
		)
	return individuals

def generate_csv(filename, M, N):
	# Generates a CSV given a filename, a number of individuals (M) and a number of positions per individual (N)
	with open(filename, 'w') as csv:
		individuals = generate_individuals(M, N)
		for i in range(len(individuals)):
			for j in range(len(individuals[i])):
				if j < 1:
					csv.write(str(individuals[i][j]) + '\n')
				else:
					for k in range(len(individuals[i][j])):
						for l in range(len(individuals[i][j][k])):
							csv.write(str(individuals[i][j][k][l]) + ', ')
						csv.write('\n')

# Start the show...
# -----------------------------

if __name__ == '__main__':
	# Run the main scripts
	# generate_csv('possum_model.csv', 5, 10)
	# generate_csv('cat_model.csv', 5, 10)
	# generate_csv('sheep_model.csv', 5, 10)
	# generate_csv('cow_model.csv', 5, 10)
	# generate_csv('fox_model.csv', 5, 10)
	generate_csv('new_lamb.csv', 10, 10)




