from parser import *
from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = new_matrix()
points = new_matrix()

parse_file( 'script', edges, transform, screen, color )

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = new_matrix()
points = new_matrix()
parse_file( 'pic.txt', edges, transform, screen, color )
