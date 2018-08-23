# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:18:32 2018

@author: NTPU
"""

from random import randrange
from mcpi.minecraft import Minecraft
w=Minecraft.create()
w.postToChat("start")
r=randrange(0,16)
while True:
    hits=w.events.pollBlockHits()
    if len(hits)>0:
        h=hits[0]
        
        block=w.getBlockWithData(h.pos)
        data=block.data
        if data ==r:
            w.postToChat("找到了")
        elif data>r:
            w.postToChat("找錯了喔!要找小一點的")
        elif data<r:
            w.postToChat("找錯了喔!要找大一點的")
            
                        
                        
                