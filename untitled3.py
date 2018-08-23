# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:34:36 2018

@author: NTPU
"""
from random import randrange
from mcpi.minecraft import Minecraft
w=Minecraft.create()

for j in range(30):
    x,y,z = mc.player.getTilePos()
    x=x+j
    for i in range(30):
        r=randrange(0,16)
        w.setBlock(x,y,z,35,r)
        z=z+1