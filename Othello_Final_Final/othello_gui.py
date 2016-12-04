# Sanjith Venkatesh
# CS32
# Project 5

import tkinter
import point
from Othello import Othello
from Othello import InvalidMoveError
from input_gui import DialogApplication

_BACKGROUND_COLOR = '#FFFFFF'
_LINE_COLOR = '#008000'
_DEFAULT_FONT = ('Verdana', 10)
_CELL_WIDTH_PIXEL = 50
_CELL_HEIGHT_PIXEL = 50
_DISC_SPACE_FRAC = 0.20
_BLACK = 0
_WHITE = 1

class Cell:
	def __init__(self, origin : point.Point, bottom_right : point.Point):
		'''
		A Cell instance contains the fractional coordinates for the bounding box of the cell 
		within the larger canvas

		_origin: fractional coordinate in the canvas for top-left corner of the cell
		_bottom_right: fractional coordinate in the canvas for the bottom-right corner of the cell
		'''
		self._origin = origin
		self._bottom_right = bottom_right

	def center(self) -> point.Point:
		'''
		returns the fractional coordinates for the center of the cell
		'''
		origin_coord = self._origin.frac()
		bottom_right_coord = self._bottom_right.frac()
		center_x = (bottom_right_coord[0] - origin_coord[0]) / 2
		center_y = (bottom_right_coord[1] - origin_coord[1]) / 2
		return Point(center_x, center_y)

	def disc_coords(self) -> (point.Point, point.Point):
		'''
		returns the fractional coordinates of the disc that will be drawn within this cell
		We don't draw the disc here since it will depend on actual pixel coordinates
		'''
		origin_coord = self._origin.frac()
		bottom_right_coord = self._bottom_right.frac()
		x_spacing = ((bottom_right_coord[0] - origin_coord[0]) * _DISC_SPACE_FRAC) / 2
		y_spacing = ((bottom_right_coord[1] - origin_coord[1]) * _DISC_SPACE_FRAC) / 2
		top_left_coord = point.from_frac(origin_coord[0] + x_spacing, origin_coord[1] + y_spacing)
		bottom_right_coord = point.from_frac(bottom_right_coord[0] - x_spacing, bottom_right_coord[1] - y_spacing)
		return (top_left_coord, bottom_right_coord)


class Board:

	def __init__(self, num_rows: int, num_cols: int):
		'''
		A Board instance represents the layout of the Othello board
		composed of Cell instances for each location the discs can be placed.
		These Cell instances contain the fractional coordinates that will help
		with drawing the Othello grid and the discs
		'''
		self._num_rows = num_rows
		self._num_cols = num_cols

		# create the board with cells defined as Cell objects
		self._board = []
		for row in range(self._num_rows):
			cell_row = []
			for col in range(self._num_cols):
				origin = point.from_frac(col * (1 / self._num_cols), row * (1 / self._num_rows))
				bottom_right = point.from_frac(((col + 1) * (1 / self._num_cols)), ((row + 1) * (1 / self._num_rows)))
				cell_row.append(Cell(origin, bottom_right))
			self._board.append(cell_row)


	def board_size(self) -> (int, int):
		return (self._num_rows, self._num_cols)

	def board(self):
		return self._board

	def cell_location(self, point : point.Point) -> (int, int):
		'''
		Determines the cell location in the board given the fractional coordinates
		'''
		row_frac = 1 / self._num_rows
		col_frac = 1 / self._num_cols
		point_coord = point.frac()
		#print("row: ", (point_coord[1], row_frac, point_coord[1]/row_frac))
		#print("col: ", (point_coord[0], col_frac, point_coord[0]/col_frac))
		row = int((point_coord[1] / row_frac)) + 1
		col = int((point_coord[0] / col_frac)) + 1
		return (row, col)

	def cell_from_point(self, point : point.Point) -> Cell:
		'''
		Returns the Cell instance of the given Point object instance
		'''
		row_frac = 1 / self._num_rows
		col_frac = 1 / self._num_cols
		point_coord = point.frac()
		row = int((point_coord[1] / row_frac))
		col = int((point_coord[0] / col_frac))
		return self._board[row][col]

	def cell_from_loc(self, row, col) -> Cell:
		return self._board[row][col]

class OthelloBoardApp:

	def __init__(self, input_data):
		'''
		Initializes the GUI board and the Othello model
		'''
		# store input data
		num_rows = input_data.get_num_rows()
		num_cols = input_data.get_num_cols()
		self._next_player = input_data.get_first_player()
		top_left_color = input_data.get_top_left_color()
		self._who_wins = input_data.get_who_wins()

		# set up the GUI: Canvas and labels
		self._root_window = tkinter.Tk()
		self._root_window.title("Othello - FULL")

		self._board = Board(num_rows, num_cols)
		self._board_width, self._board_height = self.board_size(num_rows, num_cols)

		self._canvas = tkinter.Canvas(
							master = self._root_window, width = self._board_width, height = self._board_height,
							background = _BACKGROUND_COLOR)

		self._canvas.grid(
					row = 0, column = 0, padx = 2, pady = 2,
					sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		self._next_turn = tkinter.StringVar()
		self._turn_label = tkinter.Label(
					master = self._root_window, textvariable = self._next_turn,
					font = _DEFAULT_FONT)

		self._turn_label.grid(
					row = 1, column=0, padx = 2, pady = 2,
					sticky = tkinter.W)

		self._disc_counts = tkinter.StringVar()
		self._count_label = tkinter.Label(
					master = self._root_window, textvariable = self._disc_counts,
					font = _DEFAULT_FONT)

		self._count_label.grid(
					row = 2, column=0, padx = 2, pady = 2,
					sticky = tkinter.W)

		# set up window resizing
		self._root_window.columnconfigure(0, weight = 1)
		self._root_window.rowconfigure(0, weight = 1)

		# set up callback handlers for button release and configuration
		self._canvas.bind('<ButtonRelease-1>', self._on_button_down)
		self._canvas.bind('<Configure>', self._on_canvas_resize)

		# set up Othello model
		self._game_over = False
		self._othello = Othello(num_rows, num_cols, self._next_player)
		self._othello.setBoard(top_left_color)
		self._process_next_move()

	def run(self) -> None:
		'''
		Runs the Othello application taking user inputs
		'''
		self._root_window.mainloop()

	def board_size(self, num_rows, num_cols) -> (int, int):
		''' 
		Returns the size of the board in pixel units
		Draws bigger cells when number of columns is less than 4 
		so that the complete title of the window is displayed.
		'''
		if (num_cols == 4):
			return (num_cols * 70, num_rows * 70)
		else:
			return (num_cols * 50, num_rows * 50)

	def _on_button_down(self, event: tkinter.Event):
		'''
		Event handler for left mouse button release event
		'''
		if self._game_over == False:
			canvas = event.widget
			x = canvas.canvasx(event.x)
			y = canvas.canvasy(event.y)
			#print ((event.x, event.y), (x,y))

			player_input = self._board.cell_location(point.from_pixel(x,y, self._board_width, self._board_height))
			try:
				if self._othello._validateInput(player_input, self._next_player):
					self._othello.updateBoard(player_input, self._next_player)
					self._process_next_move()
			except InvalidMoveError:
				pass # nothing to do if invalid move

	def _process_next_move(self):
		'''
		Processes the next move by calling the Othello model.
		Called after initial board set up and after every uesr selection
		'''
		#self.printBoard()
		self._draw_board(self._othello.getBoard())
		if self._othello.continuePlaying(): # game still continuing
			self._next_player = self._othello.getNextPlayer()
			self._next_turn.set('Next Turn: ' + self.display_color(self._next_player))
		else:  # game over. determine and print winner
			self._game_over = True
			self._next_turn.set("WINNER: " + self._winner())

		# set the tile count for both ongoing or end game
		num_tiles = self._othello.determineNumberTiles()
		self._disc_counts.set('Black: '+ str(num_tiles[_BLACK]) + '  White: ' + str(num_tiles[_WHITE]))

	def _winner(self) -> str:
		''' 
		Determines the winner by comparing the tile counts
		against the winner criteria provided as input to the game.
		'''
		num_tiles = self._othello.determineNumberTiles()
		winner = "None"
		if (self._who_wins == ">"):  # higher count wins
			if (num_tiles[_BLACK] < num_tiles[_WHITE]):
				winner = "White"
			elif (num_tiles[_BLACK] > num_tiles[_WHITE]):
				winner = "Black"
		elif (self._who_wins == "<"):  # lower count wins
			if (num_tiles[_BLACK] > num_tiles[_WHITE]):
				winner = "White"
			elif (num_tiles[_BLACK] < num_tiles[_WHITE]):
				winner = "Black"

		return winner

	def _on_canvas_resize(self, event: tkinter.Event):
		'''
		Handler for canvas resize. 
		Redraws the entire board with current dimensions
		'''
		self._canvas.delete(tkinter.ALL)
		self._board_width = self._canvas.winfo_width()
		self._board_height = self._canvas.winfo_height()
		self._draw_board(self._othello.getBoard())

	def _draw_board(self, board_info) -> None:
		'''
		Draw the Othello game board
		First draws the vertical and horizontal grid lines on the canvas
		Then draws the currently available black and white discs from the Othello model
		'''
		board_size = self._board.board_size()
		next_x = 0
		for vert_line in range(board_size[1]):
			# print((next_x,0,next_x,self._board_height))
			self._canvas.create_line(next_x, 0, next_x, self._board_height, fill='red', width='2.0')
			next_x = next_x + (self._board_width / board_size[1])

		next_y = 0
		for hor_line in range(board_size[0]):
			# print((0, next_y, self._board_width, next_y,))
			self._canvas.create_line(0, next_y, self._board_width, next_y, fill='red', width='2.0')
			next_y = next_y + (self._board_height / board_size[0])

		for row in range(board_size[0]):
			for col in range(board_size[1]):
				cell = self._board.cell_from_loc(row, col)
				self._draw_disc(cell, self.display_color(board_info[row][col]))

	def display_color(self, color_code: str) -> str:
		'''
		Translates the color code understood by Othello model to readable string for GUI display
		'''
		if (color_code == 'W'):
			return 'White'
		elif (color_code == 'B'):
			return 'Black'
		else:
			return None

	def _draw_disc(self, cell: Cell, color: str) -> None:
		'''
		Draws the disc of the provided color in the given Cell object instance
		'''
		if (color != None):
			disc_coords = cell.disc_coords()
			top_left = disc_coords[0].pixel(self._board_width, self._board_height)
			bottom_right = disc_coords[1].pixel(self._board_width, self._board_height)
			self._canvas.create_oval(top_left[0], top_left[1],
									bottom_right[0], bottom_right[1],
									fill = color, outline = 'black')


	def printBoard(self): 
		#prints the board on console - for debug purposes only
		boardInfo = self._othello.getBoard()
		for row in boardInfo:
			rowStr = ""
			for col in row:
				rowStr += col + " "
			print(rowStr)

if __name__ == '__main__':
	input_dialog = DialogApplication()
	input_dialog.run()
	input_data = input_dialog.get_input_data()
	OthelloBoardApp(input_data).run()

