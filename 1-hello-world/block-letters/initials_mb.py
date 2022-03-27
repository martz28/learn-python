# Slightly ridiculous coding for the intials exercise.


list_M = [
        ['M',' ', ' ', ' ', 'M'],
        ['M','M', ' ', 'M', 'M'],
        ['M','M', ' ', 'M', 'M'],
        ['M',' ', 'M', ' ', 'M'],
        ['M',' ', ' ', ' ', 'M'],
        ['M',' ', ' ', ' ', 'M'],
        ['M',' ', ' ', ' ', 'M']
        ]
        
list_B = [
        ['B','B', 'B', 'B', ' '],
        ['B',' ', ' ', ' ', 'B'],
        ['B',' ', ' ', ' ', 'B'],
        ['B','B', 'B', 'B', ' '],
        ['B',' ', ' ', ' ', 'B'],
        ['B',' ', ' ', ' ', 'B'],
        ['B','B', 'B', 'B', ' ']
        ]
  
row_len = len(list_M)

matrix_row = 0
matrix_column = 0

while matrix_row <= 6:
  matrix_column = 0
  while matrix_column <=4:

    print(list_M[matrix_row][matrix_column], sep='',end='')

    matrix_column +=1
    if matrix_column == 5:
      matrix_column = 0
      print('    ', sep='',end='')
      while matrix_column <=4:
        print(list_B[matrix_row][matrix_column], sep='',end='')
        matrix_column +=1

  print()
  matrix_row += 1
