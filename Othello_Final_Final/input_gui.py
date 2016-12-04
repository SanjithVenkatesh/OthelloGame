import tkinter

_DEFAULT_FONT = ('Verdana', 10)

# Module to obtain user choices for the Othello game

class InfoDialog:
	def __init__(self):
		self._dialog_window = tkinter.Toplevel()
		self._dialog_window.title("Othello (FULL) - Set Up")

		game_type_label = tkinter.Label(
			master = self._dialog_window, text = 'Select your choices for the game: ',
			font = _DEFAULT_FONT)

		game_type_label.grid(
			row = 0, column = 0, columnspan = 2, padx = 10, pady = 20,
			sticky = tkinter.W)

		# Label and OptionMenu for number of rows selection

		num_rows_label = tkinter.Label(
			master = self._dialog_window, text = 'Number of rows:',
			font = _DEFAULT_FONT)

		num_rows_label.grid(
			row = 1, column = 0, padx = 10, pady = 15,
			sticky = tkinter.W)

		optionList = ("4", "6", "8", "10", "12", "14", "16")
		self._row_value_option = tkinter.StringVar(self._dialog_window)
		self._row_value_option.set("4")
		self._num_rows_entry = tkinter.OptionMenu(
			self._dialog_window, self._row_value_option, *optionList)
		self._num_rows_entry["width"] = 4

		self._num_rows_entry.grid(
			row = 1, column = 1, padx = 10, pady = 15,
			sticky = tkinter.W)

		# Label and OptionMenu for number of columns selection

		num_cols_label = tkinter.Label(
			master = self._dialog_window, text = 'Number of columns:',
			font = _DEFAULT_FONT)

		num_cols_label.grid(
			row = 2, column = 0, padx = 10, pady = 10,
			sticky = tkinter.W)

		self._col_value_option = tkinter.StringVar(self._dialog_window)
		self._col_value_option.set("4")
		self._num_cols_entry = tkinter.OptionMenu(
			self._dialog_window, self._col_value_option, *optionList)
		self._num_cols_entry["width"] = 4

		self._num_cols_entry.grid(
			row = 2, column = 1, padx = 10, pady = 10,
			sticky = tkinter.W)

		# Label and Selection for player starting the game

		first_player_label = tkinter.Label(
			master = self._dialog_window, text = 'Player making first move:',
			font = _DEFAULT_FONT)

		first_player_label.grid(
			row = 3, column = 0, padx = 10, pady = 10,
			sticky = tkinter.W)

		button_frame = tkinter.Frame(master = self._dialog_window)

		self._first_player_entry = tkinter.IntVar()
		self._first_player_black_rb = tkinter.Radiobutton(
			master = button_frame, text="Black", variable=self._first_player_entry, value=1)
		self._first_player_white_rb = tkinter.Radiobutton(
			master = button_frame, text="White", variable=self._first_player_entry, value=2)
   
		self._first_player_black_rb.grid(
			row = 0, column = 0, padx = 2, pady = 2)
		self._first_player_white_rb.grid(
			row = 0, column = 1, padx = 2, pady = 2)
        
		self._first_player_black_rb.select()

		button_frame.grid(
			row = 3, column = 1, padx = 10, pady = 1,
			sticky = tkinter.W + tkinter.E)

		# Label and selection for initial top left disc color
		top_left_disc_label = tkinter.Label(
			master = self._dialog_window, text = 'Initial upper-left disc color:',
			font = _DEFAULT_FONT)

		top_left_disc_label.grid(
			row = 4, column = 0, padx = 10, pady = 10,
			sticky = tkinter.W)

		# Create a frame and place radio buttons with options "Black" and "White" on it
		button_frame = tkinter.Frame(master = self._dialog_window)

		self._top_left_disc_entry = tkinter.IntVar()
		self._top_left_black_rb = tkinter.Radiobutton(
			master = button_frame, text="Black", variable=self._top_left_disc_entry, value=1)
		self._top_left_white_rb = tkinter.Radiobutton(
			master = button_frame, text="White", variable=self._top_left_disc_entry, value=2)
   
		self._top_left_black_rb.grid(
			row = 0, column = 0, padx = 2, pady = 2)
		self._top_left_white_rb.grid(
			row = 0, column = 1, padx = 2, pady = 2)

		self._top_left_black_rb.select()  # select 'Black' by default

		button_frame.grid(
			row = 4, column = 1, padx = 10, pady = 10,
			sticky = tkinter.W + tkinter.E)

		# Label and selection for game winning criteria
		who_wins_label = tkinter.Label(
			master = self._dialog_window, text = 'Who wins?   Player with :',
			font = _DEFAULT_FONT)

		who_wins_label.grid(
			row = 5, column = 0, padx = 10, pady = 10,
			sticky = tkinter.W)


		# Create a frame and place radio buttons with options "Black" and "White" on it
		button_frame = tkinter.Frame(master = self._dialog_window)

		self._who_wins_entry = tkinter.IntVar()
		self._who_wins_higher_rb = tkinter.Radiobutton(
			master = button_frame, text="More discs", variable=self._who_wins_entry, value=1)
		self._who_wins_lower_rb = tkinter.Radiobutton(
			master = button_frame, text="Fewer discs", variable=self._who_wins_entry, value=2)
   
		self._who_wins_higher_rb.grid(
			row = 0, column = 0, padx = 2, pady = 2)
		self._who_wins_lower_rb.grid(
			row = 0, column = 1, padx = 2, pady = 2)

		self._who_wins_higher_rb.select()

		button_frame.grid(
			row = 5, column = 1, padx = 10, pady = 10,
			sticky = tkinter.W + tkinter.E)


		button_frame = tkinter.Frame(master = self._dialog_window)

		button_frame.grid(
			row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
			sticky = tkinter.E + tkinter.S)

		ok_button = tkinter.Button(
			master = button_frame, text = 'OK', font = _DEFAULT_FONT,
			command = self._on_ok_button)

		ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

		cancel_button = tkinter.Button(
			master = button_frame, text = 'Cancel', font = _DEFAULT_FONT,
			command = self._on_cancel_button)

		cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

		self._dialog_window.rowconfigure(6, weight = 1)
		self._dialog_window.columnconfigure(1, weight = 1)

		self._ok_clicked = False
		self._numRows = 0
		self._numCols = 0
		self._firstPlayer = None
		self._top_left_color = None
		self._who_wins = None

	def show(self) -> None:
		'''
		Display the modal window by grabbing all the events.
		'''
		self._dialog_window.grab_set()
		self._dialog_window.wait_window()

	def _on_ok_button(self) -> None:
		'''
		Handler for OK button
		'''
		self._ok_clicked = True
		self._numRows = self._row_value_option.get()
		self._numCols = self._col_value_option.get()

		self._firstPlayer = "B"
		if self._first_player_entry.get() == 2:
			self._firstPlayer = "W"

		self._top_left_color = "B"
		if self._top_left_disc_entry.get() == 2:
			self._top_left_color = "W"

		self._who_wins = ">"
		if self._who_wins_entry.get() == 2:
			self._who_wins = "<"

		self._dialog_window.destroy()

	def _on_cancel_button(self) -> None:
		'''
		Handler for cancel button
		'''
		self._dialog_window.destroy()

	# input data will be retrieved from the following methods

	def was_ok_clicked(self) -> bool:
		return self._ok_clicked

	def get_num_rows(self) -> int:
		value = int(self._numRows)
		return value

	def get_num_cols(self) -> int:
		value = int(self._numCols)
		return value

	def get_first_player(self) -> str:
		return self._firstPlayer

	def get_top_left_color(self) -> str:
		return self._top_left_color

	def get_who_wins(self) -> str:
		return self._who_wins


class DialogApplication:
	def __init__(self):
		self._root_window = tkinter.Tk()
		self._initialized = False 
		self._root_window.bind('<Configure>', self._onFormEvent)

	def run(self) -> None:
		'''
		Runs the DialogApplication application.
		It launches the modal dialog to collect user input about the game.
		It then destroys itself as the Othello window needs to be created new
		based on the user input received.
		'''
		self._root_window.mainloop()

	def _onFormEvent(self, event: tkinter.Event) -> None:
		'''
		Window resize (configure) event is received multiple times upon creation.
		Act only the first time to launch the modal dialog baed on the _initialized flag.
		'''
		if (self._initialized == False):
			self._initialized = True

			self._info_dialog = InfoDialog()
			self._info_dialog.show()

			# Finally destroy this window that launched the modal dialog
			# A new Othello window will be created based on user input received
			self._root_window.destroy()

	def get_input_data(self) -> InfoDialog:
		return self._info_dialog
