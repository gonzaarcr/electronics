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
		comb_background = circuit.get_combinational()
		regs_background = circuit.get_registers()
		
		# self.add(comb_background)
		# self.add(regs_background)
		self.add(circuit.get_all())

		from_anim = comb_background.copy()
		map(lambda x: x.set_stroke(width=4,color=RED_A), from_anim.submobjects)
		to_anim = regs_background.copy()
		map(lambda x: x.set_stroke(width=4,color=RED_E), to_anim.submobjects)
		
		self.wait()
		self.play(from_anim.set_stroke, width=4, color=BLUE_E, run_time=2, submobject_mode="all_at_once")
		self.wait()
		self.play(FadeToColor(to_anim, BLUE_E, run_time=3))
		self.play(FadeToColor(to_anim, RED_E, run_time=3))
		self.play(FadeToColor(to_anim, YELLOW_E, run_time=3))
		self.wait()
		# self.play(ShowCreation(from_anim, run_time=2, submobject_mode="all_at_once"))
		
		self.wait()
		
