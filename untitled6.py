# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:08:26 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z=w.player.getTilePos()
name=input("Please enter your name:")
s=input("Please enter something:")
w.postToChat("<"+name+">"+s)








