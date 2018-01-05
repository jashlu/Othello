#Joshua Lu
#60343957
#Project 4 Console 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            
        
class Gamestate:

    def __init__(self, choice, dimensions, winner, board):
        '''The initial game board'''
        if choice == 'B':
            self._gamestate = 1
        elif choice == 'W':
            self._gamestate = 2
        self._row = dimensions[0]       
        self._column = dimensions[1]       
        self._winner = winner      
        self._board = board
        self._b_count = 0
        self._w_count = 0
        self._initial_check = True
        self._drop_piece_input = []
        self._interesting_pieces = []
        self._playable = True

#Find out whose turn it is.

    def current_player(self):
        '''signals which player's turn it is at the moment'''
        if self._initial_check == True:
            if self._gamestate == 1:
                return 1
            
            if self._gamestate == 2:
                return 2
        else:
            return
    
    def next_player(self):
        '''alternates between black and white characters'''
        if self._gamestate == 1:
            self._gamestate = 2
            return self._gamestate
        else:
            self._gamestate = 1
            return self._gamestate

            
    def count_pieces(self):
        '''count number of pieces each side has'''
        big_list = []
        b_count = []
        for sublist in self._board:
            for x in sublist:
                if x == 'B':
                    b_count.append(x)
            w_count = []
            for sublist in self._board:
                for x in sublist:
                    if x == 'W':
                        w_count.append(x)

        self._b_count = len(b_count)
        self._w_count = len(w_count)
        big_list.append(self._b_count)
        big_list.append(self._w_count)
        return big_list

        
    def drop_piece(self, coordinate):
        ''' check if you can drop a piece, and if you can, drop the piece, given
        inpute coordinates'''
        self._drop_piece_input = coordinate
        if self._gamestate == 1:
           self._board[int(self._drop_piece_input[0])-1][int(self._drop_piece_input[1])-1] = 'B'
           return self._board
    
        elif self._gamestate == 2:
            self._board[int(self._drop_piece_input[0])-1][int(self._drop_piece_input[1])-1] = 'W'
            return self._board

# CHECKS
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    def check_up(self):
        '''check upwards to see if any pieces of the opposing player will be flipped to
        player's piece'''
        #6,2
        drop_input_row = int(self._drop_piece_input[0]) #6
        drop_input_column = int(self._drop_piece_input[1]) #2

        test_list = []
        if self._gamestate == 1:
            for n in range(1, self._row + 1):
                if n != drop_input_row and self._board[n-1][drop_input_column-1] == 'B':
                    designated_end = n
                    for x in range(designated_end, drop_input_row):
                        test_list.append(self._board[x-1][drop_input_column-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(designated_end, drop_input_row):
                            if self._board[y-1][drop_input_column-1] == 'W':
                                coordinates = y, drop_input_column
                                self._interesting_pieces.append(coordinates)
 
        else:
            for n in range(1, self._row + 1):
                if n != drop_input_row and self._board[n-1][drop_input_column-1] == 'W':
                    designated_end = n
                    for x in range(designated_end, drop_input_row):
                        test_list.append(self._board[x-1][drop_input_column-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(designated_end, drop_input_row):
                            if self._board[y-1][drop_input_column-1] == 'B':
                                coordinates = y, drop_input_column
                                self._interesting_pieces.append(coordinates)
                    

    def check_down(self):
        '''check downwards to see if any pieces of the opposing player will be flipped to
        player's piece'''
        
        drop_input_row = int(self._drop_piece_input[0])
        drop_input_column = int(self._drop_piece_input[1])
        test_list = []        
        if self._gamestate == 1:
            for n in range(1, self._row + 1):
                if n != drop_input_row and self._board[n-1][drop_input_column -1] == 'B':
                    designated_end = n
                    for x in range(drop_input_row, designated_end):
                        test_list.append(self._board[x][drop_input_column-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(drop_input_row, designated_end):
                            if self._board[y][drop_input_column-1] == 'W':
                                coordinates = y+1, drop_input_column
                                self._interesting_pieces.append(coordinates)
                    
        else:
            for n in range(1, self._row + 1):
                if n != drop_input_row and self._board[n-1][drop_input_column -1] == 'W':
                    designated_end = n
                    for x in range(drop_input_row, designated_end):
                        test_list.append(self._board[x][drop_input_column-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(drop_input_row, designated_end):
                            if self._board[y][drop_input_column-1] == 'B':
                                coordinates = y+1, drop_input_column
                                self._interesting_pieces.append(coordinates)
                          

    def check_right(self):
        '''check to the right to see if any pieces of the opposing player will be flipped to
        player's piece'''
        # given input = (2,1)
        drop_input_row = int(self._drop_piece_input[0])  # 2
        drop_input_column = int(self._drop_piece_input[1]) # 1
        test_list = []
        if self._gamestate == 1:
            for n in range(1, self._row + 1):
                if n != drop_input_column and self._board[drop_input_row-1][n-1] == 'B':
                    designated_end = n# 4, 4
                    for x in range(drop_input_column+1, designated_end):
                        test_list.append(self._board[drop_input_row-1][x-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(drop_input_column+1, designated_end):
                            if self._board[drop_input_row-1][y-1] == 'W':
                                coordinates = drop_input_row, y
                                self._interesting_pieces.append(coordinates)
                       
        else:
            if self._gamestate == 2:
                for n in range(1, self._row + 1):
                    if n != drop_input_column and self._board[drop_input_row-1][n-1] == 'W':
                        designated_end = n # 4, 4
                        for x in range(drop_input_column +1, designated_end):
                            test_list.append(self._board[drop_input_row-1][x-1])
                        if '.' in test_list:
                            break
                        else:
                            for y in range(drop_input_column+1, designated_end):
                                if self._board[drop_input_row-1][y-1] == 'B':
                                    coordinates = drop_input_row, y
                                    self._interesting_pieces.append(coordinates)
                                

    def check_left(self):
        '''check to the left to see if any pieces of the opposing player will be flipped to
        player's piece'''

        #given input = (2,4)
        drop_input_row = int(self._drop_piece_input[0])  #2
        drop_input_column = int(self._drop_piece_input[1]) #4
        test_list = []
        
        if self._gamestate == 1:
            for n in range(1, self._row + 1):
                if n != drop_input_column and self._board[drop_input_row-1][n-1] == 'B':
                    designated_end = n
                    for x in range(designated_end, drop_input_column):
                        test_list.append(self._board[drop_input_row-1][x-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(designated_end, drop_input_column):
                            if self._board[drop_input_row-1][y-1] == 'W':
                                coordinates = drop_input_row, y
                                self._interesting_pieces.append(coordinates)
                        
        else:
            for n in range(1, self._row + 1):
                if n != drop_input_column and self._board[drop_input_row-1][n-1] == 'W':
                    designated_end = n
                    for x in range(designated_end, drop_input_column):
                        test_list.append(self._board[drop_input_row-1][x-1])
                    if '.' in test_list:
                        break
                    else:
                        for y in range(designated_end, drop_input_column):
                            if self._board[drop_input_row-1][y-1] == 'B':
                                coordinates = drop_input_row, y
                                self._interesting_pieces.append(coordinates)
                          


    def check_up_right(self):
        '''check to the up right to see if any pieces of the opposing player will be flipped to
        player's piece'''
        try:
            drop_input_row = int(self._drop_piece_input[0])  #5
            drop_input_column = int(self._drop_piece_input[1]) #4
            final_list = []
            n_list = []
            x_list = []
            z_list = []
            for n in range(drop_input_column, self._column + 1):
                n_list.append(n)
            for x in range(1, drop_input_row + 1):
                x_list.append(x)
            for z in reversed(x_list):
                z_list.append(z)
            if len(n_list) > len(z_list):
                end = len(z_list)
            elif len(n_list) < len(z_list):
                end = len(n_list)
            else:
                end = len(z_list)

            for x in range(end):
                coord = (z_list[x],n_list[x])
                final_list.append(coord)

            if self._gamestate == 1:
                for n in range(1, drop_input_row + 1):
                    if final_list[n-1][0] != drop_input_row and self._board[(final_list[n-1][0])-1][(final_list[n-1][1])-1] == 'B':
                        designated_end = n
                        for x in range(2, designated_end):                           
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.' and final_list[x-1][0] != drop_input_row:                               
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == 'W':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
                                
            else:
                for n in range(1, drop_input_row + 1):
                    if final_list[x-1][0] != drop_input_row and self._board[(final_list[n-1][0])-1][(final_list[n-1][1])-1] == 'W':
                        designated_end = n
                        for x in range(2, designated_end):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.' and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'B':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
        except IndexError:
            return 


    def check_down_right(self):
        ''' check to the down right to see if any pieces of the opposing player will be flipped to
        player's piece'''
        #1,3
        try:
            drop_input_row = int(self._drop_piece_input[0])  #1
            drop_input_column = int(self._drop_piece_input[1]) #3
            final_list = []
            n_list = []
            x_list = []
            z_list = []
            
            for z in range(drop_input_row, self._column + 1):
                z_list.append(z) 
            for n in range(drop_input_column, self._column + 1):
                n_list.append(n)
                
            if len(n_list) > len(z_list):
                end = len(z_list)
            elif len(n_list) < len(z_list):
                end = len(n_list)
            else:
                end = len(z_list)
            for x in range(end):
                coord = (z_list[x],n_list[x])
                final_list.append(coord)
      
            if self._gamestate == 1:
                for n in range(1, len(final_list) +1):
                    if final_list[n-1][0] != drop_input_row and self._board[(final_list[n-1][0])-1][(final_list[n-1][1])-1] == 'B':
                        designated_end = n
                        for x in range(1, designated_end):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== '.' and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'W':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
    
            else:
                for x in range(1, (len(final_list) +1) ):
                     if final_list[x-1][0] != drop_input_row and self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == 'W' and (final_list[x-1][0]) != 0:
                        designated_end = x
                        for x in range(1, designated_end):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.' and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'B':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
                                
                               
        except IndexError:
            pass

    def check_up_left(self):
        '''check to the up right to see if any pieces of the opposing player will be flipped to
        player's piece'''
        #given input = (5,4)
        try:
            drop_input_row = int(self._drop_piece_input[0])  #5
            drop_input_column = int(self._drop_piece_input[1]) #4
 
            final_list = []
            n_list = []
            x_list = []
            z_list = []
            for z in range(1 + (drop_input_row - drop_input_column), drop_input_row + 2):
                z_list.append(z)
            for n in range(1, drop_input_row + 2):
                n_list.append(n)
                
            if len(n_list) > len(z_list):
                end = len(z_list)
            elif len(n_list) < len(z_list):
                end = len(n_list)
            else:
                end = len(z_list)
            for x in range(end):
                coord = (z_list[x],n_list[x])
                final_list.append(coord)
            if self._gamestate == 1:
                for n in range(1, drop_input_row + 1):
                    if final_list[n-1][0] != drop_input_row and self._board[(final_list[n-1][0])-1][(final_list[n-1][1])-1] == 'B' and (final_list[n-1][0]) != 0:
                        designated_end = n
                        for x in range(designated_end, (drop_input_column)):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.'and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'W':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
                               
            else:
                for n in range(1, drop_input_row + 1):
                    if final_list[n-1][0] != drop_input_row and self._board[(final_list[n-1][0])-1][(final_list[n-1][1])-1] == 'W' and (final_list[n-1][0]) != 0:
                        designated_end = n
                        for x in range(designated_end, (drop_input_column)):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.'and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'B':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
                                
                            
        except IndexError:
            return


    def check_down_left(self):
        '''check to the down right to see if any pieces of the opposing player will be flipped to
        player's piece'''
        try:
            drop_input_row = int(self._drop_piece_input[0])  #1
            drop_input_column = int(self._drop_piece_input[1]) #3
            final_list = []
            n_list = []
            x_list = []
            z_list = []            
            for z in range(drop_input_row, self._row + 1):
                z_list.append(z)
            for x in range(1, drop_input_column+1):
                x_list.append(x)
            for n in reversed(x_list):
                n_list.append(n)
           
            if len(n_list) > len(z_list):
                end = len(z_list)
            elif len(n_list) < len(z_list):
                end = len(n_list)
            else:
                end = len(z_list)
            for x in range(end):
                coord = (z_list[x],n_list[x])
                final_list.append(coord)

            if self._gamestate == 1:
                for x in range(1, (len(final_list) +1) ):
                     if final_list[x-1][0] != drop_input_row and self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == 'B':
                        designated_end = x
                        for x in range(1, designated_end):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.' and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'W':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)
                        
            else:
                for x in range(1, (len(final_list) +1) ):
                     if final_list[x-1][0] != drop_input_row and self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == 'W':
                        designated_end = x
                        for x in range(1, designated_end):
                            if self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1] == '.'and final_list[x-1][0] != drop_input_row:
                                break
                            elif self._board[(final_list[x-1][0])-1][(final_list[x-1][1])-1]== 'B':
                                coordinates = final_list[x-1][0],final_list[x-1][1]
                                self._interesting_pieces.append(coordinates)                       
                    
        except IndexError:
            return 


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        



    def apply_all_checks(self):
        '''switch the pieces found by the check up function to the appropriate color, given
        the input'''
        
        z = 0
        for x in self._interesting_pieces:
            z += 1
        x = 0
        if self._gamestate == 1:
            for x in range(z):
                self._board[int(self._interesting_pieces[x][0])-1][int(self._interesting_pieces[x][1])-1] = 'B'
                x += 1
        else:
            for x in range(z):
                self._board[int(self._interesting_pieces[x][0])-1][int(self._interesting_pieces[x][1])-1] = 'W'
                x += 1
                
        self._interesting_pieces = []
    


        
    def check_piece_playable(self):
        '''check to see if desired input can be played'''
        
        if self._interesting_pieces == []:
            self._playable = False
            return False

        else:
            self._playable = True
            return True

       
    def check_board_playable(self):
        '''check to see if inputted board is still playable'''
        if self._interesting_pieces == []:
            self._initial_check = False
            return False
        else:
            self._initial_check = True
            return True
        
            
    def check_for_winner(self):
        '''Now that you can't add anymore pieces, tally up amount of pieces
        each side has, and find the winner'''

        if self._interesting_pieces == []:
            if self._winner == '>':
                if self._b_count > self._w_count:
                    return 1
                elif self._b_count < self._w_count:
                    return 2
                else:
                    return 0

            if self._winner == '<':
                if self._b_count < self._w_count:
                    return 1
                elif self._b_count > self._w_count:
                    return 2
                else:
                    return 0
        else:
            return

        
    def return_board(self):
        '''returns the board, to be printed in the interface'''

        return self._board
            

    def ultimate_check(self, dimensions):
        '''check to see if you can put a piece down in certain coordinate'''
        self._drop_piece_input = []
        self._interesting_pieces = []
        drop_input_row = int(dimensions[0])
        drop_input_column = int(dimensions[1])
        self._drop_piece_input.append(drop_input_row)
        self._drop_piece_input.append(drop_input_column)
        try:
            for x in self._board:
                if drop_input_column == len(x): 
                    if(drop_input_row == len(self._board)):
                        self.check_up(),self.check_left(),self.check_up_left()                       
                    elif((drop_input_row)-1) == 0:
                        self.check_down,self.check_left(),self.check_down_left()                       
                    else:
                        self.check_up(),self.check_down(),self.check_left(),
                        self.check_up_left(),self.check_down_left()                   
                elif (drop_input_column -1) == 0:
                    if(drop_input_row) == len(self._board):
                        self.check_up(),self.check_right(),self.check_up_right()
                    elif((drop_input_row)-1) == 0:
                        self.check_down(),self.check_right(),self.check_down_right()
                    else:
                        self.check_up(),self.check_down(),self.check_right()
                        self.check_up_right(), self.check_down_right()
                else:
                    ############
                    if(drop_input_row) == len(self._board):
                        self.check_up(),self.check_right(),self.check_left()
                        self.check_up_left(),self.check_up_right()
                    elif(drop_input_row -1) == 0:
                        self.check_down(),self.check_right(),self.check_left()
                        self.check_down_left(),self.check_down_right()                      
                    else:
                        self.check_up(),self.check_down(),self.check_right()
                        self.check_left(),self.check_up_right(),self.check_up_left()
                        self.check_down_right(),self.check_down_left()
            return self._interesting_pieces 
        except IndexError:
            break


    def check_if_game_playable(self):
        '''check to see if the inputted game is playable'''
        list_of_shit = []
        self._interesting_pieces = []
        for x in range(0, self._row):
            for y in range(0, self._column):
                if self._board[x][y] == '.':
                    x1 = x + 1
                    y2 = y + 1
                    coordinate = x1, y2
                    list_of_shit.append(coordinate)
        for x in range(0, (len(list_of_shit) ) ):
            r_input = list_of_shit[x][0]
            c_input = list_of_shit[x][1]
            self._board_check(r_input, c_input)
        if self._interesting_pieces == []:
            self._initial_check = False
            return False
        else:
            self._interesting_pieces = []
            self._initial_check = True
            return True

    

    def _board_check(self, r_input, c_input):
        '''check to see if you can put a piece down in certain coordinate'''
        self._drop_piece_input = []
        self._drop_piece_input.append(r_input)
        self._drop_piece_input.append(c_input)
        row_input = self._drop_piece_input[0]
        column_input = self._drop_piece_input[1]

        try:
            for x in self._board:
                if column_input == len(x):
                    if(row_input == len(self._board)):
                        self.check_up(),self.check_left(),self.check_up_left()
                    elif((row_input)-1) == 0:
                            self.check_down,self.check_left(),self.check_down_left()
                    else:
                            self.check_up(),self.check_down(),self.check_left(),
                            self.check_up_left(),self.check_down_left()                   
                elif (column_input -1) == 0:
                    if(row_input) == len(self._board):
                        self.check_up(),self.check_right(),self.check_up_right()
                    elif((row_input)-1) == 0:
                        self.check_down(),self.check_right(),self.check_down_right()
                    else:
                        self.check_up(),self.check_down(),self.check_right()
                        self.check_up_right(), self.check_down_right()
                else:
                    ############
                    if(row_input) == len(self._board):
                        self.check_up(),self.check_right(),self.check_left()
                        self.check_up_left(),self.check_up_right()
                    elif(row_input -1) == 0:
                        self.check_down(),self.check_right(),self.check_left()
                        self.check_down_left(),self.check_down_right()
                    else:
                        self.check_up(),self.check_down(),self.check_right()
                        self.check_left(),self.check_up_right(),self.check_up_left()
                        self.check_down_right(),self.check_down_left()
                        
        except IndexError:
            return 
        
        
 
