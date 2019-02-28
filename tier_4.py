#<Super Nova>
from library_for_glad_ai_tors import*
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu=dir
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX=False
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY=True
import math
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsXY=math.sqrt
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusY=math.sin
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusX=math.cos
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYs=math.radians
import random 
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYX=random.randint
FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsXu=random.choice
def start(arg):
 return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXY",{'A':0,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsXu([-1.0,1.0]),'E':get_damage_level(arg)})
def FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXY(arg):
 (x,y)=get_position(arg)
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu=get_saved_data(arg,'D')
 if get_damage_level(arg)-get_saved_data(arg,'E')>10:
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu*=-1
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=get_saved_data(arg,'A')
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu*(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYX(3,5)%360)
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX
 c=0
 while c<360:
  (FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXuY,FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXus)=get_radar_data(arg,c)
  if FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXuY=="opponent":
   FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY
   break
  c+=0.1
 if not FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs and get_weapon_power(arg)<90:
  return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXs",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'B':0,'C':0,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'ACLT_X':0,'ACLT_Y':0,'ROT_CW':0,'ROT_CC':0,'CHARGE':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY,'SHIELD':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY})
 else:
  cw=0
  cc=0
  if FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs:
   z=get_weapon_angle(arg)
   dz=((c-z)+360)%360
   if dz>180:
    if dz>358:
     cc=0.02
    elif dz>345:
     cw=0.2
    else:
     cw=1.0
   else:
    if dz<2:
     cw=0.02
    elif dz<15:
     cc=0.2
    else:
     cc=1.0
   if(cw<0.1 and cc<0.1):
    return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYX",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'LAUNCH':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY,'SHIELD':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'CHARGE':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'ROT_CW':cw,'ROT_CC':cc})
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsY=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYs(0+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu)
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsu=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYs(90+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu)
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXu=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYs(180+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu)
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXs=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYs(270+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu)
  ax=640+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusX(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsY)*450
  ay=640-FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusY(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsY)*450
  bx=640+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusX(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsu)*450
  by=640-FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusY(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXsu)*450
  cx=640+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusX(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXu)*450
  cy=640-FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusY(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXu)*450
  dx=640+FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusX(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXs)*450
  dy=640-FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPusY(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYXs)*450 
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYuX=[((ax-x)**2+(ay-y)**2,(ax,ay)),((bx-x)**2+(by-y)**2,(bx,by)),((cx-x)**2+(cy-y)**2,(cx,cy)),((dx-x)**2+(dy-y)**2,(dx,dy))]
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYuX.sort()
  (e,(ex,ey))=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYuX[0]
  e=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsXY(e)
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYus=(ex-x)/e
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYsX=(ey-y)/e
  return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXY",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'ACLT_X':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYus,'ACLT_Y':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPYsX,'ROT_CW':cw,'ROT_CC':cc})
def FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXs(arg):
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu=get_saved_data(arg,'D')
 if get_damage_level(arg)-get_saved_data(arg,'E')>10:
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu*=-1
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=get_saved_data(arg,'A')
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu+(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYX(3,5)%360)
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX
 c=0
 while c<360:
  (FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXuY,FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXus)=get_radar_data(arg,c)
  if FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXuY=="opponent":
   FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY
   break
  c+=1
 if FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYs or get_weapon_power(arg)>80:
  return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXY",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'ROT_CW':0,'ROT_CC':0,'CHARGE':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'SHIELD':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX})
 else:
  return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXs",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'ROT_CW':0,'ROT_CC':0,'CHARGE':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY,'SHIELD':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuY})
def FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuYX(arg):
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu=get_saved_data(arg,'D')
 if get_damage_level(arg)-get_saved_data(arg,'E')>10:
  FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu*=-1
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=get_saved_data(arg,'A')
 FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu=FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu+(FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYX(3,5)%360)
 return("FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPuXY",{'A':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPXYu,'D':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsYu,'E':get_damage_level(arg),'LAUNCH':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'CHARGE':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'SHIELD':FJwKoOgIQHLylhVfcvaDnrptxGzNRbCAiWmMTUdjBeSkEqPsuX,'ROT_CW':0,'ROT_CC':0})