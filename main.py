from parser import *
from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
points = new_matrix()



parse_file( 'script', edges, transform, screen, color )
