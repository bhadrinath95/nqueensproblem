from django.shortcuts import render
from .forms import BoardForm
from .models import Board


# Create your views here.
def home(request):
    title = "N Queens Problem"
    form = BoardForm(request.POST or None)
    if form.is_valid():
        bd = form.save(commit=False)
        bd.save()
        obj = Board.objects.all().first()
        N = bd.board_size
        cellsize = 640/bd.board_size
        fontsize = 400/N
        board = solveNQ(N)
        context = {
            "form": form,
            "title":title,
            "cellsize":cellsize,
            "fontsize":fontsize,
            "board":board,
            }
        return render(request, "home.html", context)
        
    N = 8
    cellsize = 640/N
    fontsize = 400/N
    board = [ [ 0 for i in range(N) ] for j in range(N) ]
    context = {
            "form": form,
            "title":title,
            "cellsize":cellsize,
            "fontsize":fontsize,
            "board":board,
            }
    
    
    return render(request, "home.html", context)

def solveNQ(N): 
    
    board = [ [ 0 for i in range(N) ] for j in range(N) ]

    if solveNQUtil(N, board, 0) == False: 
        print ("Solution does not exist") 
        return board

    printSolution(N, board) 
    return board

def solveNQUtil(N, board, col): 
    
    # base case: If all queens are placed 
    # then return true 
    if col >= N: 
        return True

    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(N): 

        if isSafe(N, board, i, col): 
            
            # Place this queen in board[i][col] 
            board[i][col] = 1

            # recur to place rest of the queens 
            if solveNQUtil(N, board, col + 1) == True: 
                return True

            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0

    # if the queen can not be placed in any row in 
    # this colum col then return false 
    return False

def isSafe(N, board, row, col): 

    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False

    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False

    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False

    return True

def printSolution(N, board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 