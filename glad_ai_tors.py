import importlib
import random
import time
import multiprocessing
import pygame
import math
import sys

from pygame.locals import *


window_size = 640

game_world_size = 1280

tile_size = 64

frame_rate = 80



class Armour:

	def __init__(self, given_name, source_module, armour_number, initial_location):
	
		# the radii of the circles used for collision detection are hard-coded
		self.rad = 20
		
		# this is the name that will show under the armour during the battle
		self.who = given_name
		
		# 'num' is a number representing the index of this armour
		self.num = armour_number

		# (x, y) / (dx, dy) / (ddx, ddy) is the position / velocity / acceleration
		(  self.x,   self.y) = initial_location
		( self.dx,  self.dy) = (0, 0)
		(self.ddx, self.ddy) = (0, 0)
		
		# 'pwr' is an integer between 0 and 100, storing the weapon power
		self.pwr = 0
		
		# 'dmg' is an integer between 0 and 100, storing the damage level
		self.dmg = 0
		
		# 'aim' is a floating point value in (0, 359], storing the weapon angle
		self.aim = random.choice([90, 270])

		# 'max' is a floating point value between 0 and 1 used to set a cap on
		# weapon power, acceleration, etc. if shield/repair/charge is active
		self.max = 1.0

		# these are Boolean flags to store whether or not the shield, repair, or
		# charge functions are currently active
		self.shield_is_on = False
		self.repair_is_on = False
		self.charge_is_on = False

		# this stores the module defining the controlling finite state machine
		self.source_module = source_module
				
		# this stores the current state of the controlling finite state machine
		self.current_state = "start"

		# this dictionary stores the state of each effector for this armour
		self.effector_dict = {}

		# this dictionary stores the values "saved" to data registers, initially 'None'
		self.register_dict = {}
		for register in "abcdefghij":
			self.register_dict[register] = 0
		
		

class Rocket:

	def __init__(self, position, angle, owner, power):

		self.owner = owner
		
		self.power = power
		
		self.angle = angle

		angle_cos = math.cos(math.radians(angle))
		angle_sin = math.sin(math.radians(angle))

		self.sol_x = position[0] + ( angle_cos * 24)
		self.eol_x = self.sol_x

		self.sol_y = position[1] + (-angle_sin * 24)
		self.eol_y = self.sol_y

		self.dx =  angle_cos * 16.0
		self.dy = -angle_sin * 16.0
		

class Impact:

	def __init__(self, position):
	
		(self.x, self.y) = position
		
		self.frame_index = 1
		self.frame_delay = 100
		

class Pillar:

	def __init__(self, position):
	
		# the radii of the circles used for collision detection are hard-coded
		self.rad = 64
		
		# this is the location of the center of the pillar
		(self.x, self.y) = position


#def update(environment, armour, queue):
def update(environment, index, source, state, queue):

	# import the student submission for this competitor
	# module = importlib.import_module(armour.source_module)
	module = importlib.import_module(source)
	
	# the name of the finite state machine state is the function to be called
	# so find it in the module and call it, passing the environment as an argument
	# n.b., student submissions will be checked to ensure they do not attempt to
	# access the environment data directly (and, instead, must access it through
	# the accessor functions provided by me in the "library_for_glad_a_i_tors"
	#result = getattr(module, armour.current_state)(environment)
	result = getattr(module, state)(environment)
	
	# put the competitors index and the result (which is the next state for this
	# competitors finite state machine and the list corresponding to the effectors
	# registers into the queue
	#queue.put((armour.num, result))	
	queue.put((index, result))
 
 
 
def construct_environmental_data(i):

	environment = {}

	opponent_index = int(not i)
	environment['inaccessible_register_for_opponent'] = (armours[opponent_index].x, armours[opponent_index].y, armours[opponent_index].rad)
	
	environment['inaccessible_register_for_pillar_0'] = (pillars[0].x, pillars[0].y, pillars[0].rad)
	environment['inaccessible_register_for_pillar_1'] = (pillars[1].x, pillars[1].y, pillars[1].rad)
	environment['inaccessible_register_for_pillar_2'] = (pillars[2].x, pillars[2].y, pillars[2].rad)
	
	for register in "abcdefghij":
		environment[register] = armours[i].register_dict[register]

	environment['x'] = armours[i].x
	environment['y'] = armours[i].y
	environment['dx'] = armours[i].dx
	environment['dy'] = armours[i].dy
	environment['aim'] = armours[i].aim		
	environment['pwr'] = armours[i].pwr	
	environment['dmg'] = armours[i].dmg
	environment['shield'] = armours[i].shield_is_on
	environment['repair'] = armours[i].repair_is_on
	environment['charge'] = armours[i].charge_is_on

	environment['n_border'] = 0 + tile_size
	environment['s_border'] = game_world_size - tile_size
	environment['e_border'] = game_world_size - tile_size
	environment['w_border'] = 0 + tile_size
	
	return environment
	
	

def detect_collision_line_circle(u, v):

	# unpack u; a line is an ordered pair of points and a point is an ordered pair of co-ordinates
	(u_sol, u_eol) = u
	(u_sol_x, u_sol_y) = u_sol
	(u_eol_x, u_eol_y) = u_eol

	# unpack v; a circle is a center point and a radius (and a point is still an ordered pair of co-ordinates)
	(v_ctr, v_rad) = v
	(v_ctr_x, v_ctr_y) = v_ctr

	# the equation for all points on the line segment u can be considered u = u_sol + t * (u_eol - u_sol), for t in [0, 1]
	# the center of the circle and the nearest point on the line segment (that which we are trying to find) define a line 
	# that is is perpendicular to the line segment u (i.e., the dot product will be 0); in other words, it suffices to take
	# the equation v_ctr - (u_sol + t * (u_eol - u_sol)) · (u_evol - u_sol) and solve for t
	t = ((v_ctr_x - u_sol_x) * (u_eol_x - u_sol_x) + (v_ctr_y - u_sol_y) * (u_eol_y - u_sol_y)) / ((u_eol_x - u_sol_x) ** 2 + (u_eol_y - u_sol_y) ** 2)

	# this t can be used to find the nearest point w on the infinite line between u_sol and u_sol, but the line is not 
	# infinite so it is necessary to restrict t to a value in [0, 1]
	t = max(min(t, 1), 0)
	
	# so the nearest point on the line segment, w, is defined as
	w_x = u_sol_x + t * (u_eol_x - u_sol_x)
	w_y = u_sol_y + t * (u_eol_y - u_sol_y)
	
	# Euclidean distance squared between w and v_ctr
	d_sqr = (w_x - v_ctr_x) ** 2 + (w_y - v_ctr_y) ** 2
	
	# if the Eucliean distance squared is less than the radius squared then there has been a collision
	if (d_sqr <= v_rad ** 2):
		return True, (w_x, w_y)

	# if there hasn't been a collision the function will still return the nearest point (just in case)
	return False, (w_x, w_y)


	
def detect_collision_circle_circle(u, v):

	# unpack u; a circle is a center point and a radius (and a point is still an ordered pair of co-ordinates)
	(u_ctr, u_rad) = u
	(u_ctr_x, u_ctr_y) = u_ctr

	# unpack c; a circle is a center point and a radius (and a point is still an ordered pair of co-ordinates)
	(v_ctr, v_rad) = v
	(v_ctr_x, v_ctr_y) = v_ctr

	# collision if the distance between the centers is less than or equal to the sum of the radii
	distance_between_centers = math.sqrt(((v_ctr_x - u_ctr_x) ** 2 + (v_ctr_y - u_ctr_y) ** 2))
	
	return distance_between_centers <= (v_rad + u_rad), distance_between_centers
	
	
	
def blit_with_rotation(surface, image, position, angle):
	
	# rotate the image by the angle parameter
	rotated_image = pygame.transform.rotate(image, angle)
	
	# get a new drawing rectangle centered on the position parameter (i.e., for the original image)
	rect = rotated_image.get_rect(center = position)
	
	# blit the rotated image and return
	surface.blit(rotated_image, rect)
	return surface	
	
	
	
# required for multiprocessing
if __name__ == '__main__':

	# check for incorrect number of command line arguments
	if len(sys.argv) != 3:
		print()
		print("To use 'Glad_AI_tors' from the command line, you must provide the file names that")
		print("contain the red and blue A.I.s (respectively) as a pair of command line arguments.")
		print()
		print("Example: python glad_ai_tors.py comp1501_123123123_a3.py comp1501_456456456_a3.py")
		print()
		sys.exit()
		
	# initialize pygame and the font module and create a font
	pygame.init()
	pygame.font.init()
	myfont = pygame.font.SysFont('Courier New', 18)
	mysmallfont = pygame.font.SysFont('Arial', 16)
	
	# create the clock
	clock = pygame.time.Clock()
	
	# create the window surface
	window_surf = pygame.display.set_mode((window_size, window_size))	
	pygame.display.set_caption('Glad..AI..tors')
	
	# create the surface onto which all elements will be blitted, and a background image surface of the same size
	# n.b., it doesn't really need to be square, but I will keep it square for the time being
	foregd_surf = pygame.Surface((game_world_size, game_world_size))

	# create a surface to hold the background image
	backgd_surf = pygame.Surface((game_world_size, game_world_size))
	
	# load the image assets for creating the background surface
	image_assets = {}
	image_assets['_______'] = pygame.image.load("Assets/error.png")	
	image_assets['empty_1'] = pygame.image.load("Assets/tileGrass1.png")
	image_assets['empty_2'] = pygame.image.load("Assets/tileGrass2.png")	
	image_assets['road_NS'] = pygame.image.load("Assets/tileGrass_roadNorth.png")	
	image_assets['road_EW'] = pygame.image.load("Assets/tileGrass_roadEast.png")	
	image_assets['crnr_NE'] = pygame.image.load("Assets/tileGrass_roadCornerUR.png")	
	image_assets['crnr_NW'] = pygame.image.load("Assets/tileGrass_roadCornerUL.png")	
	image_assets['crnr_SE'] = pygame.image.load("Assets/tileGrass_roadCornerLR.png")	
	image_assets['crnr_SW'] = pygame.image.load("Assets/tileGrass_roadCornerLL.png")	
	image_assets['tee_NSE'] = pygame.image.load("Assets/tileGrass_roadSplitE.png")	
	image_assets['tee_NSW'] = pygame.image.load("Assets/tileGrass_roadSplitW.png")	
	image_assets['tee_EWN'] = pygame.image.load("Assets/tileGrass_roadSplitN.png")	
	image_assets['tee_EWS'] = pygame.image.load("Assets/tileGrass_roadSplitS.png")	
	image_assets['xroad_1'] = pygame.image.load("Assets/tileGrass_roadCrossing.png")	
	image_assets['xroad_2'] = pygame.image.load("Assets/tileGrass_roadCrossingRound.png")	
	image_assets['fence_N'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt40.png"), (tile_size, tile_size))
	image_assets['fence_S'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt04.png"), (tile_size, tile_size))
	image_assets['fence_E'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt21.png"), (tile_size, tile_size))
	image_assets['fence_W'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt23.png"), (tile_size, tile_size))
	image_assets['bend_NE'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt28.png"), (tile_size, tile_size))
	image_assets['bend_NW'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt27.png"), (tile_size, tile_size))
	image_assets['bend_SE'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt46.png"), (tile_size, tile_size))
	image_assets['bend_SW'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt45.png"), (tile_size, tile_size))
	image_assets['bar_crc'] = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt_pillar.png").convert_alpha(), (tile_size * 2, tile_size * 2))	
	image_assets['chas_rd'] = pygame.image.load("Assets/tankBody_red_outline.png")
	image_assets['chas_bl'] = pygame.image.load("Assets/tankBody_blue_outline.png")
	image_assets['weap_rd'] = pygame.image.load("Assets/specialBarrel3_red_outline.png")
	image_assets['weap_bl']	= pygame.image.load("Assets/specialBarrel3_blue_outline.png")
	image_assets['expln_1']	= pygame.image.load("Assets/explosion1.png")
	image_assets['expln_2']	= pygame.image.load("Assets/explosion2.png")	
	image_assets['expln_3']	= pygame.image.load("Assets/explosion3.png")
	image_assets['expln_4']	= pygame.image.load("Assets/explosion4.png")
	image_assets['expln_5']	= pygame.image.load("Assets/explosion5.png")

	# the list of instances of the armour class, for storing the combatants
	armours = []
	number_of_armours = 2
	initial_location_list = [(random.randint(100, 300), random.randint(100, 1180)), (random.randint(980, 1180), random.randint(100, 1180))]
	source_code_file_list = [sys.argv[1].replace(".py", ""), sys.argv[2].replace(".py", "")] 
	
	
	
	for i in range(number_of_armours):
		
		file = open(source_code_file_list[i]+".py", "r")
		data = file.readline().strip()
		file.close()
		if data[0:2] == "#<" and data[len(data)-1] == ">":
			data = data.rstrip(">")
			armours.append(Armour(data[2:14].center(12), source_code_file_list[i], i, initial_location_list[i]))
		else:
			armours.append(Armour("Untitled".center(12), source_code_file_list[i], i, initial_location_list[i]))
			
		
	# the list of instances of the pillar class, which are the randomly placed obstacles
	pillars = []
	number_of_pillars = 3
	for i in range(number_of_pillars):
		x = (game_world_size / 2) + (192 * random.randint(-1, 1))
		y = (game_world_size / 2) - 192 + (192 * i)
		pillars.append(Pillar((x, y)))
		
	# the list of instances of the rocket class, which are the active weapons
	rockets = []

	# the list of instances of the impact class, which are animated explosion sprites
	impacts = []

	# lists where the authors can put lines or text for debugging purposes
	debug_lines = []
	debug_texts = []
		
	# initialize an empty two-dimensional list for holding the randomly-generated background image
	backgd_map = []
	for i in range(game_world_size // tile_size):
		backgd_row = []
		for j in range(game_world_size // tile_size):
			backgd_row.append(False)
		backgd_map.append(backgd_row)
		
	# initialize a drunkard's walk starting near the center of either the top row or the leftmost column
	(drunk_row, drunk_col, drunk_dir) = random.choice( [(random.choice([8, 11]), 0, (0, 1)), (0, random.choice([8, 11]), (1, 0))] )
	
	# to force the drunkard to "carve" paths without short segments, maintain a cooldown timer whenever the drunkard gets a new direction
	drunk_tmr = 3

	drunk_end = False
	drunk_len = 0
	while True:

		# once the drunkard has "carved" 64 units out of the total 400, finish the current segment of the walk and then flag for break
		if drunk_len == 96:
			drunk_end = True
			
		# whenever the drunkard walks off the edge of the map, either break (on flag) or start a new drunkard's walk
		if drunk_row < 0 or drunk_row > 19 or drunk_col < 0 or drunk_col > 19:
			if drunk_end:
				break
			(drunk_row, drunk_col, drunk_dir) = random.choice( [(random.choice([5, 8, 11, 14]), 0, (0, 1)), (0, random.choice([5, 8, 11, 14]), (1, 0))] )
			drunk_tmr = 3
			
		# when the cooldown timer reachers zero, with a small probability the drunkard changes (but never reverses) direction 
		elif (drunk_tmr == 0 and random.random() < 0.4):
			drunk_dir = random.choice( [i for i in [(-1, 0), (0, 1), (1, 0), (0, -1)] if i != drunk_dir and i != tuple([j * -1 for j in drunk_dir])] )
			drunk_tmr = 3
		
		# otherwise just continue "carving" the paths for the background roads
		else:
			if not backgd_map[drunk_row][drunk_col]:
				backgd_map[drunk_row][drunk_col] = True
				drunk_len += 1
			drunk_row += drunk_dir[0]
			drunk_col += drunk_dir[1]
			drunk_tmr -= 1

			
	
	# visit inner elements of the map (i.e., those not on the edge) and blit the corresponding tile to make the background image
	for row in range(1, len(backgd_map) - 1):
		for col in range(1, len(backgd_map[0]) - 1):
			if backgd_map[row][col]:
				road_N = backgd_map[row - 1][col]
				road_S = backgd_map[row + 1][col]
				road_E = backgd_map[row][col + 1]
				road_W = backgd_map[row][col - 1]
				if road_N and road_S and road_E and road_W:
					next_tile = random.choice([image_assets['xroad_1'], image_assets['xroad_2']])
				elif not road_N and road_S and road_E and road_W:
					next_tile = image_assets['tee_EWS']
				elif road_N and not road_S and road_E and road_W:
					next_tile = image_assets['tee_EWN']
				elif road_N and road_S and not road_E and road_W:
					next_tile = image_assets['tee_NSW']
				elif road_N and road_S and road_E and not road_W:
					next_tile = image_assets['tee_NSE']					
				elif road_N and not road_S and road_E and not road_W:
					next_tile = image_assets['crnr_NE']
				elif road_N and not road_S and not road_E and road_W:
					next_tile = image_assets['crnr_NW']
				elif not road_N and road_S and road_E and not road_W:
					next_tile = image_assets['crnr_SE']
				elif not road_N and road_S and not road_E and road_W:
					next_tile = image_assets['crnr_SW']
				elif road_N and road_S and not road_E and not road_W:
					next_tile = image_assets['road_NS']
				elif not road_N and not road_S and road_E and road_W:
					next_tile = image_assets['road_EW']				
				else:
					next_tile = image_assets['badtile']
			else:
				next_tile = random.choice([image_assets['empty_1'], image_assets['empty_2']])
			backgd_surf.blit(next_tile, (col * tile_size, row * tile_size))

	# now visit the outer elements (i.e., those that are on the edge) and blit the corresponding barrier tiles
	for row in range(1, len(backgd_map) - 1):
		backgd_surf.blit(image_assets['fence_W'], ( 0 * tile_size, row * tile_size))
		backgd_surf.blit(image_assets['fence_E'], (19 * tile_size, row * tile_size))

	for col in range(1, len(backgd_map[0]) - 1):
		backgd_surf.blit(image_assets['fence_N'], (col * tile_size,  0 * tile_size))
		backgd_surf.blit(image_assets['fence_S'], (col * tile_size, 19 * tile_size))
			
	backgd_surf.blit(image_assets['bend_NW'], ( 0 * tile_size,  0 * tile_size))
	backgd_surf.blit(image_assets['bend_SW'], ( 0 * tile_size, 19 * tile_size))
	backgd_surf.blit(image_assets['bend_NE'], (19 * tile_size,  0 * tile_size))
	backgd_surf.blit(image_assets['bend_SE'], (19 * tile_size, 19 * tile_size))	
	
	#backgd_pillar_image = pygame.transform.smoothscale(pygame.image.load("Assets/road_asphalt_pillar.png").convert_alpha(), (tile_size * 2, tile_size * 2))	
	for pillar in pillars:
		backgd_surf.blit(image_assets['bar_crc'], (pillar.x - tile_size, pillar.y - tile_size))

		

	# the queue required for sharing data between the processes and this main program
	manager = multiprocessing.Manager()
	queue = manager.Queue()
	
	# the processes for the competitors are created and started
	processes = []
	for i in range(number_of_armours):

		environment = construct_environmental_data(i)
		processes.append(multiprocessing.Process(target = update, args = (environment, armours[i].num, armours[i].source_module, armours[i].current_state, queue,)))
		processes[i].start()
	
	
	
	# this is the main loop which can be terminated from the close button in the top corner
	closed_flag = False
	while not closed_flag:
	
		# this just checks if the close button was pressed
		for event in pygame.event.get():
			if event.type == QUIT:
				closed_flag = True

		# for each of the competitor processes
		for i in range(number_of_armours):
		
			# if the process has finished then that competitors finite state machine can report
			# the status of its effector registers and is ready to move to the next state 
			if not processes[i].is_alive():
			
				# presumably it is possible for more than one process to have finished before this
				# line is executed, so empty the queue of shared memory and use it to move each  
				# finite state machine that has finished its current state into its next state 
				while not queue.empty():
					(index, (state, effectors)) = queue.get()
					armours[index].current_state = state
					# the effectors of each agent are used to do the updating of the environment
					armours[index].effector_dict = effectors
				
				# process every key in the effector dictionary
				for key in armours[i].effector_dict:				

					# strip the key and convert to uppercase, just in case students are not following instructions
					key = key.strip().upper()
				
					if key.lower() in "abcdefghij" and (isinstance(armours[i].effector_dict[key], (bool, int, float)) or (isinstance(armours[i].effector_dict[key], str) and len(armours[i].effector_dict[key]) == 1)) :
					
						# this is the only way for a submission to "save" from one frame to the next; n.b., storage is _very_ limited
						armours[i].register_dict[key.lower()] = armours[i].effector_dict[key]				
				
				# replace the dead process with a new process corresponding to the next state of
				# that particular finite state machine and start that process
				environment = construct_environmental_data(i)
				processes[i] = multiprocessing.Process(target = update, args = (environment, armours[i].num, armours[i].source_module, armours[i].current_state, queue,))
				processes[i].start()
			
			
		# the effectors of each armour are checked and the attributes of the armours are adjusted
		#for armour in armours:
		for i in range(number_of_armours):
		
			firing_the_weapon = False
			firing_angle = 0
			
			# process every key in the effector dictionary
			for key in armours[i].effector_dict:

				# strip the key and convert to uppercase, just in case students are not following instructions
				key = key.strip().upper()
				
				# these are the flags for whether the combatant is charging/repairing/shielding
				is_charge_active = False
				is_repair_active = False
				is_shield_active = False
				
				# if key.lower() in "abcdefghij" and (isinstance(armours[i].effector_dict[key], (bool, int, float)) or (isinstance(armours[i].effector_dict[key], str) and len(armours[i].effector_dict[key]) == 1)) :
				
					# # this is the only way for a submission to "save" from one frame to the next; n.b., storage is _very_ limited
					# armours[i].register_dict[key.lower()] = armours[i].effector_dict[key]
				
				if key == "KABOOM" and isinstance(armours[i].effector_dict[key], (bool, int)):
				
					# since a desctroyed tank will cause damage to things within a small radius, suicide missions are a possible strategy
					if armours[i].effector_dict["KABOOM"]:				
						armours[i].dmg = 100

				elif key == "LAUNCH" and isinstance(armours[i].effector_dict[key], (bool, int)):
				
					# a "LAUNCH" key is first set to false, and then a new rocket is created with the corresponding position, angle, owner, and power level
					if armours[i].effector_dict["LAUNCH"]:
						firing_the_weapon = True
						firing_angle = armours[i].aim
						armours[i].effector_dict["LAUNCH"] = False
					
				elif key == "CHARGE" and isinstance(armours[i].effector_dict[key], (bool, int)):
				
					# a "CHARGE" key activates or deactivates the weapon charging functionality
					if armours[i].effector_dict["CHARGE"]:
						armours[i].charge_is_on = True
					else:
						armours[i].charge_is_on = False
					
				elif key == "SHIELD" and isinstance(armours[i].effector_dict[key], (bool, int)):
				
					# a "SHIELD" key activates or deactivates the shield functionality
					if armours[i].effector_dict["SHIELD"]:
						armours[i].shield_is_on = True
					else:
						armours[i].shield_is_on = False

				elif key == "ROT_CW" and isinstance(armours[i].effector_dict[key], (int, float)) and (0 <= armours[i].effector_dict[key] <= 1):

					# rotate the weapon in a clockwise direction
					armours[i].aim = (armours[i].aim - armours[i].effector_dict[key]) % 360
					
				elif key == "ROT_CC" and isinstance(armours[i].effector_dict[key], (int, float)) and (0 <= armours[i].effector_dict[key] <= 1):

					# rotate the weapon in a counterclockwise direction
					armours[i].aim = (armours[i].aim + armours[i].effector_dict[key]) % 360
					
				elif key == "ACLT_X" and isinstance(armours[i].effector_dict[key], (int, float)) and (-1 <= armours[i].effector_dict[key] <= 1):
				
					# change the horizontal acceleration of the armour
					armours[i].ddx = armours[i].effector_dict[key] * 0.2
					
				elif key == "ACLT_Y" and isinstance(armours[i].effector_dict[key], (int, float)) and (-1 <= armours[i].effector_dict[key] <= 1):
				
					# change the vertical acceleration of the armour
					armours[i].ddy = armours[i].effector_dict[key] * 0.2

				elif key == "D_LINE" and isinstance(armours[i].effector_dict[key], tuple):
				
					debug_lines.append(armours[i].effector_dict[key])

				elif key == "D_TEXT" and isinstance(armours[i].effector_dict[key], str):
				
					debug_texts.append((armours[i].effector_dict[key], i))
					
			if firing_the_weapon:
				rockets.append(Rocket((armours[i].x, armours[i].y), firing_angle, i, armours[i].pwr))
				armours[i].pwr = 1
			
			# both the charge and shield functions place a crippling upper bound on both acceleration and velocity
			armours[i].max = 1.0
			
			if armours[i].charge_is_on:
				armours[i].max -= 0.3
				armours[i].pwr = armours[i].pwr + 1

			if armours[i].shield_is_on:
				armours[i].max -= 0.3

								

								
			# the actual updating (position, velocity, weapon power level, etc.) is performed
			adjusted_ddx = armours[i].ddx * armours[i].max
			adjusted_ddy = armours[i].ddy * armours[i].max

			armours[i].dx = (armours[i].dx + adjusted_ddx) * 0.92 * armours[i].max
			armours[i].dy = (armours[i].dy + adjusted_ddy) * 0.92 * armours[i].max

			armours[i].x = armours[i].x + armours[i].dx
			armours[i].y = armours[i].y + armours[i].dy				


			
			# detect and respond to collisions between tanks
			has_collided, distance_between_centers = detect_collision_circle_circle(((armours[0].x, armours[0].y), armours[0].rad), ((armours[1].x, armours[1].y), armours[1].rad))
			if has_collided:

				collision_damage = math.sqrt((armours[0].dx - armours[1].dx) ** 2 + (armours[0].dy - armours[1].dy) ** 2)
				armours[0].dmg += collision_damage
				armours[1].dmg += collision_damage
				
				n_mag = (armours[0].rad + armours[1].rad)
				
				n_x = (armours[0].x - armours[1].x) / distance_between_centers
				n_y = (armours[0].y - armours[1].y) / distance_between_centers

				p = ((n_x * armours[0].dx) + (n_y * armours[0].dy)) - ((n_x * armours[1].dx) + (n_y * armours[1].dy))
				
				armours[0].x = armours[1].x + (n_mag / distance_between_centers) * (armours[0].x - armours[1].x)
				armours[0].y = armours[1].y + (n_mag / distance_between_centers) * (armours[0].y - armours[1].y)				

				armours[1].x = armours[0].x + (n_mag / distance_between_centers) * (armours[1].x - armours[0].x)
				armours[1].y = armours[0].y + (n_mag / distance_between_centers) * (armours[1].y - armours[0].y)	
				
				armours[0].dx = armours[0].dx - p * n_x
				armours[0].dy = armours[0].dy - p * n_y

				armours[1].dx = armours[1].dx + p * n_x
				armours[1].dy = armours[1].dy + p * n_y							

				armours[0].ddx = 0
				armours[0].ddy = 0
				
				armours[1].ddx = 0
				armours[1].ddy = 0
				

				
				
			# detect and respond to collisions with the pillars
			for j in range(number_of_pillars):
			
				has_collided, distance_between_centers = detect_collision_circle_circle(((armours[i].x, armours[i].y), armours[i].rad), ((pillars[j].x, pillars[j].y), pillars[j].rad))
				if has_collided:

					collision_damage = math.sqrt(armours[i].dx ** 2 + armours[i].dy ** 2)
					armours[i].dmg += collision_damage

					n_mag = (pillars[j].rad + armours[i].rad)
					
					n_x = (armours[i].x - pillars[j].x) / n_mag
					n_y = (armours[i].y - pillars[j].y) / n_mag
				
					n_dot_v = (n_x * armours[i].dx) + (n_y * armours[i].dy) 
				
					armours[i].x = pillars[j].x + (n_mag / distance_between_centers) * (armours[i].x - pillars[j].x)
					armours[i].y = pillars[j].y + (n_mag / distance_between_centers) * (armours[i].y - pillars[j].y)
				
					armours[i].dx = armours[i].dx - 2 * n_dot_v * n_x
					armours[i].dy = armours[i].dy - 2 * n_dot_v * n_y			

					armours[i].ddx = 0
					armours[i].ddy = 0
					
					break
					
			# detect and respond to collisions with the walls
			
			has_collided = False
			
			if (armours[i].x - armours[i].rad) < tile_size:
				has_collided = True
				armours[i].x = tile_size + armours[i].rad
				armours[i].dx *= -1
				armours[i].ddx = 0

			if (armours[i].x + armours[i].rad) >= game_world_size - tile_size:
				has_collided = True
				armours[i].x = game_world_size - tile_size - armours[i].rad
				armours[i].dx *= -1
				armours[i].ddx = 0

			if (armours[i].y - armours[i].rad) < tile_size:
				has_collided = True
				armours[i].y = tile_size + armours[i].rad
				armours[i].dy *= -1
				armours[i].ddy = 0
				
			if (armours[i].y + armours[i].rad) >= game_world_size - tile_size:				
				has_collided = True
				armours[i].y = game_world_size - tile_size - armours[i].rad
				armours[i].dy *= -1
				armours[i].ddy = 0				

			if has_collided:
				collision_damage = math.sqrt(armours[i].dx ** 2 + armours[i].dy ** 2)
				armours[i].dmg += collision_damage			
			
		
		# the updating for the rocket position and velocity is now done
		for i in range(len(rockets)-1, -1, -1):
		
			rockets[i].sol_x = rockets[i].eol_x
			rockets[i].sol_y = rockets[i].eol_y

			rockets[i].eol_x = rockets[i].eol_x + rockets[i].dx
			rockets[i].eol_y = rockets[i].eol_y + rockets[i].dy

			# a rocket can collide with the walls to the north, south, east, and west
			if rockets[i].eol_x < (0 + tile_size) or rockets[i].eol_y < (0 + tile_size) or rockets[i].eol_x >= (game_world_size - tile_size) or rockets[i].eol_y >= (game_world_size - tile_size):
			
				# remove that rocket
				impacts.append(Impact((rockets[i].eol_x, rockets[i].eol_y)))
				rockets.pop(i)
				break
				
			else:
			
				# a rocket is not permitted to collide with the combatant that fired it
				if rockets[i].owner == 0:
					j = 1
				else:
					j = 0
				
				has_collided, _ = detect_collision_line_circle(((rockets[i].sol_x, rockets[i].sol_y), (rockets[i].eol_x, rockets[i].eol_y)), ((armours[j].x, armours[j].y), armours[j].rad)) 
				if has_collided:

					# if the armour has its shield on the damage is reduced by 20%
					if armours[j].shield_is_on:
						armours[j].dmg = min(armours[j].dmg + int(rockets[i].power * 0.8), 100)
					else:
						armours[j].dmg = min(armours[j].dmg + rockets[i].power, 100)
						
					# remove that rocket
					impacts.append(Impact((rockets[i].eol_x, rockets[i].eol_y)))
					rockets.pop(i)
					break

				else:
				
					for j in range(number_of_pillars):
					
						has_collided, _ = detect_collision_line_circle(((rockets[i].sol_x, rockets[i].sol_y), (rockets[i].eol_x, rockets[i].eol_y)), ((pillars[j].x, pillars[j].y), pillars[j].rad)) 
						if has_collided:

							# remove that rocket
							impacts.append(Impact((rockets[i].eol_x, rockets[i].eol_y)))
							rockets.pop(i)
							break

							
							
		# enforce the constraint that pwr, dmg, etc. are in (0, 100)
		for i in range(number_of_armours):
			armours[i].pwr = int(max(min(armours[i].pwr, 100), 0))
			armours[i].dmg = int(max(min(armours[i].dmg, 100), 0))
			
		# that match ends when one or more tanks have 100% damage or if 3 minutes have elapsed
		match_has_ended = False
		if (armours[0].dmg == 100 and armours[1].dmg == 100) or pygame.time.get_ticks() > 180000:
			print("No Winner", "No Winner", 100-armours[0].dmg, 100-armours[1].dmg, pygame.time.get_ticks(), sep = ',')
			match_has_ended = True
		elif armours[0].dmg == 100:
			print(armours[1].source_module, armours[1].who, 100-armours[0].dmg, 100-armours[1].dmg, pygame.time.get_ticks(), sep = ',')
			match_has_ended = True
		elif armours[1].dmg == 100:
			print(armours[0].source_module, armours[0].who, 100-armours[0].dmg, 100-armours[1].dmg, pygame.time.get_ticks(), sep = ',')
			match_has_ended = True
			
		if match_has_ended:
			for i in range(number_of_armours):
				processes[i].terminate()
			pygame.quit()
			sys.exit()
	
	
		# prepare the camera surface for rendering, starting with the background surface image
		foregd_surf.blit(backgd_surf, (0, 0))
		
		# rotate and then blit the chassis and weapon sprites for both the red and the blue armours
		foregd_surf = blit_with_rotation(foregd_surf, image_assets['chas_rd'], (armours[0].x, armours[0].y), math.degrees(math.atan2(-armours[0].dy, armours[0].dx)))
		foregd_surf = blit_with_rotation(foregd_surf, image_assets['weap_rd'], (armours[0].x, armours[0].y), armours[0].aim)

		foregd_surf = blit_with_rotation(foregd_surf, image_assets['chas_bl'], (armours[1].x, armours[1].y), math.degrees(math.atan2(-armours[1].dy, armours[1].dx)))
		foregd_surf = blit_with_rotation(foregd_surf, image_assets['weap_bl'], (armours[1].x, armours[1].y), armours[1].aim)
		
		# create a new rectangle object to use for drawing the power and damage meters beneath each tank
		power_or_damage_meter = Rect(0, 0, 0, 6)
		for i in range(number_of_armours):
			
			power_or_damage_meter.height = 6
			
			power_or_damage_meter.width = int (40 * (armours[i].pwr / 100))
			power_or_damage_meter.center = (armours[i].x, armours[i].y + 36)
			pygame.draw.rect(foregd_surf, (0, 255, 0), power_or_damage_meter)

			power_or_damage_meter.width = int (40 * ((100 - armours[i].dmg) / 100))
			power_or_damage_meter.center = (armours[i].x, armours[i].y + 44)
			pygame.draw.rect(foregd_surf, (255, 255, 0), power_or_damage_meter)
		
			foregd_surf.blit(myfont.render(armours[i].who, True, (0, 0, 0)), (armours[i].x - 66, armours[i].y - 50))
		
		# draw a line for each of the rockets
		for rocket in rockets:
			pygame.draw.aaline(foregd_surf, (0, 0, 0), (int(rocket.sol_x), int(rocket.sol_y)), (int(rocket.eol_x), int(rocket.eol_y)), 4)
			
		# draw any debugging lines	
		for line in debug_lines:	
			try:
				pygame.draw.aaline(foregd_surf, (255, 0, 0), (int(line[0][0]), int(line[0][1])), (int(line[1][0]), int(line[1][1])), 4)
			except:
				print("ERROR: Could not draw the debug line stored as:", line)
				
		debug_lines.clear()		
			
		# blit any debugging text
		for text in debug_texts:	
			try:
				text_sfc = mysmallfont.render('"'+text[0]+'"', True, (255, 0, 0))
				(text_wid, text_hgt) = text_sfc.get_size()
				foregd_surf.blit(text_sfc, (armours[text[1]].x - (text_wid//2), armours[text[1]].y - 80))
			except:
				print("ERROR: Could not write the debug text stored as:", text)
				
		debug_texts.clear()					
			
		# draw (and advance the frame) the animated impact sprites, removing them if they have finished
		for i in range(len(impacts)-1, -1, -1):
		
			impacts[i].frame_delay -= frame_rate
			
			if impacts[i].frame_delay < 0:
				impacts[i].frame_delay += 100
				impacts[i].frame_index += 1
				
			if impacts[i].frame_index <= 5:
				frame_image_key = 'expln_' + str(impacts[i].frame_index)
				rect = image_assets[frame_image_key].get_rect()
				rect.center = (impacts[i].x, impacts[i].y)
				foregd_surf.blit(image_assets[frame_image_key], rect)
			else:
				impacts.pop(i)
				break

		# the camera size is the larger of the difference between the x and y co-ordinates of the combatants, plus a small margin
		camera_size = max(window_size // 1, max(abs(armours[0].x - armours[1].x), abs(armours[0].y - armours[1].y)) + 2 * tile_size)
		
		# the camera zoom is the factor that camera_size must be multiplied by to produce window_size as the product
		camera_zoom = window_size / camera_size
		
		# the top left position of the camera is computed using the average of the combatant positions as the center
		foregd_lft = int(camera_zoom * (((armours[0].x + armours[1].x) // 2) - camera_size // 2))
		foregd_top = int(camera_zoom * (((armours[0].y + armours[1].y) // 2) - camera_size // 2))
		foregd_dim = int(camera_zoom * camera_size)
	
		# prepare the window_surface for rendering by filling with the background colour of the outer barrier tiles
		window_surf.fill((164, 199, 201))
		
		# finally blit the camera view onto the window  
		window_surf.blit(pygame.transform.smoothscale(foregd_surf, (int(camera_zoom * game_world_size), int(camera_zoom * game_world_size))), (0, 0), (foregd_lft, foregd_top, foregd_dim, foregd_dim))
		
		# the frame rate is capped at 80 frames per second
		pygame.display.update()
		clock.tick(frame_rate)
		
	# the loop has ended so terminate the processes
	for i in range(number_of_armours):
		processes[i].terminate()
	