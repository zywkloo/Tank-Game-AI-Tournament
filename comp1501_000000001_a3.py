#<Trainer 01>
  
from library_for_glad_ai_tors import *
	
def start(arg):
	return ("moving_W", {"ACLT_X": -1, "ACLT_Y": +0})

def moving_N(arg):
	(x, y) = get_position(arg)
	border = get_n_border(arg)
	if y < border + 300:
		return ("moving_E", {"ACLT_X": +1, "ACLT_Y": +0})
	else:
		return ("moving_N", {"ACLT_X": +0, "ACLT_Y": -1})

def moving_E(arg):
	(x, y) = get_position(arg)
	border = get_e_border(arg)
	if x >= border - 300:
		return ("moving_S", {"ACLT_X": +0, "ACLT_Y": +1})
	else:
		return ("moving_N", {"ACLT_X": +1, "ACLT_Y": -0})
		
def moving_S(arg):
	(x, y) = get_position(arg)
	border = get_s_border(arg)
	if y >= border - 300:
		return ("moving_W", {"ACLT_X": -1, "ACLT_Y": +0})
	else:
		return ("moving_S", {"ACLT_X": +0, "ACLT_Y": +1})

def moving_W(arg):
	(x, y) = get_position(arg)
	border = get_w_border(arg)
	if x < border + 300:
		return ("moving_N", {"ACLT_X": +0, "ACLT_Y": -1})
	else:
		return ("moving_W", {"ACLT_X": -1, "ACLT_Y": +0})
