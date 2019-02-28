#<Noob Noob>
from library_for_glad_ai_tors import*
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi=False
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYI=True
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkIi=max
import math
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkiY=math.sin
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIkY=math.radians
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIki=math.cos
import random 
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkiI=random.uniform
HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI=400
def start(arg):
 return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY=0
 while HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY<360:
  (HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIk,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzikY)=get_radar_data(arg,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY)
  if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIk=="opponent":
   HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYI
   break
  HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY+=0.1
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYI,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY,(HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzikY<150)
 else:
  return HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,0,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY,HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzikI=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  dx=+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIki(HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIkY(HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY))
  dy=-HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkiY(HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIkY(HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY))
  z=get_weapon_angle(arg)
  dz=((HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziIY-z)+360)%360
  cw=0
  cc=0
  if dz>180:
   cw=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkIi(0,0.4+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkiI(-0.3,+0.3))
  else:
   cc=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkIi(0,0.4+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkiI(-0.3,+0.3))
  HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYiI=(dz>350 or dz<10)
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'ACLT_X':dx,'ACLT_Y':dy,'ROT_CC':cc,'ROT_CW':cw,'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzikI and get_weapon_power(arg)<40,'SHIELD':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,'LAUNCH':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYiI})
 else:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYkI",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYkI(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,_,_=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 (x,y)=get_position(arg)
 if x<get_w_border(arg)+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
  if y<get_n_border(arg)+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
   return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIik",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi}) 
  elif y>get_s_border(arg)-HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
   return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIiY",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 else:
  if y<get_n_border(arg)+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
   return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYi",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi}) 
  elif y>get_s_border(arg)-HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
   return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYk",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 if x<get_e_border(arg)/2:
  dx=-1
 else:
  dx=+1
 if y<get_s_border(arg)/2:
  dy=-1
 else:
  dy=+1 
 return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYkI",{'ACLT_X':dx,'ACLT_Y':dy,'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIiY(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,_,_=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 (x,y)=get_position(arg)
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik=get_n_border(arg)
 if y<HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIik",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+1,"ACLT_Y":+0})
 else:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIiY",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+0,"ACLT_Y":-1})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIik(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,_,_=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 (x,y)=get_position(arg)
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik=get_e_border(arg)
 if x>=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik-HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYi",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+0,"ACLT_Y":+1})
 else:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIiY",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+1,"ACLT_Y":-0})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYi(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,_,_=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 (x,y)=get_position(arg)
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik=get_s_border(arg)
 if y>=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik-HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYk",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":-1,"ACLT_Y":+0})
 else:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYi",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+0,"ACLT_Y":+1})
def HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYk(arg):
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk,_,_=HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYIk(arg)
 if HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYk:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYki",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi})
 (x,y)=get_position(arg)
 HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik=get_w_border(arg)
 if x<HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzYik+HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBziYI:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIiY",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":+0,"ACLT_Y":-1})
 else:
  return("HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzIYk",{'CHARGE':HtugUCacFqGrmWpRxPOMlAXoNfdLnyEVwDsSeQKjvJTbhBzkYi,"ACLT_X":-1,"ACLT_Y":+0})