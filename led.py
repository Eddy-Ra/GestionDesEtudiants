#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(False) 

class Led:
    def __init__(self):
        gp.setup(16, gp.OUT, initial=gp.LOW)
        gp.setup(20, gp.OUT, initial=gp.LOW)
        gp.setup(21, gp.OUT, initial=gp.LOW)

    def action(self, data):
        data = data
        if data == "red on":
            gp.output(16, gp.HIGH)
        if data == "red off":
            gp.output(16, gp.LOW)
        if data == "green on":
            gp.output(20, gp.HIGH)
        if data == "green off":
            gp.output(20, gp.LOW)
        if data == "blue on":
            gp.output(21, gp.HIGH)
        if data == "blue off":
            gp.output(21, gp.LOW)