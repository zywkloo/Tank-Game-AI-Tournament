#<Million Ants>
from library_for_glad_ai_tors import*
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs=False
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq=True
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExs=min
import math
import random 
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqx=random.uniform
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsEx=random.choice
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsEq=random.randint
nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs=300
def start(arg):
 return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqx",{'C':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsEq(4,6),'F':get_damage_level(arg)})
def nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqx(arg):
 nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE=[(+1,0),(-1,0),(0,+1),(0,-1)]
 (x,y)=get_position(arg)
 if x>(get_e_border(arg)-nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs):
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((+1,0))
 else:
  (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE)=get_radar_data(arg,0)
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx=="obstacle" and nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE<nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs:
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((+1,0))
 if y<(get_n_border(arg)+nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs):
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((0,-1))
 else:
  (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE)=get_radar_data(arg,90)
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx=="obstacle" and nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE<nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs:
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((0,-1))
 if x<(get_w_border(arg)+nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs):
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((-1,0))
 else:
  (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE)=get_radar_data(arg,180)
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx=="obstacle" and nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE<nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs:
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((-1,0))
 if y>(get_s_border(arg)-nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs):
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((0,+1))
 else:
  (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE)=get_radar_data(arg,270)
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsx=="obstacle" and nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqsE<nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxs:
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE.remove((0,+1))
 nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEx=nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsEx(nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqxE)
 return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE",{'A':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEx[0],'B':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEx[1],'C':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsEq(4,6),'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs})
def nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE(arg):
 nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs=get_saved_data(arg,'C')
 nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs-=1
 if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs<0 or(get_damage_level(arg)-get_saved_data(arg,'F')>5):
  return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqx",{'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'F':get_damage_level(arg)})
 else:
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs=nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs
  nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqE=0
  while nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqE<360:
   (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsq,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsE)=get_radar_data(arg,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqE)
   if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsq=="opponent":
    nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs=nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq
    break
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqE+=1
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs:
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq=((nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqE-get_weapon_angle(arg))+360)%360
   if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq>180:
    cc=0
    if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq>355:
     cw=0.1
    elif nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq>345:
     cw=0.3
    else:
     cw=1.0
   else:
    cw=0
    if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq<5:
     cc=0.1
    elif nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq<15:
     cc=0.3
    else:
     cc=1.0
   if(nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq<3 or nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxEq>357)and get_weapon_power(arg)>15:
    (x,y)=get_position(arg)
    return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsxE",{'C':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs,'F':get_damage_level(arg),'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'ACLT_X':-get_saved_data(arg,'A')/1.5,'ACLT_Y':-get_saved_data(arg,'B')/1.5,'ROT_CW':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExs(cc/1.5+nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqx(-0.05,0.05),0),'ROT_CC':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExs(cw/1.5+nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqx(-0.05,0.05),0)})
   else:
    return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE",{'C':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs,'D':cw,'E':cc,'F':get_damage_level(arg),'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'ACLT_X':get_saved_data(arg,'A'),'ACLT_Y':get_saved_data(arg,'B'),'ROT_CW':cw,'ROT_CC':cc})
  else:
   return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE",{'C':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLqEs,'F':get_damage_level(arg),'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'ACLT_X':get_saved_data(arg,'A'),'ACLT_Y':get_saved_data(arg,'B'),'ROT_CW':get_saved_data(arg,'D')/1.5,'ROT_CC':get_saved_data(arg,'E')/1.5}) 
def nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsxq(arg):
 nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs=nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs
 c=0
 while c<360:
  (nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsq,nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsE)=get_radar_data(arg,c)
  if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxsq=="opponent":
   nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs=nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq
   break
  c+=1
 if nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLxqs or get_weapon_power(arg)>80:
  return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE",{'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs})
 else:
  return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsxq",{'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq})
def nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsxE(arg):
 return("nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLsqE",{'LAUNCH':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLExq,'CHARGE':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,'SHIELD':nmhGwYBOiRIalrgeHPpUcAFouXSNtbvWCdzfykTQVjJMKDLEqs,})