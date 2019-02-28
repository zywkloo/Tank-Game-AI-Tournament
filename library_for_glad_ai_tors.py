from time import sleep
from math import cos, sin, tan, acos, asin, atan, atan2, degrees, radians, sqrt, pow, floor, ceil
from random import random

def get_position(arg):
	return (arg['x'], arg['y'])
	
def get_velocity(arg):
	return (arg['dx'], arg['dy'])


def get_n_border(arg):
	return arg['n_border']

def get_s_border(arg):
	return arg['s_border']

def get_e_border(arg):
	return arg['e_border']

def get_w_border(arg):
	return arg['w_border']


def get_weapon_angle(arg):
	return arg['aim']

def get_weapon_power(arg):
	return arg['pwr']
	
def get_damage_level(arg):
	return arg['dmg']
	
def is_charge_active(arg):
	return arg['charge']

def is_shield_active(arg):
	return arg['shield']

def get_saved_data(arg, register_name):
    if register_name.lower() in "abcdefghij":
        return arg[register_name.lower()]
    else:
        return None
	
def get_radar_data(arg, radar_angle):

	u_sol_x = arg['x']
	u_sol_y = arg['y']
	u_eol_x = u_sol_x + cos(radians(radar_angle))
	u_eol_y = u_sol_y - sin(radians(radar_angle))

	detectables = []
	detectables.append( ("opponent", arg['inaccessible_register_for_opponent']) )
	detectables.append( ("obstacle", arg['inaccessible_register_for_pillar_0']) )
	detectables.append( ("obstacle", arg['inaccessible_register_for_pillar_1']) )
	detectables.append( ("obstacle", arg['inaccessible_register_for_pillar_2']) )
	
	nearest_of_every_detectable = None
	squared_distance_to_nearest = 0
	
	for detectable in detectables:
	
		(v_ctr_x, v_ctr_y, v_rad) = detectable[1]

		# the equation for all points on the line segment u can be considered u = u_sol + t * (u_eol - u_sol), for t in [0, 1]
		# the center of the circle and the nearest point on the line segment (that which we are trying to find) define a line 
		# that is is perpendicular to the line segment u (i.e., the dot product will be 0); in other words, it suffices to take
		# the equation v_ctr - (u_sol + t * (u_eol - u_sol)) · (u_evol - u_sol) and solve for t
		t = ((v_ctr_x - u_sol_x) * (u_eol_x - u_sol_x) + (v_ctr_y - u_sol_y) * (u_eol_y - u_sol_y)) / ((u_eol_x - u_sol_x) ** 2 + (u_eol_y - u_sol_y) ** 2)

		# this t can be used to find the nearest point w on the infinite line between u_sol and u_sol, but the line is actually 
		# a ray emitted in the direction the radar is pointed, so t must be nonnegative (i.e., the ray cannot go backward)
		t = max(t, 0)
		
		# so the nearest point on the line segment, w, is defined as
		w_x = u_sol_x + t * (u_eol_x - u_sol_x)
		w_y = u_sol_y + t * (u_eol_y - u_sol_y)

		# measure the distance between u and w
		squared_distance_from_u_to_w = (w_x - u_sol_x) ** 2 + (w_y - u_sol_y) ** 2

		# if no nearest has been found yet or if the current detectable is nearest so far
		if nearest_of_every_detectable == None or squared_distance_from_u_to_w < squared_distance_to_nearest:
		
			# find the squared distance between w and v
			squared_distance_from_w_to_v = (w_x - v_ctr_x) ** 2 + (w_y - v_ctr_y) ** 2
	
			# if the Eucliean distance squared is less than the radius squared then the ray has collided with a detectable
			if (squared_distance_from_w_to_v <= v_rad ** 2):
				
				nearest_of_every_detectable = detectable[0]
				squared_distance_to_nearest = squared_distance_from_u_to_w
	
	return (nearest_of_every_detectable, sqrt(squared_distance_to_nearest))
