from time import perf_counter
from sudokuSolver import *


if __name__ == "__main__":

    easy = [["-","-","-",8,"-",5,"-",1,3],
         ["-","-","-",2,"-",3,6,"-","-"],
         [6,"-","-","-",9,"-",2,"-",4],
         ["-","-","-","-","-","-","-","-",5],
         ["-",4,"-",1,"-","-",7,"-",6],
         [2,5,6,3,"-",4,8,9,"-"],
         [5,9,"-","-","-",7,1,"-",2],
         [1,"-",2,"-",8,"-",4,7,"-"],
         ["-","-",4,9,1,"-","-",3,8]]

    hard = [[6,"-","-","-",8,"-","-",5,"-"],
            ["-","-",9,"-","-",6,"-",1,"-"],
            ["-","-","-",9,"-",2,"-","-","-"],
            [9,"-","-","-","-","-","-","-",2],
            [3,"-","-","-",1,"-","-","-",7],
            ["-","-",8,7,2,"-","-","-",4],
            ["-","-","-","-","-","-","-","-","-"],
            [8,"-","-","-",7,"-","-",3,"-"],
            ["-",4,"-","-",6,"-","-","-",1]]

    expert = [[3,"-","-","-","-","-","-",2,"-"],
            ["-","-","-","-","-","-",9,6,4],
            [2,"-",8,"-","-","-","-",5,"-"],
            [1,7,"-","-",8,"-","-","-","-"],
            ["-","-","-",2,"-","-","-","-",7],
            ["-","-","-","-",5,"-",4,"-","-"],
            ["-","-",9,"-","-","-","-","-","-"],
            ["-","-",6,"-","-",4,"-","-",5],
            ["-",2,"-",9,"-",6,"-","-","-"]]

    extreme = [["-",1,"-","-","-","-","-","-","-"],
            ["-","-",2,"-","-","-","-","-","-"],
            ["-","-","-",3,"-","-","-","-","-"],
            [1,"-","-","-",4,"-","-","-","-"],
            ["-",7,"-","-","-",5,"-","-","-"],
            ["-","-",8,"-","-","-",6,"-","-"],
            ["-","-","-",4,"-","-","-",1,"-"],
            ["-","-","-","-","-","-","-","-","-"],
            [9,"-",7,"-","-","-","-","-","-"]]

    starteasy = perf_counter()
    # Easy Category Sudoku
    print("Easy Category Sudoku")
    printBoard(easy)
    solve(easy)
    printBoard(easy)
    easytime = perf_counter()
    print('Solved in: %s seconds' % (easytime - starteasy))
    print()

    starthard = perf_counter()
    # Hard Category Sudoku
    print("Hard Category Sudoku")
    printBoard(hard)
    solve(hard)
    printBoard(hard)
    hardtime = perf_counter()
    print("Solved in: %s seconds" % (hardtime - starthard))
    print()

    expertstart = perf_counter()
    # Expert Category Sudoku
    print("Expert Category Sudoku")
    printBoard(expert)
    solve(expert)
    printBoard(expert)
    expertime = perf_counter()
    print("Solved in: %s seconds" % (expertime - expertstart))
    print()

    extremestart = perf_counter()
    # Expert Category Sudoku
    print("Extreme Category Sudoku")
    printBoard(extreme)
    solve(extreme)
    printBoard(extreme)
    extremetime = perf_counter()
    print("Solved in: %s seconds" % (extremetime - extremestart))
    print()