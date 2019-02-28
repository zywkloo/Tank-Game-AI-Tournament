#<Alan Rails>
from library_for_glad_ai_tors import*
qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP=True
qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGk=False
import math
import random 
qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkG=random.choice
qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk=100
def start(arg):
 if get_weapon_angle(arg)==270:
  return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPG",{})
 else:
  return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPk",{})
def qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPk(arg):
 (x,y)=get_position(arg)
 if y>get_s_border(arg)-qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
  if x<get_w_border(arg)+qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
   return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':+1})
  else:
   return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':-1})
 else:
  return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPk",{'A':-1,'ACLT_Y':1,'CHARGE':get_weapon_power(arg)<60})
def qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPG(arg):
 (x,y)=get_position(arg)
 if y<get_n_border(arg)+qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
  if x<get_w_border(arg)+qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
   return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':+1})
  else:
   return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':-1})
 else:
  return("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIPG",{'A':-1,'ACLT_Y':-1,'CHARGE':get_weapon_power(arg)<60}) 
def qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP(arg):
 (x,y)=get_position(arg)
 qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIG=get_saved_data(arg,'A')
 (qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPkI,qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPkG)=get_radar_data(arg,get_weapon_angle(arg))
 qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI=qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPkI=="opponent"
 if qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIG==-1:
  if x<get_w_border(arg)+qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
   return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':+1,'CHARGE':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI,'LAUNCH':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI})
  else:
   if qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI:
    return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':+1,'ACLT_X':+1,'CHARGE':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP,'LAUNCH':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP})
   else:
    return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'ACLT_X':-1,'CHARGE':(get_weapon_power(arg)<10 and qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkG([qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP,qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGk]))})
 else:
  if x>get_e_border(arg)-qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPIk:
   return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':-1,'CHARGE':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI,'LAUNCH':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI})
  else:
   if qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQPGI:
    return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'A':-1,'ACLT_X':-1,'CHARGE':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP,'LAUNCH':qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP})
   else:
    return ("qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkP",{'ACLT_X':+1,'CHARGE':(get_weapon_power(arg)<10 and qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIkG([qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGP,qyEuhosJKVAmNrRlHwTDaeXSdLcjMtgfUCviObpYBFWzxnQIGk]))})