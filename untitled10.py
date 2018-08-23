# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:41:31 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z=w.player.getTilePos()
for i in range(50):
    w.setBlock(x,y-1,z+i,57)
   
    
    














































