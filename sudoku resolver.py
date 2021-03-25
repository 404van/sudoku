board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):	#imprime por pantalla el tablero
	for i in range (9):
		if i % 3 == 0 and i != 0:
				print("---------------------------")
		for j in range(9):
			if j % 3 == 0 and j!= 0:
				print(" | ", end=" ")
				print(bo[i][j], end=" ")
			elif j == 8:
				print(bo[i][j])
			else:(print(bo[i][j] , end=" "))
			
			

def encontrar_lugar(bo):	#encuentra un lugar con un cero y devuelvo fila, columna y numero
	for i in range (9):
		for j in range (9):
			if bo[i][j] == 0:
				return(i,j,bo[i][j])

def atempt_digits(bo,fila,columna):	#esto no anda
	for i in range (1,9):
		if i not in bo[fila]:
			for j in range (9):
				if i not in bo[fila][columna]:
					bo[fila][columna] = i 
	return(bo)

def main():
	vacio = encontrar_lugar(board)
	print(vacio)
	atempt_digits(board, vacio[1], vacio[2])



main()