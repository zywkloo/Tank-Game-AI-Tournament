#<Crocu Bot>
from library_for_glad_ai_tors import*
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp=False
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV=True
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapD=range
import math
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVD=math.sqrt
import random 
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV=random.uniform
cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp=random.randint
def start(arg):
 (x,y)=get_position(arg)
 if x<640:
  if y<640:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
 else:
  if y<640:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD(arg):
 (x,y)=get_position(arg)
 a=get_saved_data(arg,'A')
 b=get_saved_data(arg,'B')
 dx=a-x
 dy=b-y
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDp=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVD(dx**2+dy**2)
 if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDp<50:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(20,30)
  if x<640:
   if y<640:
    return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVa",{'ACLT_X':0,'ACLT_Y':0,'C':225,'D':405,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
   else:
    return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDV",{'ACLT_X':0,'ACLT_Y':0,'C':-45,'D':135,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
  else:
   if y<640:
    return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDa",{'ACLT_X':0,'ACLT_Y':0,'C':135,'D':315,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
   else:
    return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaV",{'ACLT_X':0,'ACLT_Y':0,'C':45,'D':225,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpD=dx/cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDp
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpa=dy/cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDp
  (cw,cc,f,g,h,_)=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,[0,360],0.1)
  if not h:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'LAUNCH':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'CHARGE':get_weapon_power(arg)<60,'ACLT_X':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpD,'ACLT_Y':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpa,'ROT_CC':cc,'ROT_CW':cw})
  elif get_weapon_power(arg)>40:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'LAUNCH':g,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'ACLT_X':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpD,'ACLT_Y':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpa,'ROT_CC':cc,'ROT_CW':cw})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'LAUNCH':f,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'CHARGE':(cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1,10)==1),'ACLT_X':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpD,'ACLT_Y':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVpa,'ROT_CC':cc,'ROT_CW':cw})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVa(arg):
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa=get_saved_data(arg,'E')
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa-=1
 c=get_saved_data(arg,'C')
 d=get_saved_data(arg,'D')
 (cw,cc,_,f,_,q)=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,[c,d],0.02)
 if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa<0:
  if q>315:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD=get_weapon_power(arg)
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD>60:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVa",{'LAUNCH':f,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVa",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDV(arg):
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa=get_saved_data(arg,'E')
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa-=1
 c=get_saved_data(arg,'C')
 d=get_saved_data(arg,'D')
 (cw,cc,_,f,_,q)=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,[c,d],0.02)
 if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa<0:
  if q<45:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD=get_weapon_power(arg)
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD>60:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDV",{'LAUNCH':f,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDV",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDa(arg):
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa=get_saved_data(arg,'E')
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa-=1
 c=get_saved_data(arg,'C')
 d=get_saved_data(arg,'D')
 (cw,cc,_,f,_,q)=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,[c,d],0.02)
 if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa<0:
  if q>235:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD=get_weapon_power(arg)
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD>60:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDa",{'LAUNCH':f,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpDa",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaV(arg):
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa=get_saved_data(arg,'E')
 cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa-=1
 c=get_saved_data(arg,'C')
 d=get_saved_data(arg,'D')
 (cw,cc,_,f,_,q)=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,[c,d],0.02)
 if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa<0:
  if q<135:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180)})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpVD",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,'A':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(1080,1180),'B':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaVp(100,200)})
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD=get_weapon_power(arg)
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVaD>60:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaV",{'LAUNCH':f,'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
  else:
   return("cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaV",{'SHIELD':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'CHARGE':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,'ROT_CC':cc,'ROT_CW':cw,'E':cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVDa})
def cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlpaD(arg,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapD,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVa):
 z=get_weapon_angle(arg)
 if get_radar_data(arg,z)[0]=="opponent":
  return(0,0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,-1)
 else:
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVap=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapD[0]
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVp=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapD[1]
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVap>cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVp:
   cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVa*=-1
  cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDpV=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp
  c=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlVap
  while c<cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVp:
   (cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDpa,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDaV)=get_radar_data(arg,c)
   if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDpa=="opponent":
    cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDpV=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV
    c+=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV(0.0,0.05)
    break
   c+=cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDVa
  if cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlDpV:
   dz=((c-z)+360)%360
   if dz>180:
    if dz>358.5:
     return(cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV(0.0,0.05),0.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
    elif dz>350:
     return(cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV(0.2,0.3),0.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
    else:
     return(1.0,0.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
   else:
    if dz<1.5:
     return(0.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV(0.0,0.05),cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
    elif dz<10:
     return(0.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDV(0.2,0.3),cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
    else:
     return(0.0,1.0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlapV,c)
  return(0,0,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,cBwQLqIdCSfMjUJbYxNPHKTtGXFngimehuzEoWyRskAvOrlaDp,-1)