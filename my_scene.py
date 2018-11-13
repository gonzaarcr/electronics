#!/usr/bin/env python
# -*- coding: utf-8 -*-


from animation import *
from animation.creation import *
from animation.composition import *
from animation.indication import *
from camera import *
from mobject.geometry import *
from mobject.svg.svg_mobject import *
from mobject.svg.tex_mobject import *
from scene.scene import Scene

# from electronics.components import *


class Introduccion(Scene):

	def construct(self):
		title = TextMobject("Multiplicaci\\'{o}n \\\\ binaria").scale(1.5)
		self.play(Write(title))
		self.wait()
		self.play(FadeOut(title))


class AlgoritmoTradicional(Scene):
	mul_sign = "\\times"

	#  Para la dot notation
	dots_v_dist = 0
	dots_h_dist = 0

	def construct(self):
		on_screen = self._first_part()
		on_screen = self._second_part(on_screen)
		on_screen = self._third_part(on_screen)
		on_screen = self._fourth_part(on_screen)
		[dots, result_lines] = self._fifth_part(on_screen)
		[dots, result_lines] = self._sixth_part(dots, result_lines)
		on_screen = self._seventh_part(dots, result_lines)
		self.wait(5)


	def _first_part(self):
		"""
		a₃a₂a₁a₀ x b₃b₂b₁b₀ =
		a₃a₂a₁a₀ x b₃x10³
		a₃a₂a₁a₀ x b₂x10²
		a₃a₂a₁a₀ x b₁x10¹
		a₃a₂a₁a₀ x b₀x10⁰
		"""
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

	def _second_part(self, on_screen):
		"""
		a₃xb₃ a₂xb₃ a₁xb₃ a₀xb₃ x10³
		a₃xb₂ a₂xb₂ a₁xb₂ a₀xb₂ x10²
		a₃xb₁ a₂xb₁ a₁xb₁ a₀xb₁ x10¹
		a₃xb₀ a₂xb₀ a₁xb₀ a₀xb₀ x10⁰
		"""
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
			m = on_screen_eq.get_parts_by_tex(mult)[i * 2 + 2]
			m_rep = eq_tex.get_parts_by_tex(mult)[i]
			line_replacements.append([m, m_rep])

			ten = on_screen_eq.get_part_by_tex("10^" + str(3 - i))
			ten_rep = eq_tex.get_part_by_tex("10^" + str(3 - i))
			line_replacements.append([ten, ten_rep])

			x = on_screen_eq.get_parts_by_tex(mult)[i * 2 + 1]

			self.play(*(map(lambda x: ReplacementTransform(*x), line_replacements))
				+ [FadeOut(x)])

		return [eq_tex, plus_copy]

	def _third_part(self, on_screen):
		"""
		Conversión a notación dot
		"""
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

	def _fourth_part(self, dots):
		"""
		Animación de suma
		"""
		#  Alunas distancias y vectores para operar
		[_, dots_v_dist, _] = dots[0].get_center() - dots[4].get_center()
		[dots_h_dist, _, _] = dots[1].get_center() - dots[0].get_center()
		self.dots_v_dist = dots_v_dist
		self.dots_h_dist = dots_h_dist
		carry_height = dots[0].get_center()[1] + dots_v_dist
		result_height = dots[len(dots) - 1].get_center()[1] - dots_v_dist

		result_line_height = \
			dots[len(dots) - 4].get_center()[1] \
			- dots_v_dist / 2
		result_line = Line(
			[dots[len(dots) - 4].get_center()[0] - dots_h_dist * 1.5, result_line_height, 0],
			[dots[3].get_center()[0] + dots_h_dist / 2, result_line_height, 0]
		)
		result_line.set_stroke(width=2)
		self.play(ShowCreation(result_line))

		added_in_scene = []
		carry_dots = []

		for i in range(8):
			#  Animación de suma
			#  Baja una columna, y sube el carry al mismo tiempo
			#  Se repite eso 8 veces
			indeces = [(6 - i) - (3 - k) for k in range(4)]
			movin_dots = [dots[j * 4 + k] for j, k in enumerate(indeces) if 0 <= k < 4]
			movin_dots = [x.copy() for x in movin_dots]
			movin_dots += carry_dots[0] if len(carry_dots) > 0 else []

			#  La última iteración no tiene carry
			carry_dots = [x.copy() for x in movin_dots] if i != 7 else []

			anim = []
			result_coord = np.array([
				movin_dots[0].get_center()[0],
				result_height,
				movin_dots[0].get_center()[2]]
			)

			carry_coord = np.array([
				movin_dots[0].get_center()[0] - dots_h_dist,
				carry_height,
				movin_dots[0].get_center()[2]]
			)

			for el in movin_dots:
				anim.append(el.move_to)
				anim.append(result_coord)

			for el in carry_dots:

				anim.append(el.move_to)
				anim.append(carry_coord)

			self.play(*anim)

			#  Dejo uno solo cuando termina la animación
			#  Para mejor organización
			for i in range(1, len(carry_dots)):
				self.remove(carry_dots[i])
			carry_dots = [carry_dots[0]] if len(carry_dots) > 0 else []

			for i in range(1, len(movin_dots)):
				self.remove(movin_dots[i])
			movin_dots = [movin_dots[0]] if len(movin_dots) > 0 else []

			added_in_scene += carry_dots + movin_dots

			self.wait()

		self.wait()
		added_in_scene += [result_line]
		self.play(*map(lambda x: FadeOut(x), added_in_scene))

		return dots

	def _fifth_part(self, dots):
		"""
		Multiplicación de 2 operandos, empezando
		de la parte de “abajo” de la suma de cuatro
		Lineas de puntos:
		- 4 de la cuenta original (de 0 a 3)
		- p_2 y A x b_1 (de 4 a 5)
		- p_3 y A x b_0 (de 6 a 7)
		- p_4 (8)
		"""
		all_dots = []
		for i in range(4):
			all_dots.append(dots[i*len(dots)/4 : (i+1)*len(dots)/4])
		first_lines = dots[:len(dots)/2]
		second_lines = dots[len(dots)/2:]

		# Mueve la 3a y 4a fila al centro de la pantalla
		self.play(*map(lambda x: FadeOut(x), first_lines))

		despl_vector = ORIGIN - second_lines[1].get_corner(DR)

		# Las mueve aunque no se vean para después aparecer
		for e in first_lines:
			e.shift(despl_vector)

		anim = []
		for e in second_lines:
			anim.append(e.shift)
			anim.append(despl_vector)

		self.play(*anim)

		#  Alunas distancias y vectores para operar
		dots_v_dist = self.dots_v_dist
		dots_h_dist = self.dots_h_dist
		result_height = second_lines[len(second_lines) - 1].get_center()[1] - dots_v_dist

		result_line_height = \
			second_lines[len(second_lines) - 4].get_center()[1] \
			- dots_v_dist / 2
		result_line = Line(
			[second_lines[len(second_lines) - 4].get_center()[0] - dots_h_dist * 1.5, result_line_height, 0],
			[second_lines[3].get_center()[0] + dots_h_dist / 2, result_line_height, 0]
		)
		# Dibuja la linea del resultado
		self.play(ShowCreation(result_line))

		anim = []
		x_axis = []
		to_remove = []
		result_dots = []
		
		for e in second_lines:
			e_copy = e.copy()
			result_dots.append(e_copy)
			move_v = DOWN * (e_copy.get_center()[1] - result_height)
			anim.append(e_copy.shift)
			anim.append(move_v)
			for x in x_axis:
				if abs(e_copy.get_center()[0] - x) < 0.1:
					to_remove.append(e_copy)
					break
			else:
				x_axis.append(e_copy.get_center()[0])				

		carry = second_lines[len(second_lines)/2].copy()
		move_v = DOWN * (e_copy.get_center()[1] - result_height)
		move_v += LEFT * dots_h_dist
		anim.append(carry.shift)
		anim.append(move_v)

		result_dots.insert(0, carry)
		for e in result_dots:
			if e in to_remove:
				result_dots.remove(e)
		all_dots.append(result_dots)

		self.play(*anim)
		self.remove(*to_remove)

		return [all_dots, [result_line]]

	def _sixth_part(self, dots, result_lines):
		"""
		Crea p_3
		- 4 de la cuenta original (de 0 a 3)
		- p_2 y A x b_1 (de 4 a 5)
		- p_3 y A x b_0 (de 6 a 7)
		- p_4 (8)
		"""
		self.play(*map(lambda x: FadeIn(x), dots[1]))

		anim = []
		for i in range(len(dots)):
			for j in range(len(dots[i])):
				if dots[i][j] in self.get_mobjects():
					anim.append(dots[i][j].shift)
					anim.append(UP * self.dots_v_dist/2)
				else:
					# Los que no están en la escena los mueve directamente
					dots[i][j].shift(UP * self.dots_v_dist/2)

		anim.append(result_lines[0].shift)
		anim.append(UP * self.dots_v_dist/2)
		self.play(*anim)

		move_v = abs(dots[1][0].get_center()[1] - dots[4][0].get_center()[1]) \
			+ self.dots_v_dist
		anim = []
		sumando = []
		for e in dots[1]:
			e_copy = e.copy()
			sumando.append(e_copy)
			anim.append(e_copy.shift)
			anim.append(DOWN * move_v)

		dots.append(sumando)
		self.play(*anim)

		result_line = Line(
			result_lines[0].get_start() + DOWN * self.dots_v_dist * 2,
			result_lines[0].get_end() + DOWN * self.dots_v_dist * 2 + RIGHT * self.dots_h_dist
		)
		result_lines.append(result_line)
		# Dibuja la linea del resultado
		self.play(ShowCreation(result_line))

		anim = []
		x_axis = []
		to_remove = []
		result_dots = []

		for e in dots[4] + dots[5]:
			e_copy = e.copy()
			result_dots.append(e_copy)
			move_v = dots[4][0].get_center()[1] - self.dots_v_dist * 2
			move_v = [e_copy.get_center()[0], move_v, 0]
			anim.append(e_copy.move_to)
			anim.append(move_v)
			for x in x_axis:
				if abs(e_copy.get_center()[0] - x) < 0.1:
					to_remove.append(e_copy)
					break
			else:
				x_axis.append(e_copy.get_center()[0])				

		for e in result_dots:
			if e in to_remove:
				result_dots.remove(e)
		dots.append(result_dots)

		self.play(*anim)
		self.remove(*to_remove)

		return [dots, result_lines]

	def _seventh_part(self, dots, result_lines):
		"""
		Crea p_4
		- 4 de la cuenta original (de 0 a 3)
		- p_2 y A x b_1 (de 4 a 5)
		- p_3 y A x b_0 (de 6 a 7)
		- p_4 (8)
		"""
		self.play(*map(lambda x: FadeIn(x), dots[0]))

		anim = []
		for i in range(len(dots)):
			for j in range(len(dots[i])):
				if dots[i][j] in self.get_mobjects():
					anim.append(dots[i][j].shift)
					anim.append(UP * self.dots_v_dist)
				else:
					# Los que no están en la escena los mueve directamente
					print(":481 DEBUG: Sí hay alguno en la escena "
						+ str(i) + ", " + str(j)
						+ " no debería")
					dots[i][j].shift(UP * self.dots_v_dist)

		for e in result_lines:
			anim.append(e.shift)
			anim.append(UP * self.dots_v_dist)

		self.play(*anim)

		move_v = abs(dots[0][0].get_center()[1] - dots[6][0].get_center()[1]) \
			+ self.dots_v_dist
		anim = []
		sumando = []
		for e in dots[0]:
			e_copy = e.copy()
			sumando.append(e_copy)
			anim.append(e_copy.shift)
			anim.append(DOWN * move_v)

		dots.append(sumando)
		self.play(*anim)

		result_line = Line(
			result_lines[1].get_start() + DOWN * self.dots_v_dist * 2,
			result_lines[1].get_end() + DOWN * self.dots_v_dist * 2 + RIGHT * self.dots_h_dist
		)
		result_lines.append(result_line)
		# Dibuja la linea del resultado
		self.play(ShowCreation(result_line))

		anim = []
		x_axis = []
		to_remove = []
		result_dots = []

		for e in dots[6] + dots[7]:
			e_copy = e.copy()
			result_dots.append(e_copy)
			move_v = dots[6][0].get_center()[1] - self.dots_v_dist * 2
			move_v = [e_copy.get_center()[0], move_v, 0]
			anim.append(e_copy.move_to)
			anim.append(move_v)
			for x in x_axis:
				if abs(e_copy.get_center()[0] - x) < 0.1:
					to_remove.append(e_copy)
					break
			else:
				x_axis.append(e_copy.get_center()[0])				

		for e in result_dots:
			if e in to_remove:
				result_dots.remove(e)
		dots.append(result_dots)

		self.play(*anim)
		self.remove(*to_remove)

		return [dots, result_lines]

	def _eight_part(self):
		pass


class MyScene(Scene):
	"""
	Esto quedó re tirado pero en un momento era la escena orignal,
	lo usé de playground y empezó por otro lado.
	"""

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

		# self.play(Succession(
		#	ShowCreation(signal.getEdges(), run_time=10),
		#	FadeOut, signal.getEdges(),
		# ))
		# self.wait(5)
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
		from_anim.set_stroke(width=4, color=RED_A)
		to_anim = regs_background.copy()
		to_anim.set_stroke(width=4, color=RED_E)

		self.wait()
		self.play(ShowCreation(from_anim, submobject_mode="all_at_once"))
		self.wait()
		self.play(FadeToColor(to_anim, BLUE_E, run_time=3))
		self.play(FadeToColor(to_anim, RED_E, run_time=3))
		self.play(FadeToColor(to_anim, YELLOW_E, run_time=3))
		self.wait()
		# self.play(ShowCreation(from_anim, run_time=2, submobject_mode="all_at_once"))

		self.wait()
