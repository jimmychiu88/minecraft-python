# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:34:30 2018

@author: NTPU
"""
import random
from mcpi.minecraft import Minecraft
w=Minecraft.create()

x,y,z=w.player.getTilePos()
for i in range(20):
    r=random.randrange(1,5)
    if r==1:
        w.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
    if r==2:
        w.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4
    if r==3:
        w.setBlocks(x,y,z,x,y,z+4,1)
        x=x+4
    if r==4:
        w.setBlocks(x,y,z,x,y,z-4,1)
        x=x-4
    if r==5:
        w.setBlocks(x,y,z,x,y+1,z,1)
        x=x-4
    if r==6:
        w.setBlocks(x,y,z,x,y-1,z,1)
        x=x-4
                  