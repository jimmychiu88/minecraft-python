# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:13:59 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z=w.player.getTilePos()
w.spawnEntity(x,y,z,63)


















