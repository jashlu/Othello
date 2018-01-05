#Joshua Lu
#60343957
#Project 5

import point1
import spots1
import joshothellotkinter
from joshothellotkinter import GameSetup
import joshuaconsole1
from joshuaconsole1 import Gamestate
import tkinter

DEFAULT_FONT = ('Helvetica', 20)


class SpotsApplication:
    def __init__(self, dimensions, turn, winner, board, state1: spots1.SpotsState):
        self._dimensions = dimensions
        self._row = int(dimensions[0])
        self._column = int(dimensions[1])
        self._drop_x = None
        self._drop_y = None
        self._winner = winner
        self.board = board
        self._xbox = []
        self._ybox = []
        self._turn = turn
        self._state = state1
        self._root_window = tkinter.Tk()
        self._b_count = 0
        self._w_count = 0

        title1 = tkinter.StringVar()
        title1.set('OTHELLO: FULL VERSION')
        self._title = tkinter.Label(master = self._root_window, textvariable = title1, font = DEFAULT_FONT)
        self._title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#1a5b10')
        self._canvas.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
#-------------
        self._score_label = tkinter.Label(
            master = self._root_window, text = '',
            font = ('Helvetica', 20))
        self._score_label.grid(row = 1, column = 0, padx = 0, pady = 10)

        title2 = tkinter.StringVar()              
        title2.set('Press BEGIN GAME to Start Playing!')
        self._title2 = tkinter.Label(master = self._root_window, textvariable = title2, font = DEFAULT_FONT)
        self._title2.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = tkinter.W)

        self._button1 = tkinter.Button(
            master = self._root_window, text = 'BEGIN GAME', font = DEFAULT_FONT, command = self.update_button1)
        self._button1.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.S)
            
        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._button_frame = tkinter.Frame(
            master = self._root_window, background = 'pink')
        self._button_frame.grid(
            row = 1, column = 2, rowspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        
        numbered_button = tkinter.Button(
            master = self._button_frame, text = 'QUIT GAME', font = DEFAULT_FONT, command = self.leave_game)
        numbered_button.grid(
            row = 0, column = 0, padx = 0, pady = 0)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def update_button1(self):
        self._canvas.bind('<Button-1>', self.setup_board)
        self._button1.destroy()
        self._title2.destroy()
        self._button2 = tkinter.Button(
            master = self._root_window, text = 'Player 2 Turn', font = DEFAULT_FONT, command = self.update_button2)
        self._button2.grid(row = 4, column = 0, padx = 10, pady = 20,
                           sticky = tkinter.W + tkinter.S)
        title2 = tkinter.StringVar()
        title2.set('Enter Pieces for Player 1, \n Once Done, Press Button to Move On to Player 2')
        self._title2 = tkinter.Label(master = self._root_window, textvariable = title2, font = DEFAULT_FONT)
        self._title2.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = tkinter.W)
    
    def update_button2(self):
        if self._turn == 'B':
            self._turn = 'W'
        else:
            self._turn = 'B'
        self._button2.destroy()
        self._title2.destroy()
        self._button3 = tkinter.Button(
            master = self._root_window, text = "Let's Play!", font = DEFAULT_FONT, command = self.update_button3)
        self._button3.grid(row = 4, column = 0, padx = 10, pady = 20,
                               sticky = tkinter.W + tkinter.S)
        title3 = tkinter.StringVar()
        title3.set('Enter Pieces for Player 2, \nOnce Done, Press Button to Begin!!')
        self._title3 = tkinter.Label(master = self._root_window, textvariable = title3, font = DEFAULT_FONT)
        self._title3.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = tkinter.W)
        
        
    def update_button3(self):
        if self._turn == 'B':
            title2 = tkinter.StringVar()
            title2.set("Let's Play The Game! PLAYER W GOES FIRST")
            self._title = tkinter.Label(master = self._root_window, textvariable = title2, font = DEFAULT_FONT)
            self._title.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.S)       
            self._turn = 'W'
        else:
            title3 = tkinter.StringVar()
            title3.set("Let's Play The Game! PLAYER B GOES FIRST")
            self._title = tkinter.Label(master = self._root_window, textvariable = title3, font = DEFAULT_FONT)
            self._title.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.S)       
            self._turn = 'B'
            
        self._button3.destroy()
        self._title3.destroy()
        gamestate = joshuaconsole1.Gamestate(self._turn, self._dimensions, self._winner, self.board)
        check = gamestate.check_if_game_playable()
        
        if check == True:
            self._title.destroy()
            turn = gamestate.current_player()
            self._display_turn(turn)
            self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        else:
            self._title.destroy()
            end_title = tkinter.StringVar()
            end_title.set("GAME OVER")
            self._end_title = tkinter.Label(master = self._root_window, textvariable = end_title, font = DEFAULT_FONT)
            self._end_title.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
            self._canvas.bind('<Button-1>', self.leave_game)

            self._winner_label = tkinter.Label(
                master = self._root_window, text = '',
                font = ('Helvetica', 20))
            self._winner_label.grid(row = 4, column = 0, padx = 0, pady = 10)

            scores = gamestate.count_pieces()
            win_num = gamestate.check_for_winner()
            if win_num == 1:
                winner = 'B'
                self._winner_label['text'] = f'WINNER: {winner}'
            elif win_num == 2:
                winner = 'W'
                self._winner_label['text'] = f'WINNER: {winner}'
            elif win_num == 0:
                winner = 'NONE'
                self._winner_label['text'] = f'WINNER: {winner}'


                   
    def _display_turn(self, turn):
        if turn == 1:
            turn_title = tkinter.StringVar()
            turn_title.set("TURN: B")
            self._turn_title = tkinter.Label(master = self._root_window, textvariable = turn_title, font = DEFAULT_FONT)
            self._turn_title.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
        elif turn == 2:
            turn_title = tkinter.StringVar()
            turn_title.set("TURN: W")
            self._turn_title = tkinter.Label(master = self._root_window, textvariable = turn_title, font = DEFAULT_FONT)
            self._turn_title.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
            
    
    def leave_game(self):
        self._root_window.destroy()
                      
    def run(self) -> None:
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._redraw_all_spots()
        self._redraw_all_lines()

    def setup_board(self, event: tkinter.Event) -> None:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        converted = self.convert_piece(event.x, event.y)

        gamestate = joshuaconsole1.Gamestate(self._turn, self._dimensions, self._winner, self.board)
        
        coordinates = self._update_gamestate(converted)
        game1 = gamestate.drop_piece(coordinates)    
        
        click_point = point1.from_pixel(
            converted[0], converted[1], width, height)
    
        if self._turn.upper() == 'B':
            self._state.handle_black_click(click_point)
        else:
            self._state.handle_white_click(click_point)
            
        self._redraw_into_spots()


    def _update_gamestate(self, converted):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        variable = width/self._row
        coordinates = []

        for x in range(1, self._column + 1):
            if (variable * (x-1)) < converted[1] < variable * x:
                coordinates.append(x)               
        for y in range(1,self._row + 1):
            if (variable * (y-1)) < converted[0] < variable * y:
                coordinates.append(y)              
        return coordinates
    

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:


        gamestate = joshuaconsole1.Gamestate(self._turn, self._dimensions, self._winner, self.board)
        turn = gamestate.current_player()
        self._display_turn(turn)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        converted = self.convert_piece(event.x, event.y)
        
        check = gamestate.check_if_game_playable()
        if check == True:

            coordinates = self._update_gamestate(converted)
            game2 = gamestate.ultimate_check(coordinates)
            game3 = list(set(game2))
            game3.append(coordinates)
            
            if game2 != []:
                for x in game3:
                    update_pieces = self.reversed_convert_piece(x)                
                    gamestate.drop_piece(x)

                    click_point = point1.from_pixel(
                        update_pieces[0], update_pieces[1], canvas_width, canvas_height)
                    if self._turn.upper() == 'B':
                        self._state.handle_black_click(click_point)
                        if x != game3[-1]:
                            self._state.handle_white_click(click_point)
        
                    elif self._turn.upper() == 'W':
                        self._state.handle_white_click(click_point)
                        if x != game3[-1]:
                            self._state.handle_black_click(click_point)
                self._next_player()

            self._redraw_all_spots()

        check = gamestate.check_if_game_playable()
        if check == False:
            self._game_over(event)
        
           
##### still got to print winner 

    def _game_over(self, event: tkinter.Event) -> None:
        gamestate = joshuaconsole1.Gamestate(self._turn, self._dimensions, self._winner, self.board)
        
        self._title.destroy()
        end_title = tkinter.StringVar()
        end_title.set("GAME OVER")
        self._end_title = tkinter.Label(master = self._root_window, textvariable = end_title, font = DEFAULT_FONT)
        self._end_title.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
        self._canvas.bind('<Button-1>', self.leave_game)

        self._winner_label = tkinter.Label(
            master = self._root_window, text = '',
            font = ('Helvetica', 20))
        self._winner_label.grid(row = 4, column = 0, padx = 0, pady = 10)

        scores = gamestate.count_pieces()
        win_num = gamestate.check_for_winner()
        if win_num == 1:
            winner = 'B'
            self._winner_label['text'] = f'WINNER: {winner}'
        elif win_num == 2:
            winner = 'W'
            self._winner_label['text'] = f'WINNER: {winner}'
        elif win_num == 0:
            winner = 'NONE'
            self._winner_label['text'] = f'WINNER: {winner}'
        


    def _next_player(self) -> None:

        if self._turn == 'B':
            self._turn = 'W'
        elif self._turn == 'W':
            self._turn = 'B' 

 #>>>>>>>>>>>>>       
        
    def _redraw_into_spots(self) -> None:

        self._canvas.delete(tkinter.ALL)
        self._redraw_all_lines()
        
        for spot in self._state.all_black_spots():
            self._draw_black_spot(spot)

        for spot in self._state.all_white_spots():
            self._draw_white_spot(spot)

#>>>>>>>>>>>>>>>
        
    def _redraw_all_spots(self) -> None:

        gamestate = joshuaconsole1.Gamestate(self._turn, self._dimensions, self._winner, self.board)
        scores = gamestate.count_pieces()
        b = scores[0]
        self._b_count = b
        w = scores[1]
        self._w_count = w
        self._score_label['text'] = f'Black: {b} White: {w}'
      
        self._canvas.delete(tkinter.ALL)
        self._redraw_all_lines()

        for spot in self._state.all_black_spots():
            self._draw_black_spot(spot)

        for spot in self._state.all_white_spots():
            self._draw_white_spot(spot)

####fix the size of the circles redrawn it looks weird

    def _draw_black_spot(self, spot: spots1.Spot) -> None:
        center_frac_x, center_frac_y = spot.center().frac()
        frac_radius = spot.radius_frac()

        topleft_frac_x = center_frac_x - frac_radius
        topleft_frac_y = center_frac_y - frac_radius
        bottomright_frac_x = center_frac_x + frac_radius
        bottomright_frac_y = center_frac_y + frac_radius
        
        topleft = point1.from_frac(topleft_frac_x, topleft_frac_y)
        bottomright = point1.from_frac(bottomright_frac_x, bottomright_frac_y)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        topleft_pixel_x, topleft_pixel_y = topleft.pixel(canvas_width, canvas_height)
        bottomright_pixel_x, bottomright_pixel_y = bottomright.pixel(canvas_width, canvas_height)

        self._canvas.create_oval(
            topleft_pixel_x, topleft_pixel_y,
            bottomright_pixel_x, bottomright_pixel_y,
            fill = 'black', outline = '#000000')           

    def _draw_white_spot(self, spot: spots1.Spot) -> None:
        center_frac_x, center_frac_y = spot.center().frac()
        frac_radius = spot.radius_frac()

        topleft_frac_x = center_frac_x - frac_radius
        topleft_frac_y = center_frac_y - frac_radius
        bottomright_frac_x = center_frac_x + frac_radius
        bottomright_frac_y = center_frac_y + frac_radius
        
        topleft = point1.from_frac(topleft_frac_x, topleft_frac_y)
        bottomright = point1.from_frac(bottomright_frac_x, bottomright_frac_y)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        topleft_pixel_x, topleft_pixel_y = topleft.pixel(canvas_width, canvas_height)
        bottomright_pixel_x, bottomright_pixel_y = bottomright.pixel(canvas_width, canvas_height)

        self._canvas.create_oval(
            topleft_pixel_x, topleft_pixel_y,
            bottomright_pixel_x, bottomright_pixel_y,
            fill = '#f5f9f4', outline = '#000000')           

            
    def gameboard_conversion(self):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        for x in range(1, self._row+1):
            if (width /self._row)*(x-1) == self._xbox[0]:
                self._drop_y = x
                
        for y in range(1, self._column+1):
            if (height /self._column)*(y-1) == self._ybox[0]:
                self._drop_x = y           


#>>>>>>>>>>>>>>>>>>>>>>>>>>

    def reversed_convert_piece(self, dimensions) -> list:
        # go from 4,2 to 227.25, 530.25
        converted_coordinate = []
        column_coord= dimensions[0]
        row_coord = dimensions[1]
        constant = ((self._canvas.winfo_width()/self._row)/2)

        #for the 227.5 part
        x_value = ((self._canvas.winfo_width()/self._row) * (row_coord - 1)) + constant
        converted_coordinate.append(x_value)
        #for the 378.75 part
        y_value = ((self._canvas.winfo_height()/self._column) * (column_coord -1)) + constant
        converted_coordinate.append(y_value)
        return converted_coordinate
       

    def convert_piece(self, center_x, center_y):
        y = []
        self._point_boundaries()
        xbox = self.x_conversion(center_x)
        ybox = self.y_conversion(center_y)
        y.append(xbox[0])
        y.append(ybox[0])
        y.append(xbox[1])
        y.append(ybox[1])
        z = []
        x1 = ((y[2] - y[0])/2 + y[0])
        x2 = ((y[3] - y[1])/2 + y[1])
        z.append(x1)
        z.append(x2)
        return z
        
   
    def x_conversion(self,center_x):
        box = []

        for x in range(0,len(self._r_coordinates)):
            if 0 <= center_x <= self._r_coordinates[0]:
                box.append(0)
                box.append(self._r_coordinates[0])
                return box

            elif self._r_coordinates[x] <= center_x <= self._r_coordinates[(x+1)]:
                box.append(self._r_coordinates[x])
                box.append(self._r_coordinates[(x+1)])
                return box                   

    def y_conversion(self, center_y):
        box = [] 
        for y in range(len(self._c_coordinates)):
            if 0 <= center_y <= self._c_coordinates[0]:
                box.append(0)
                box.append(self._c_coordinates[0])
                return box
        
            elif self._r_coordinates[y] <= center_y <= self._c_coordinates[(y+1)]:
                box.append(self._r_coordinates[(y)])
                box.append(self._c_coordinates[y+1])
                return box

    def _point_boundaries(self):
        self._r_coordinates = []
        self._c_coordinates = []
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        for x in range(1, self._row+1):
            coord = (canvas_width/self._row)*x
            self._r_coordinates.append(coord)
       
        for y in range(1, self._column+1):
            coord = (canvas_height/self._column)*y
            self._c_coordinates.append(coord)
        
#>>>>>>>>>>>>>>>>>>>>>>>
            
    def _redraw_all_lines(self):
        self._create_row_line()
        self._create_column_line()
        
    def _create_row_line(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for x in range(1, self._row):
            variable = (1/self._row)*x
            self._black_row_line = self._canvas.create_line(variable*canvas_width, 0,
                                                            variable*canvas_width, canvas_height)          

    def _create_column_line(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for y in range(1, self._column):
            variable = (1/self._column)*y
            self._black_row_line = self._canvas.create_line(0, variable*canvas_height,
                                                            canvas_width, variable*canvas_height)



def input_board(row, column):
    '''User will create their designated board'''
    board = []
    for i in range(row):
        board.append([])
        for j in range(column):
            board[i].append('.')
    return board


def run():
    inputs = joshothellotkinter.GameSetup()
    inputs.start()
    gamestate = inputs._gamestate
    row = int(gamestate[0])
    column = int(gamestate[1])
    dimensions = []
    dimensions.append(row)
    dimensions.append(column)
    turn = gamestate[2]
    winner = gamestate[3]
    board = input_board(row, column)
    SpotsApplication(dimensions, turn, winner, board, spots1.SpotsState()).run()


if __name__ == '__main__':
    try:
        run()
    except IndexError:
        pass 
