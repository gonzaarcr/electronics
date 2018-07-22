#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animation import *
from animation.creation import *
from animation.composition import *
from animation.indication import *
from mobject.geometry import *
from mobject.svg.svg_mobject import *
from scene.scene import Scene

from electronics.components import Signal


class MyScene(Scene):

	def construct(self):
		points = [
			LEFT * 8,
			LEFT * 1,
			UP * 3 + RIGHT * 5,
			UP * 3 + RIGHT * 6,
		]
		signal = Signal(points)
		tmp1 = signal.get_edge_propogation_animations()
		# self.play(*tmp1)

		#self.play(Succession(
		#	ShowCreation(signal.getEdges(), run_time=10),
		#	FadeOut, signal.getEdges(),
		#))
		#self.wait(5)
		args = []
		for e in signal.getEdges():
			args += [e]
		args = map(FadeOut, args)
		# self.play(*args)
		# self.play(*tmp1)
		# self.wait(5)

		circuit = SVGMobject(file_name="drawing2")
		import pdb; pdb.set_trace()
		circuit.set_stroke(width=1,color="White")
		circuit.set_fill(opacity=0)
		brain_outline = circuit.copy()
		brain_outline.set_stroke(BLUE_B, 3)

		self.add(circuit)

		for x in range(2):
			self.play(
				ShowPassingFlash(
					brain_outline, 
					time_width = 2,
					run_time = 2
				)
			)

		self.wait()


