#!/usr/bin/env python
# -*- coding: utf-8 -*-

from animation import *
from animation.creation import *
from animation.composition import *
from animation.indication import *
from mobject.geometry import *
from mobject.svg.svg_mobject import *
from mobject.svg.tex_mobject import *
from scene.scene import Scene

from electronics.components import *


class Introduccion(Scene):

	def construct(self):
		title = TextMobject("Multiplicaci\\'{o}n \\\\ binaria").scale(1.5)
		self.play(Write(title))
		self.wait()
		self.play(FadeOut(title))


class AlgoritmoTradicional(Scene):

	def construct(self):
		a = ["a_3", "a_2", "a_1", "a_0"]
		b = ["b_3", "b_2", "b_1", "b_0"]
		mul_sign = "\\times"
		#  a₃a₂a₁a₀ x b₃b₂b₁b₀
		left_side = a + ["\\times"] + b
		
		first_term = a + [mul_sign, "b_3", mul_sign, "10^3"]
		second_term = a + [mul_sign, "b_2", mul_sign, "10^2"]
		third_term = a + [mul_sign, "b_1", mul_sign, "10^1"]
		fourth_term = a + [mul_sign, "b_0", mul_sign, "10^0"]

		#  a₃a₂a₁a₀ x b₃x10³
		#  a₃a₂a₁a₀ x b₂x10²
		#  a₃a₂a₁a₀ x b₁x10¹
		#  a₃a₂a₁a₀ x b₀x10⁰
		equation = \
			left_side + ["=", "\\\\"] + \
			first_term + ["\\\\"] + \
			second_term + ["\\\\"] + \
			third_term + ["\\\\"] + \
			fourth_term

		eq_text = TexMobject(*equation)
		
		a_first_line = eq_text[0:4].copy()
		b_first_line = eq_text[5].copy()
		self.play(Write(eq_text[:10]))
		self.play(ReplacementTransform(a_first_line, eq_text[11:15]),
			ReplacementTransform(b_first_line, eq_text[16]))
		self.play(Write(eq_text[15]), Write(eq_text[17:20]))

		a_second_line = eq_text[0:4].copy()
		b_second_line = eq_text[6].copy()
		self.play(ReplacementTransform(a_second_line, eq_text[20:24]),
			ReplacementTransform(b_second_line, eq_text[25]))
		self.play(Write(eq_text[24]), Write(eq_text[26:29]))

		a_third_line = eq_text[0:4].copy()
		b_third_line = eq_text[7].copy()
		self.play(ReplacementTransform(a_third_line, eq_text[29:33]),
			ReplacementTransform(b_third_line, eq_text[34]))
		self.play(Write(eq_text[33]), Write(eq_text[35:38]))

		a_fourth_line = eq_text[0:4].copy()
		b_fourth_line = eq_text[8].copy()
		self.play(ReplacementTransform(a_fourth_line, eq_text[38:42]),
			ReplacementTransform(b_fourth_line, eq_text[43]))
		self.play(Write(eq_text[42]), Write(eq_text[44:47]))

		import pdb; pdb.set_trace()
		plus = TexMobject("+")
		horizontal_point = \
			eq_text.get_parts_by_tex('a_3')[1].get_left() + LEFT * plus.get_width()
		vertical_points = \
			[(eq_text.get_parts_by_tex('a_3')[i].get_center() + eq_text.get_parts_by_tex('a_3')[i + 1].get_center()) / 2
			for i in range(1, 4)]

		plus.move_to(horizontal_point * RIGHT + vertical_points[0] * UP)
		plus_2 = plus.copy()
		plus_2.move_to(horizontal_point * RIGHT + vertical_points[1] * UP)
		plus_3 = plus.copy()
		plus_3.move_to(horizontal_point * RIGHT + vertical_points[2] * UP)
		self.play(Write(plus), Write(plus_2), Write(plus_3))

		long_dash = "\\textendash"
		one_dash = TexMobject(long_dash)

		# fin de primera animación

		self.wait()


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
		from_anim.set_stroke(width=4,color=RED_A)
		to_anim = regs_background.copy()
		to_anim.set_stroke(width=4,color=RED_E)
		
		self.wait()
		self.play(ShowCreation(from_anim, submobject_mode="all_at_once"))
		self.wait()
		self.play(FadeToColor(to_anim, BLUE_E, run_time=3))
		self.play(FadeToColor(to_anim, RED_E, run_time=3))
		self.play(FadeToColor(to_anim, YELLOW_E, run_time=3))
		self.wait()
		# self.play(ShowCreation(from_anim, run_time=2, submobject_mode="all_at_once"))
		
		self.wait()
		
