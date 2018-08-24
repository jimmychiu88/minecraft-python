# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:14:18 2018

@author: NTPU
"""
from random import choice
from mcpi.minecraft import Minecraft
w=Minecraft.create()
"""
block=[14,15,16,56,73,129]
r=choice(block)
"""
list2=[[]],
        [56,17,46]]

myID=w.getPlayerEntityId("jimmychiu830")
x,y,z=w.entity.getTilePos(myID)
StartX=x
for list1 in list2:
    for i in list1:
        w.setBlock(x,y,z,i)
        x=x+1
    x=StartX
    z=z+1