# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:25:14 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def wer(x,y,z,block,base=18):
    x,y,z = mc.player.getTilePos()
    base = 18
    height = (base//2)+1

    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
    
        x2 = x + base - i
    #y與y2相同
        z2 = z + base - i
        mc.setBlocks(x1, y1, z1, x2, y1, z2, block)
    
