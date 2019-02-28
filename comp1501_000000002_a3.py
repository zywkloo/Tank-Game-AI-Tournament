#<Trainer 02>
  
from library_for_glad_ai_tors import *

import math
	
def start(arg):
	return ("searching_for_target", {'CHARGE': True})
	
def searching_for_target(arg):

	angle = get_weapon_angle(arg)
	
	(target, _) = get_radar_data(arg, angle)
	
	(x1, y1) = get_position(arg)
	(x2, y2) = (x1 + (math.cos(math.radians(angle)) * 200), y1 - (math.sin(math.radians(angle)) * 200))
	
	if target == "opponent":
		return ("firing_on_target", {'ROT_CC': 0.0})
	else:
		return ("searching_for_target", {'ROT_CC': 0.1})

def firing_on_target(arg):
	return ("searching_for_target", {'LAUNCH': True})