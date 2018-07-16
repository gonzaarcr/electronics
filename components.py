#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mobject.geometry import *
from animation.animation import *
from animation.indication import *
from animation.creation import *

class Signal(Line):
	"""
	Modela una señal, osea, un “cable”
	"""

	def __init__(self, points = []):
		"""
		Crea que recorre cada punto x1, x2...
		"""
		self.edge_color = LIGHT_GREY
		self.edge_stroke_width = 2
		self.edge_propogation_color = YELLOW
		self.edge_propogation_time = 1

		self.points = points

		self.edge_groups = VGroup()

		for i in range(0, len(points) - 2):

		edge = Line(
			ORIGIN,
			LEFT + UP,
			stroke_color = self.edge_color,
			stroke_width = self.edge_stroke_width,
		)
		# self.edge_groups.add(edge)

		edge2 = Line(
			LEFT + UP,
			RIGHT + UP,
			stroke_color = self.edge_color,
			stroke_width = self.edge_stroke_width * 10,
		)
		# edge2.submobjects += edge
		edge2.next_to(edge)
		self.edge_groups.add(edge2)

	def get_edge_propogation_animations(self, index = 0):
		"""
		Animación de color
		"""


		animation = []
		for e in self.points:

			


			
			copy = e.copy()
			copy.set_stroke(
				self.edge_propogation_color,
				width = 1.5 * self.edge_stroke_width
			)
			animation += [Succession(
            	ShowCreation(
					copy.copy(),
					run_time = self.edge_propogation_time,
					submobject_mode = "one_at_a_time",
					remover = True,
				),
				Uncreate(
					copy.copy(),
					run_time = self.edge_propogation_time,
					submobject_mode = "one_at_a_time",
					remover = True
				)
        	)]

		return animation


class Register():
	pass
