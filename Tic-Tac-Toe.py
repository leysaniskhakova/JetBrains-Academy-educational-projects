def print_cells(cells):
	print(f'''---------
| {' '.join(cells[:3])} |
| {' '.join(cells[3:6])} |
| {' '.join(cells[6:])} |
---------''')

cells = [' ' for i in range(9)]
print_cells(cells)

voc_coordinates = {}
for ind in range(len(cells)):
	list_coordinates = []
	for i in range(3, 0, -1):
		for j in range(1, 4):
			coordinate = j, i
			list_coordinates.append(coordinate)
	voc_coordinates[list_coordinates[ind]] = [ind, cells[ind]]

def combinations(cells):
	return [cells[0] + cells[1] + cells[2],
			cells[3] + cells[4] + cells[5],
			cells[6] + cells[7] + cells[8],
			cells[0] + cells[3] + cells[6],
			cells[1] + cells[4] + cells[7],
			cells[2] + cells[5] + cells[8],
			cells[0] + cells[4] + cells[8],
			cells[2] + cells[4] + cells[6]]

state = 'play'
def wins(state):
	for line in combinations_of_cells:
		if line == 'XXX':
			state = 'X wins'
		elif line == 'OOO':
			state = 'O wins'
	return state

value_cells = 'O'
def change_cells(value_cells):
	if value_cells == 'X':
		voc_coordinates[coordinates][1] = 'O'
		cells[voc_coordinates[coordinates][0]] = 'O'
		value_cells = 'O'
	elif value_cells == 'O':
		voc_coordinates[coordinates][1] = 'X'
		cells[voc_coordinates[coordinates][0]] = 'X'
		value_cells = 'X'
	return value_cells

while True:
	input_coordinates = input('Enter the coordinates: ').split()
	try:
		coordinates = tuple(map(int, input_coordinates))
		if coordinates not in voc_coordinates.keys():
			print('Coordinates should be from 1 to 3!')
		elif voc_coordinates[coordinates][1] != ' ':
			print("This cell is occupied! Choose another one!")
		elif voc_coordinates[coordinates][1] == ' ':
			value_cells = change_cells(value_cells)
			print_cells(cells)
			combinations_of_cells = combinations(cells)
			state = wins(state)
			if state == 'X wins' or state == 'O wins':
				print(state)
				break
			elif ' ' not in cells:
				print('Draw')
				break
	except ValueError:
		print('You should enter numbers!')