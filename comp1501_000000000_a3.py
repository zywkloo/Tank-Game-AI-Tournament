#<Trainer 00>
  
from library_for_glad_ai_tors import *

import math
	
def start(arg):

	angle = get_weapon_angle(arg)
	distance = 100
		
	(x1, y1) = get_position(arg)
	(x2, y2) = (x1 + (math.cos(math.radians(angle)) * distance), y1 - (math.sin(math.radians(angle)) * distance))
	
	return ("start", {'LAUNCH':True, 'ROT_CC':0.1})