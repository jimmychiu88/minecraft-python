# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:38:26 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z=w.player.getTilePos()
a=0
while a<20:
    w.setBlocks(x+30,y-1,z,x-30,y-30,z,19)
    z=z+5
    a=a+1
















































