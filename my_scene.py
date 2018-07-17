#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animation import *
from animation.creation import *
from animation.composition import *
from mobject.geometry import *
from scene.scene import Scene

from electronics.components import Signal

class MyScene(Scene):

	def construct(self):
		points = [
			DOWN + LEFT,
			DOWN + RIGHT,
			UP + RIGHT,
		]
		signal = Signal(points)
		tmp1 = signal.get_edge_propogation_animations()
		
		self.play(*tmp1)
		self.wait()
		self.play(FadeOut(signal.edges))
