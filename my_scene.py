#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scene.scene import Scene

from electronics.components import Signal

class MyScene(Scene):

	def construct(self):
		signal = Signal()
		tmp1 = signal.get_edge_propogation_animations()
		import pdb; pdb.set_trace()
		self.play(*tmp1)

