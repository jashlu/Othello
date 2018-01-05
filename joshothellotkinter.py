#Joshua Lu
#60343957
#Project 5


import tkinter

class SizeError(Exception):
    '''raised when the chessboard is oversized or too small'''
    pass


class NumError(Exception):
    '''raised when the user input is invalid'''
    pass


DEFAULT_FONT = ('Helvetica', 14)
_BACKGROUND_COLOR = '##00FFFF'


class GameSetup:
    '''setup functions for the othello game'''
    
    def __init__(self):
        self._gamestate = []

        self._dialog_window = tkinter.Tk()
        self._dialog_window.title('Othello Setup')


        intro_label = tkinter.Label(
            master = self._dialog_window, text = 'Welcome to Othello')
        intro_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        intro_label_2 = tkinter.Label(
            master = self._dialog_window, text = 'Please Fill Out the Following!')
        intro_label_2.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)        

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        row_input = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows:',
            font = DEFAULT_FONT)

        row_input.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_input_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._row_input_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        column_input = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns:',
            font = DEFAULT_FONT)

        column_input.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._column_input_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._column_input_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        choose_player_input = tkinter.Label(
            master = self._dialog_window, text = 'Choose Player to Start:',
            font = DEFAULT_FONT)
        
        choose_player_input.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._choose_player_input_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._choose_player_input_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        choose_winner_input = tkinter.Label(
            master = self._dialog_window, text = "Choose  ' > '  or  ' < ' :",
            font = DEFAULT_FONT)

        choose_winner_input.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._choose_winner_input_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._choose_winner_input_entry.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)        

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        self._button = tkinter.Button(master = self._dialog_window, text = "Let's Play!",
                                      command = self._on_ok_button,
                                      font = DEFAULT_FONT)

        self._button.grid(row = 6, column = 0, columnspan = 2, padx = 30, pady = 30,
                          sticky = tkinter.W + tkinter.S + tkinter.N + tkinter.E)
        

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._row_input = ''
        self._input = ''


    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        row_input = self._row_input_entry.get()
        column_input = self._column_input_entry.get()
        player_input = self._choose_player_input_entry.get()
        winner_input = self._choose_winner_input_entry.get()

        try:
            if int(row_input) < 4 or int(row_input) > 16:
                raise SizeError()
            if int(column_input) < 4 or int(row_input) > 16:
                raise SizeError()
            if not int(row_input) % 2 == 0 or not int(column_input) % 2 == 0:
                raise NumError()
 
            else:
                self._gamestate.append(row_input)
                self._gamestate.append(column_input)
                self._gamestate.append(player_input)
                self._gamestate.append(winner_input)
                self._dialog_window.destroy()
                return self._gamestate
                

        except ValueError:
           self._new_window = tkinter.Tk()
           self._new_window.title('WARNING')
           error_message = tkinter.Label(master = self._new_window, text = 'Please Enter Number Inputs')
           error_message.grid(row = 0, column = 0, padx = 10, pady = 10)
           close_popup = tkinter.Button(master = self._new_window, text = 'Ok', command = self._close_it)
           close_popup.grid(row = 1, column = 0, padx = 10, pady = 10)

        except NumError:
            self._new_window = tkinter.Tk()
            self._new_window.title('WARNING')
            error_message = tkinter.Label(master = self._new_window, text = 'Please Enter Even Number Inputs')
            error_message.grid(row = 0, column = 0, padx = 10, pady = 10)
            close_popup = tkinter.Button(master = self._new_window, text = 'Ok', command = self._close_it)
            close_popup.grid(row = 1, column = 0, padx = 10, pady = 10)

        except SizeError:
            self._new_window = tkinter.Tk()
            self._new_window.title('WARNING')
            error_message = tkinter.Label(master = self._new_window, text = 'Please Enter Number Inputs Between 4 and 16 (INCLUSIVE)')
            error_message.grid(row = 0, column = 0, padx = 10, pady = 10)
            close_popup = tkinter.Button(master = self._new_window, text = 'Ok', command = self._close_it)
            close_popup.grid(row = 1, column = 0, padx = 10, pady = 10)

            
    def _close_it(self):
        self._new_window.destroy()

    def start(self):
        self._dialog_window.mainloop()
        return self._gamestate



class SizeError(Exception):
    '''raised when the chessboard is oversized or too small'''
    pass


class NumError(Exception):
    '''raised when the user input is invalid'''
    pass


