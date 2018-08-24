# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:22:17 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
myID=w.getPlayerEntityId("jimmychiu830")
w.postToTitle(myID,"§1hi")