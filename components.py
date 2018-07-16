#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mobject.geometry import *
from animation.animation import *
from animation.indication import *

class Signal(Line):
	"""
	Modela una señal, osea, un “cable”
	"""

	def __init__(self):

		self.edge_color = LIGHT_GREY
		self.edge_stroke_width = 2
		self.edge_propogation_color = YELLOW
		self.edge_propogation_time = 1

		self.edge_groups = VGroup()

		edge = Line(
			ORIGIN,
			LEFT + UP,
			stroke_color = self.edge_color,
			stroke_width = self.edge_stroke_width,
		)
		self.edge_groups.add(edge)

		edge2 = Line(
			LEFT + UP,
			RIGHT + UP,
			stroke_color = self.edge_color,
			stroke_width = self.edge_stroke_width * 10,
		)
		edge2.move_to(DOWN)
		self.edge_groups.add(edge2)

	def get_edge_propogation_animations(self, index = 0):
		"""
		Animación de color
		"""
		edge_group_copy = self.edge_groups[index].copy()
		edge_group_copy.set_stroke(
			self.edge_propogation_color,
			width = 1.5 * self.edge_stroke_width
		)
		return [ShowCreationThenDestruction(
			edge_group_copy,
				run_time = self.edge_propogation_time,
				submobject_mode = "lagged_start"
			)]


class Register():
	pass
