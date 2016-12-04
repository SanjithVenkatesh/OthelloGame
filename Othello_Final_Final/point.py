#point.py
#Sanjith Venkatesh
#ICS 32

class Point:
	'''
	This class is reused from CS32 lecture "The Spots Application"
	'''

	def __init__(self, frac_x: float, frac_y: float):
		'''
		Initializes  a Point object, given its fractional coordinates
		'''
		self._frac_x = frac_x
		self._frac_y = frac_y

	def frac(self) -> (float, float):
		'''
		Returns (x,y) tuple representation for this Point object
		'''
		return (self._frac_x, self._frac_y)

	def pixel(self, width: int, height: int) -> (int, int):
		'''
		Returns (x,y) tuple in pixel coordinates 
		given the width and height in pixel units
		'''
		return (int(self._frac_x * width), int(self._frac_y * height))

def from_frac(frac_x: float, frac_y: float) -> Point:
	'''
	Returns a Point object given its fractional coordinates
	'''
	return Point(frac_x, frac_y)

def from_pixel(pixel_x: int, pixel_y: int, width: int, height: int) -> Point:
	'''
	Returns a Point object given the pixel coordinates and its actual width, length
	'''
	return Point(pixel_x / width, pixel_y / height)