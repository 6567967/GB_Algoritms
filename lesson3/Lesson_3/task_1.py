a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a, b, sep='\n')

a = [1, 2, 3]
b = a
a += [4, 5]     # a.extend([4, 5])
print(a, b, sep='\n')

# 2
row = [' '] * 3
print(row)
board = [row] * 3
print(board)
board[0][0] = 'X'
row[1] = 'O'
print(board)

board = [[' '] * 3 for _ in range(3)]
board[0][0] = 'X'
print(board)

# 3
tup = ('one', 'two')
for item in tup:
    print(item)

tup = ('one', )
for item in tup:
    print(item)
print(type(tup))


