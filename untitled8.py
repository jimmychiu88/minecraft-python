# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:48:06 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
while True:
    hits=w.events.pollProjectileHits()
    if len(hits)>0:
        h=hits[0]
        x,y,z=h.pos.x,h.pos.y,h.pos.z
        w.createExplosion(x,y,z,150)

















