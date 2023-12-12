def find_snake_location(path):
    x, y = 0, 0  # Initial position
    snake_locations = []

    for move in path:
        if move == '^':
            y += 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == 'v':
            y -= 1
        elif move == 'x':
            snake_locations.append((x, y))

    if not snake_locations:
        return 'Not Found'
    else:
        return snake_locations

path = input("Path: ")
locations = find_snake_location(path)
    
if locations != 'Not Found':
    new_tup = ' '.join([str(tuple(map(int, i))) for i in locations])
    print("Locations:",new_tup)
else:
    print(locations)
print()
