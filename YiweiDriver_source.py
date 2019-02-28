#<Yiwei.Driver>
# ============================================================  
# 
# Student Name (as it appears on cuLearn): Yiwei Zhang          
# Student ID (9 digits in angle brackets): <101071022>               
# Course Code (for this current semester): COMP1501A                
#                                                                   
# ============================================================


#location cmd for dev use: cd C:\Yiwei_Study_CS\COMP 1501\AS 3
#python Glad_AI_tors.py tier_1.py comp1501_w18_101071022_a3_source.py
#python Glad_AI_tors.py comp1501_000000000_a3 comp1501_w18_101071022_a3_source.py
#python Glad_AI_tors.py comp1501_000000001_a3 comp1501_w18_101071022_a3_source.py
#python Glad_AI_tors.py comp1501_000000002_a3 comp1501_w18_101071022_a3_source.py
#python Glad_AI_tors.py comp1501_w18_101071022_a3_source.py CWH 

'''
Register variables:
 'D': string,'E'or 'W'or 'N'or'S',  the present moving direction in wandering mode.
 'E': integer, the angle between enemy and your tank
 'F': bool, if enemy found in this frame
 'A':the power of bullets that have been shot during a certain time

'''
from library_for_glad_ai_tors import *

import math
import random

def start(arg):
	return ("WANDER", {'CHARGE': True,"ACLT_X": -1, "ACLT_Y": +0,'F':False,'D':'W','E':999999}) #initial move to N    [-1,+0]

def WANDER(arg):
	(x,y)=get_position(arg)
	borderw = get_w_border(arg)
	bordern = get_n_border(arg)
	bordere = get_e_border(arg)
	borders = get_s_border(arg)
	DirDic={'W':[-1,+0],'N':[+0,-1],'E':[+1,+0],'S':[+0,+1]}
	DirV=[-1,+0]
	Dnote=None
	CW='NUL'
	Enemy=False
	enemyangle=None
	# Tank move control
	if get_saved_data(arg, 'D')=='W':  #move to W
		if x < borderw + 200:
			DirV=[+0,-1]   	#move to N
			Dnote='N'
		else:
			DirV=DirDic[get_saved_data(arg, 'D')]
	elif get_saved_data(arg, 'D')=='N':  #move to N
		if y < bordern + 200:
			DirV=[+1,+0]   	#move to E
			Dnote='E'
		else:
			DirV=DirDic[get_saved_data(arg, 'D')]
	elif get_saved_data(arg, 'D')=='E':  #move to E
		if x >= bordere - 200:
			DirV=[+0,+1]   	#move to S
			Dnote='S'
		else:
			DirV=DirDic[get_saved_data(arg, 'D')]
	elif get_saved_data(arg, 'D')=='S':  #move to S
		if y >= borders - 200:
			DirV=[-1,+0]  	#move to W
			Dnote='W'
		else:
			DirV=DirDic[get_saved_data(arg, 'D')]
	
	# Tank cannon control
	if get_saved_data(arg, 'E')==999999:
		(Cx,Cy)=((bordere-borderw)/2,(borders-bordern)/2)
		centerangle= (-math.atan2(Cy-y, Cx-x) * 180/math.pi+180)%360
		aimangle=(centerangle-180)%360
	else:			#if the enemy has been found once, inherit the enemy angle
		aimangle=get_saved_data(arg, 'E')
		(Cx,Cy)=(x+600*math.cos(radians(aimangle)),y-600*math.sin(radians(aimangle)))
	
	
	if -20<(get_weapon_angle(arg)-aimangle)%360<20:
		CW='CNUL'
	elif (get_weapon_angle(arg)>aimangle and get_weapon_angle(arg)-aimangle<180 ) or (get_weapon_angle(arg)<aimangle and  get_weapon_angle(arg)+360-aimangle<180):
		CW='CW'
	else:
		CW="CC"

	# Tank Enemy Detection
	for angle_i in range(int(get_weapon_angle(arg))-30,360+int(get_weapon_angle(arg))-30):	
		if get_radar_data(arg, angle_i%360)[0]=='opponent':
			Enemy=True
			enemyangle=angle_i%360
			break
	#judge whether need charging
	if  get_weapon_power(arg)<100:
		needcharge=True
	else:
		needcharge=False

	#status return
	if Enemy :
		if CW=='CW':
			return ("COMBAT", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': False,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'F':Enemy,'ROT_CW':1,'D_TEXT':"COMBAT_CW",'D':Dnote,'E':enemyangle})#"COMBAT_CW!"
		elif CW=='CC':
			return ("COMBAT", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': False,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'F':Enemy,'ROT_CC':1,'D_TEXT':"COMBAT_CC",'D':Dnote,'E':enemyangle}) #"COMBAT_CC!"
		else:
			return ("COMBAT", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': False,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':"COMBAT_CNUL",'D':Dnote,'E':enemyangle}) #"COMBAT_CNUL!"
	else:

		if CW=='CW':
			return ("WANDER", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': needcharge,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'ROT_CW':1,'D_TEXT': "WANDER_CW!",'D':Dnote}) #"WANDER_CW!"
		elif CW=='CC':
			return ("WANDER", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': needcharge,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'ROT_CC':1,'D_TEXT': "WANDER_CC!",'D':Dnote}) #"WANDER_CC!"
		else:
			return ("WANDER", {'D_LINE':((x,y),((Cx,Cy))),'CHARGE': needcharge,"ACLT_X": DirV[0],'SHIELD': False, "ACLT_Y": DirV[1],'D_TEXT': "WANDER_CNUL!",'D':Dnote}) #"WANDER_CNUL!"



def COMBAT(arg):
	(x,y)=get_position(arg)
	(dx,dy)=get_velocity(arg)

	borderw = get_w_border(arg)
	bordern = get_n_border(arg)
	bordere = get_e_border(arg)
	borders = get_s_border(arg)
	##################   SCAN   ############# GET enemy information
	Enemy=False
	enemyangle=get_saved_data(arg, 'E')
	enemydist=999999
	min_obstacle=[999999,None]
	DirV=[0,0]
	for angle_i in range(360):	
		if get_radar_data(arg, angle_i%360)[0]=='opponent':
			Enemy=True
			enemydist_temp=get_radar_data(arg, angle_i%360)[1]
			if enemydist_temp<enemydist:
				enemydist=enemydist_temp
				enemyangle=angle_i%360
		elif get_radar_data(arg, angle_i%360)[0]=='obstacle' and int(get_radar_data(arg, angle_i%360)[1])< 120:#and  get_radar_data(arg, angle_i%360)[1]<30:
			obstacle_element=[int(get_radar_data(arg, angle_i%360)[1]),angle_i%360]
			# compare every obstacle's dist and angle 
			if obstacle_element[0]<min_obstacle[0]:
				min_obstacle=obstacle_element 
				#find the nearest obstacle

	##################   STATUS return   ############# if no enemy found return to wander mode
	if not Enemy:
		return ("WANDER", {'CHARGE': True,'LAUNCH': False,'D_TEXT': "WANDER_CNUL!",'D':'E'}) #"WANDER_CNUL!"

		#the coordinates of aiming line
	enemyradians=radians(enemyangle)
	weaponradians=radians(get_weapon_angle(arg))
	(ex,ey)=(x+enemydist*math.cos(enemyradians),y-enemydist*math.sin(enemyradians))
	(wx,wy)=(x+enemydist*math.cos(weaponradians),y-enemydist*math.sin(weaponradians))

	##################   MOVE INI  ################### to keep minimal distance against enemy when close ; forward to enemy or try to evade from bullet when far away 
	SHIELD=False
	if enemydist<100:
		runenemy_angle=(enemyangle-170)%360  #  the perpendicular line of the  aiming line
		DirV=[math.cos(radians(runenemy_angle)),-math.sin(radians(runenemy_angle))]
	elif 75<enemyangle<105 or 255<enemyangle<290  : 
		runenemy_angle=(enemyangle-random.choice((-90,90)))%360  #  evade the no.5 enemy
		DirV=[math.cos(radians(runenemy_angle)),-math.sin(radians(runenemy_angle))]		
	else:
		if math.cos(enemyradians)**2>math.sin(enemyradians)**2:
			if math.cos(enemyradians)>0:
				DirV=[1,-math.sin(enemyradians)/math.cos(enemyradians)]
			else:
				DirV=[-1,math.sin(enemyradians)/math.cos(enemyradians)]
		else:
			if math.sin(enemyradians)<0:
				DirV=[-math.cos(enemyradians)/math.sin(enemyradians),1]
			else:
				DirV=[math.cos(enemyradians)/math.sin(enemyradians),-1]			

		#SHIELD=False
	##################   MOVE adjustment  #############  once have shot some bullets ,move to evade bullets

	shotpower=get_saved_data(arg, 'A')


	##################   MOVE adjustment  #############  to keep distance against  obstacles
	if min_obstacle!= [999999,None]:
		runob_angle0=(min_obstacle[1]-180)%360  # the counterclockwise perpendicular line of the direction of an obstacle
		runob_radians=radians(runob_angle0)
		DirV=[math.cos(runob_radians),-math.sin(runob_radians)]
		# if math.cos(runob_radians)**2>math.sin(runob_radians)**2:
		# 	if math.cos(runob_radians)>0:
		# 		DirV=[1,-math.sin(runob_radians)/math.cos(runob_radians)]
		# 	else:
		# 		DirV=[-1,math.sin(runob_radians)/math.cos(runob_radians)]
		# else:
		# 	if math.sin(runob_radians)<0:
		# 		DirV=[-math.cos(runob_radians)/math.sin(runob_radians),1]
		# 	else:
		# 		DirV=[math.cos(runob_radians)/math.sin(runob_radians),-1]			
			

	##################   MOVE adjustment  #############  to keep minimal distance against boundaries
	if DirV[1]>=0:
		ACLT_Y=1
	else:
		ACLT_Y=-1
	if DirV[0]>=0:
		ACLT_X=1
	else:
		ACLT_X=-1
		
	if x < borderw + 150 :
		DirV=[+1,ACLT_Y] 	#move to N or S  and E
	if x >= bordere - 150:
		DirV=[-1,ACLT_Y]   	#move to N or S  and W
	if  y < bordern + 150 :
		DirV=[ACLT_X,+1]   #move to W or E and S
	if y>= borders - 150:
		DirV=[ACLT_X,-1]  #move to W or E and N



	##################   weapon adjustment  ############# weapon charging adjustment
	if get_weapon_power(arg)<100:
		needcharge=True
	else:
		needcharge=False
	
	##################   weapon adjustment  ############# weapon direction adjustment

	CWlist_Far=[(0,10,0.06),(10,20,0.15),(20,30,0.3),(30,180,1)]
	CClist_Far=[(350,360,0.2),(340,350,0.3),(330,340,0.5),(180,330,1)]
	CWlist_Mid=[(0,10,0.1),(10,20,0.3),(20,30,0.5),(30,180,1)]
	CClist_Mid=[(350,360,0.15),(340,350,0.3),(330,340,0.5),(180,330,1)]	
	CWlist_Near=[(0,10,0.15),(10,20,0.3),(20,30,0.5),(30,180,1)]
	CClist_Near=[(350,360,0.2),(340,350,0.3),(330,340,0.5),(180,330,1)]
	rotateangle=(get_weapon_angle(arg)-enemyangle)%360
	
	if enemydist >650:   #when the enemy is far away
		if (wx-ex)**2+(wy-ey)**2<=17*2:
			shotpower+=get_weapon_power(arg)
			if shotpower>50:
				evadeenemy_angle=(enemyangle-45)%360  
				DirV=[math.cos(radians(evadeenemy_angle)),-math.sin(radians(evadeenemy_angle))]
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':"LAUNCH",'E':enemyangle,'A':0})	
			else:
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,'CHARGE': needcharge,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'E':enemyangle,'A':shotpower}) #"COMBAT_RUN"
		
		if (wx-ex)**2+(wy-ey)**2<=6*2:
			return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
		elif 0<= rotateangle <180:		
			for inter_tuple in CWlist_Far:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CW':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
		else:
			for inter_tuple in CClist_Far:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return   ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CC':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 

	elif enemydist >250:
		if (wx-ex)**2+(wy-ey)**2<=17**2:
			shotpower+=get_weapon_power(arg)
			if shotpower>20:
				evadeenemy_angle=(enemyangle-45)%360  
				DirV=[math.cos(radians(evadeenemy_angle)),-math.sin(radians(evadeenemy_angle))]
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':"LAUNCH",'E':enemyangle,'A':0})	
			else:
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,'CHARGE': needcharge,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'E':enemyangle,'A':shotpower}) #"COMBAT_RUN
		if (wx-ex)**2+(wy-ey)**2<=3*2:
			return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
		elif 0<= rotateangle <180:		
			for inter_tuple in CWlist_Mid:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CW':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
		else:
			for inter_tuple in CClist_Mid:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return   ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CC':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
	else:
		if (wx-ex)**2+(wy-ey)**2<=17**2:
			shotpower+=get_weapon_power(arg)
			if shotpower>50:
				evadeenemy_angle=(enemyangle-45)%360  
				DirV=[math.cos(radians(evadeenemy_angle)),-math.sin(radians(evadeenemy_angle))]
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':"LAUNCH",'E':enemyangle,'A':0})	
			else:
				return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'LAUNCH': True,'SHIELD': SHIELD,'CHARGE': needcharge,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'E':enemyangle,'A':shotpower}) #"COMBAT_RUN"
	
		if (wx-ex)**2+(wy-ey)**2<=5*2:
			return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 		
		elif 0<= rotateangle <180:		
			for inter_tuple in CWlist_Near:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CW':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 
		else:
			for inter_tuple in CClist_Near:
				if inter_tuple[0]<= rotateangle <inter_tuple[1]:
					return   ("COMBAT", {'D_LINE':((x+int(24*dx),y+int(24*dy)),(wx,wy)),'CHARGE': needcharge,'LAUNCH': False,'SHIELD': SHIELD,"ACLT_X": DirV[0], "ACLT_Y": DirV[1],'F':Enemy,'ROT_CC':inter_tuple[2],'D_TEXT':str(enemyangle)+"'"+str(int(enemydist))+".M",'E':enemyangle}) 





