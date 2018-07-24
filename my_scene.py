#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animation import *
from animation.creation import *
from animation.composition import *
from animation.indication import *
from mobject.geometry import *
from mobject.svg.svg_mobject import *
from scene.scene import Scene

from electronics.components import *


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

		circuit = SvgBuilder("drawing2.svg")
		circuit.get_combinational().scale_to_fit_height(2)
		self.add(circuit.get_combinational())

		from_anim = circuit.get_registers().copy()
		from_anim.set_stroke(width=1,color=BLUE_E)
		to_anim = circuit.get_registers().copy()
		to_anim.set_stroke(width=1,color=RED_E)

		self.play(circuit.get_combinational().set_stroke, width=1, color=RED_E)
		
		self.wait()
		
