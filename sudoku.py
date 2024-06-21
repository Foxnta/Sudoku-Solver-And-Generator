import random
import copy

def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("--" * 11)
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(cell, end=" ")
        print()
    print()

def is_still_valid(matrix):
  def validate_row(matrix):
  #rows
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        data = matrix[row][col]
        if(data !=0 and data in matrix[row][col+1:]):
          return False
    return True

  #cols
  col_data = []
  for i in range(len(matrix)):
    row_data = []
    for j in range(len(matrix)):
      row_data.append(matrix[j][i])
    col_data.append(row_data)

    #sections
    
    secciones  = [
        [(0, 3), (0, 3)], [(0, 3), (3, 6)], [(0, 3), (6, 9)],
        [(3, 6), (0, 3)], [(3, 6), (3, 6)], [(3, 6), (6, 9)],
        [(6, 9), (0, 3)], [(6, 9), (3, 6)], [(6, 9), (6, 9)]
    ]

    matrizdesecciones =[]
    for seccion in secciones:
        lista = []
        for row in range(seccion[0][0],seccion[0][1]):
            for col in range(seccion[1][0],seccion[1][1]):
                lista.append(matrix[row][col])
        matrizdesecciones.append(lista)
        
  return validate_row(matrix) and validate_row(col_data) and validate_row(matrizdesecciones)


def fill_matrix(n, matrix, visited, numofsolution=float('inf'), row=0, col=0, states = 0, solutions = 0, sudokus=[]):
  if(row == n):
    sudokus.append([row[:] for row in matrix])
    return states, solutions+1, sudokus
  
  for idx, op in enumerate(range(1, n+1)):
    visited = [False] * n
    if(not visited[idx]):
      visited[idx] = True #marqué como visitado
      matrix[row][col] = op #componiendo solución
      next_col = (col + 1) % n
      next_row = row + (col + 1) // n
      if(solutions < numofsolution):
        if(is_still_valid(matrix)):
            states, solutions, sudokus = fill_matrix(n, matrix, visited, numofsolution, next_row, next_col, states+1, solutions, sudokus)
        visited[idx] = False #desmarcar como visitado
        matrix[row][col] = 0 #descomponiendo solución
  return states, solutions, sudokus



def find_matrix(n, matrix, visited, row=0, col=0, states = 0, solutions = 0, sudokus=[]):
  if(row == n):
    sudokus.append([row[:] for row in matrix])
    return states, solutions+1, sudokus
  for idx, op in enumerate(range(1, n+1)):
    visited = [False] * n
    if(not visited[idx]):
      visited[idx] = True #marqué como visitado
      if matrix[row][col]==0:
        matrix[row][col] = op #componiendo solución
      next_col = (col + 1) % n
      next_row = row + (col + 1) // n    
      if(solutions!=1):
        if(is_still_valid(matrix)):
            states, solutions, sudokus = find_matrix(n, matrix, visited, next_row, next_col, states+1, solutions, sudokus)
        visited[idx] = False #desmarcar como visitado
        matrix[row][col] = 0 #descomponiendo solución
  return states, solutions, sudokus



def generar_juego():
    n = 9
    visited = [False] * 9
    matrix = [[0]*n for _ in range(n)]
    result = fill_matrix(n, matrix, visited, 10)
    # print(result)
    return random.choice(result[2])

def buscar_solucion(m):
    n = 9
    visited = [False] * 9
    result = find_matrix(n, m, visited)
    return result[2][0]

def hide_number(m, n):
    nm = [row[:] for row in m]
    numeros_cambiados = 0

    while(n!=numeros_cambiados):
        for i in range(len(m)):
            if numeros_cambiados == n:
                        break
            for j in range(len(m)):
                if random.random() < 0.2 and nm[i][j] != 0:
                    nm[i][j] = 0
                    numeros_cambiados += 1
                    if numeros_cambiados == n:
                        break
    return nm

def entregar_pista(m_user, m_solucion):
    position = None
    for row in range(len(m_user)):
        if position != None:
            break
        for col in range(len(m_user)):
            if m_user[row][col]==0:
                position = (row, col)
                m_user[row][col]=m_solucion[row][col]
                break
    return m_user
    
def pedir_matriz():
    entrada =  input('Escriba el sudoku: ')
    entrada = entrada.replace(" ", "")
    if entrada.startswith("[[") and entrada.endswith("]]"):
        entrada = entrada[2:-2]
        entrada_str = entrada.split("],[")
        sudoku = []
        for i in entrada_str:
            numeros_str = i.split(',')
            numeros = [int(numero) for numero in numeros_str]
            sudoku.append(numeros)
        return sudoku
    else:
        print("sudoku invalido")
        return []

def run():
    menu_principal = True
    while menu_principal:
        print("Menu:")
        print("1. Nuevo juego")
        print("2. Traigo un Sudoku")
        print("3. Fin del juego")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            valor=30
            solucion = generar_juego()
            print("Selecciona el nivel de dificultad:")
            print("1. Fácil")
            print("2. Medio")
            print("3. Difícil")
            eleccion = input("Ingresa el número correspondiente al nivel: ")
            if eleccion == "1":
                valor = 15
            elif eleccion == "2":
                valor = 30
            elif eleccion == "3":
                valor = 40
            hide_sudoku = hide_number(solucion, valor)
            

            juego_en_curso = True
            while juego_en_curso:
                print_sudoku(hide_sudoku)
                print("Juego en curso:")
                print("1. Pedir pista")
                print("2. ver solucion")
                print("3. Volver al menú anterior")
                print("4. Fin del juego")

                opcion_juego = input("Seleccione una opción (1/2/3): ")

                if opcion_juego == '1':
                    entregar_pista(hide_sudoku,solucion)
                elif opcion_juego == '2':
                    print_sudoku(solucion)
                    juego_en_curso = False
                elif opcion_juego == '3':
                    juego_en_curso = False
                elif opcion_juego == '4':
                    print("Fin del juego")
                    juego_en_curso = False
                    menu_principal = False
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == '2':
            sudoku_en_curso = True
            sudoku = []
            while sudoku_en_curso:
                if not sudoku:
                    sudoku = pedir_matriz()
                if sudoku:    
                    original_sudoku = copy.deepcopy(sudoku)
                    if is_still_valid(sudoku):
                        solucion = buscar_solucion(sudoku)
                        print('---Sudoku---')
                        print_sudoku(original_sudoku)
                        print("1. Pedir pista")
                        print("2. ver solucion")
                        print("3. Volver al menú anterior")
                        print("4. Fin del juego")
                        opcion = input("Seleccione una opción (1/2/3): ")
                        if opcion == '1':
                            sudoku = entregar_pista(original_sudoku,solucion)
                        elif opcion == '2':
                            print_sudoku(solucion)
                            sudoku_en_curso = False
                        elif opcion == '3':
                            sudoku_en_curso = False
                        elif opcion == '4':
                            print("Fin del juego")
                            sudoku_en_curso = False
                            menu_principal = False
                        else:
                            print("Opción no válida. Intente de nuevo.")
                    else:
                        print('el sudoku no tiene solucion')
                        sudoku_en_curso = False
                else:
                    menu_principal = False

        elif opcion == '3':
            print("Fin del juego")
            menu_principal = False
        else:
            print("Opción no válida. Intente de nuevo.")


# if you want to solve your sudoku, you can use this example for the input:
#[[0, 2, 3, 0, 5, 0, 7, 8, 9], [4, 5, 6, 0, 8, 9, 0, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6], [0, 0, 4, 0, 6, 0, 8, 9, 7], [3, 0, 5, 8, 9, 0, 2, 1, 4], [0, 9, 0, 2, 1, 4, 3, 6, 5], [5, 0, 1, 6, 4, 2, 9, 7, 8], [0, 4, 2, 0, 7, 8, 6, 3, 0], [6, 7, 0, 9, 0, 1, 0, 0, 2]]


if __name__ == "__main__":
    run()
