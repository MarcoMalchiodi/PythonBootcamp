grid = " 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9 "
# [1] [5] [9] 
# [26] [30] [34] 
# [51] [55] [59]
print(grid)
player_turn = 0
game_on = True

def check_winner(player,current_grid):
    global game_on
    grid = current_grid
    
    if grid[1]==grid[5] and grid[5]==grid[9]:
        print(f"{player} won!")
        game_on = False
    elif grid[26]==grid[30] and grid[30]==grid[34]:
        print(f"{player} won!")
        game_on = False
    elif grid[51]==grid[55] and grid[55]==grid[59]:
        print(f"{player} won!")
        game_on = False
    elif grid[1]==grid[26] and grid[26]==grid[51]:
        print(f"{player} won!")
        game_on = False
    elif grid[5]==grid[30] and grid[30]==grid[34]:
        print(f"{player} won!")
        game_on = False
    elif grid[9]==grid[34] and grid[34]==grid[59]:
        print(f"{player} won!")
        game_on = False
    elif grid[1]==grid[30] and grid[30]==grid[59]:
        print(f"{player} won!")
        game_on = False
    elif grid[9]==grid[30] and grid[30]==grid[51]:
        print(f"{player} won!")
        game_on = False
    else:
        pass


while game_on:
    
    if player_turn == 0:
        print("Player 1: ")
        player_choice = str(input("Enter a position: "))
        if player_choice in grid:
            grid = grid.replace(player_choice,"X")
            print(grid)
            check_winner(player='Player 1',current_grid=grid)
            if game_on==False:
                break
            player_turn = 1
        else:
            print('please, insert a valid character')
    
    if player_turn == 1:
        print("Player 2: ")
        player_choice = str(input("Enter a position: "))
        if player_choice in grid:
            grid = grid.replace(player_choice,"O")
            print(grid)
            check_winner(player='Player 2',current_grid=grid)
            player_turn = 0
        else:
            print('please, insert a valid character')