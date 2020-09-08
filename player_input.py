def player_input():
    marker = ''
    
    while not(marker=='X' or marker=='O'):
        marker=input('Player1: Please select X or O:').upper()
        
        if marker=='X':
            return ('X','O')
        else:
            return ('O','X')
player_input()