# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:20:53 2018

@author: NTPU
"""
from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z=w.player.getTilePos()
w.setSign(x,y,z,63,0,"歡迎來到黃金城","","","")


















