#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy
from os import path
from tempfile import NamedTemporaryFile
from xml.etree import ElementTree

from manim import *
from mobject.geometry import *
from mobject.svg.svg_mobject import *
from animation.animation import *
from animation.creation import *
from animation.indication import *
from animation.transform import *


class SvgBuilder():
	"""
	Construye la estructura a partir de un svg. Los rect son registros, el
	resto son señales combinacinales
	"""

	def __init__(self, path):
		self.registers = None
		self.combinational = None
		self._cycle_time = 10
		self._register_transform_time = 1

		if not os.path.isabs(path):
			path = SVG_IMAGE_DIR + os.sep + path

		if path is None or not os.path.exists(path):
			return

		self._init_from_file(path)

	def _init_from_file(self, path):
		combinationals = [
			"circle",
			"ellipse",
			"line",
			"polygon",
			"polyline",
			"path",
		]
		import pdb;pdb.set_trace()
		with open(path) as f:
			xml = ElementTree.parse(f)
			tree = xml.getroot()
			regsEt = deepcopy(xml)
			combEt = deepcopy(xml)
			regs = regsEt.getroot()
			comb = combEt.getroot()

		to_remove = []
		for el in comb.iterfind('{http://www.w3.org/2000/svg}rect'):
			to_remove.append(el)

		map(lambda x: comb.remove(x), to_remove)

		to_remove = []
		for tag in combinationals:
			for el in regs.iterfind('{http://www.w3.org/2000/svg}' + tag):
				to_remove.append(el)
		
		map(lambda x: regs.remove(x), to_remove)

		g = NamedTemporaryFile()
		h = NamedTemporaryFile()
		combEt.write(g.name,default_namespace=None)
		regsEt.write(h.name,default_namespace=None)

		self.registers = SVGMobject(file_name=g.name)
		self.registers.set_stroke(width=1,color="White")
		self.registers.set_fill(opacity=0)
		self.combinational = SVGMobject(file_name=h.name)
		self.combinational.set_stroke(width=1,color="White")
		self.combinational.set_fill(opacity=0)

		if not g.closed:
			g.close()
		if not h.closed:
			h.close()

	def get_animation(self):
		retval = []
		from_anim = self.registers.copy()
		from_anim.set_stroke(width=1,color=BLUE_E)
		to_anim = self.registers.copy()
		to_anim.set_stroke(width=1,color=RED_E)
		return ReplacementTransform(from_anim, to_anim)

	def get_registers(self):
		return self.registers

	def get_combinational(self):
		return self.combinational


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
