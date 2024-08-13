# A 2D LIST IS BASICALLY LISTS INSIDE A LIST

number_grid=[

    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(number_grid[0])

print(number_grid[0][2]) # for accessing specific element inside the first list

for row in number_grid:
    print(row)
    for col in row:     # a for loop inside a for loop is called a nested loop
        print(col)