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

	mul_sign = "\\times"

	def construct(self):
		on_screen = self._first_part()
		on_screen = self._second_part(on_screen)
		on_screen = self._third_part(on_screen)
		on_screen = self._fourth_part(on_screen)
		self.wait(5)

	'''
	a₃a₂a₁a₀ x b₃b₂b₁b₀ =
	a₃a₂a₁a₀ x b₃x10³
	a₃a₂a₁a₀ x b₂x10²
	a₃a₂a₁a₀ x b₁x10¹
	a₃a₂a₁a₀ x b₀x10⁰
	'''
	def _first_part(self):
		a = ["a_3", "a_2", "a_1", "a_0"]
		b = ["b_3", "b_2", "b_1", "b_0"]
		mul_sign = self.mul_sign
		#  a₃a₂a₁a₀ x b₃b₂b₁b₀
		left_side = a + [mul_sign] + b
		
		first_term = a + [mul_sign, "b_3", mul_sign, "10^3"]
		second_term = a + [mul_sign, "b_2", mul_sign, "10^2"]
		third_term = a + [mul_sign, "b_1", mul_sign, "10^1"]
		fourth_term = a + [mul_sign, "b_0", mul_sign, "10^0"]

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

		plus = TexMobject("+")
		horizontal_point = \
			eq_text.get_parts_by_tex('a_3')[1].get_left() + LEFT * plus.get_width()
		vertical_points = \
			[(eq_text.get_parts_by_tex('a_3')[i].get_center() + eq_text.get_parts_by_tex('a_3')[i + 1].get_center()) / 2
				for i in range(1, 4)]

		plus = [
			plus.copy().move_to(horizontal_point * RIGHT + vertical_points[i] * UP)
			for i in range(3)
		]
		self.play(*map(lambda x: Write(x), plus))
		self.wait()

		return [eq_text, plus]

	'''
	a₃xb₃ a₂xb₃ a₁xb₃ a₀xb₃ x10³
	a₃xb₂ a₂xb₂ a₁xb₂ a₀xb₂ x10²
	a₃xb₁ a₂xb₁ a₁xb₁ a₀xb₁ x10¹
	a₃xb₀ a₂xb₀ a₁xb₀ a₀xb₀ x10⁰
	'''
	def _second_part(self, on_screen):
		[on_screen_eq, on_screen_plus] = on_screen
		long_dash = "\\textendash"
		one_dash = TexMobject(long_dash)
		mult = self.mul_sign
		space = "\\ "
		equation = [
			"a_3", "b_3", space, "a_2", "b_3", space, "a_1", "b_3", space, "a_0", "b_3", space, mult, "10^3", "\\\\",
			"a_3", "b_2", space, "a_2", "b_2", space, "a_1", "b_2", space, "a_0", "b_2", space, mult, "10^2", "\\\\",
			"a_3", "b_1", space, "a_2", "b_1", space, "a_1", "b_1", space, "a_0", "b_1", space, mult, "10^1", "\\\\",
			"a_3", "b_0", space, "a_2", "b_0", space, "a_1", "b_0", space, "a_0", "b_0", space, mult, "10^0", "\\\\",
		]
		eq_tex = TexMobject(*equation)

		plus_copy = map(lambda x: x.copy(), on_screen_plus)
		map(lambda x: 
			x.move_to((eq_tex.get_left() - x.get_width()) * RIGHT + (x.get_center() + x.get_height()) * UP), 
			plus_copy)

		self.play(FadeOut(on_screen_eq[0:10]),
			ReplacementTransform(on_screen_plus[0], plus_copy[0]),
			ReplacementTransform(on_screen_plus[1], plus_copy[1]),
			ReplacementTransform(on_screen_plus[2], plus_copy[2]))

		#  Las cuatro lineas de el resultado
		for i in range(4):
			line_replacements = []
			for j in range(4):
				#  las cuatro a's
				a = on_screen_eq.get_parts_by_tex("a_" + str(j))[i + 1]
				a_replace = eq_tex.get_parts_by_tex("a_" + str(j))[i]
				line_replacements.append([a, a_replace])

			b = on_screen_eq.get_parts_by_tex("b_" + str(3 - i))
			#  1 porque es el segundo, el primero está del otro lado de la ecuación
			b = b[1]
			#  el original y 3 copias
			b = [b.copy(), b.copy(), b.copy()] + [b]
			b_replace = eq_tex.get_parts_by_tex("b_" + str(3 - i))
			for k in range(len(b)):
				line_replacements.append([b[k], b_replace[k]])

			# x10^ ...
			m = on_screen_eq.get_parts_by_tex(mult)[i*2+2]
			m_rep = eq_tex.get_parts_by_tex(mult)[i]
			line_replacements.append([m, m_rep])

			ten = on_screen_eq.get_part_by_tex("10^" + str(3 - i))
			ten_rep = eq_tex.get_part_by_tex("10^" + str(3 - i))
			line_replacements.append([ten, ten_rep])
			
			x = on_screen_eq.get_parts_by_tex(mult)[i*2+1]

			self.play(*(map(lambda x: ReplacementTransform(*x), line_replacements))
				+ [FadeOut(x)])

		return [eq_tex, plus_copy]

	'''
	Conversión a notación dot
	'''
	def _third_part(self, on_screen):
		[on_screen_eq, on_screen_plus] = on_screen
		first_line = on_screen_eq[:14]
		second_line = on_screen_eq[15:29]
		third_line = on_screen_eq[30:44]
		fourth_line = on_screen_eq[45:59]

		step = first_line[:3].get_width() * 0.82

		plus_copy = map(lambda x: x.copy(), on_screen_plus)
		map(lambda x: 
			x.shift(-1.5 * step * RIGHT),
			plus_copy)
		
		self.play(
			ReplacementTransform(on_screen_plus[0], plus_copy[0]),
			ReplacementTransform(on_screen_plus[1], plus_copy[1]),
			ReplacementTransform(on_screen_plus[2], plus_copy[2]))
		self.play(
			first_line.shift, (1.5 * step) * RIGHT,
			second_line.shift, (0.5 * step) * RIGHT,
			third_line.shift, (-0.5 * step) * RIGHT,
			fourth_line.shift, (-1.5 * step) * RIGHT,
			)

		self.wait()

		to_fade = []
		to_fade += on_screen_eq.get_parts_by_tex(self.mul_sign)
		for i in range(4):
			to_fade += on_screen_eq.get_parts_by_tex("10^" + str(i))
		self.play(*map(lambda x: FadeOut(x), to_fade))

		self.wait()

		pairs = zip(on_screen_eq.get_parts_by_tex("a_"), on_screen_eq.get_parts_by_tex("b_"))
		pairs = [VGroup(*x) for x in pairs]
		dots = [Dot() for _ in range(len(pairs))]
		dots = [x.move_to(pairs[i].get_center()) for i, x in enumerate(dots)]
		self.play(*[ReplacementTransform(pairs[i], dots[i]) for i in range(len(pairs))])
		self.wait()

		self.play(*[FadeOut(x) for x in plus_copy])

		return dots

	'''
	Animación de suma
	'''
	def _fourth_part(self):


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

