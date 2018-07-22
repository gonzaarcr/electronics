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

	def __init__(self, points=None):
		"""
		Crea que recorre cada punto x1, x2...
		"""
		self.edge_color = LIGHT_GREY
		self.edge_stroke_width = 2
		self.edge_propogation_color = YELLOW
		self.edge_propogation_time = 1

		self.points = points if points is not None else []
		self.edges = VGroup()

		for i in range(0, len(self.points) - 1):
			edge = Line(
				self.points[i],
				self.points[i + 1],
				stroke_color=self.edge_color,
				stroke_width=self.edge_stroke_width * 10,
				name="Line"+str(i)
			)
			edge.set_stroke(
				self.edge_propogation_color,
				width = 1.5 * self.edge_stroke_width
			)

			self.edges.add(edge)

	def get_edge_propogation_animations(self):
		"""
		Animación de color
		"""
		animations = []
		for edge in self.edges:
			animations += [ShowCreation(
				edge.copy(),
				run_time=self.edge_propogation_time,
			)]

		return [Succession(*animations)]

	def getEdges(self):
		return self.edges


class Register():
	pass
