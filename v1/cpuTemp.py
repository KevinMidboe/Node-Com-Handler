#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-28 13:56:48
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-01-28 13:58:35

from pyspectator.processor import Cpu
from time import sleep

cpu = Cpu(monitoring_latency=1)
with cpu:
	for _ in range(8):
		cpu.load, cpu.temperature
		sleep(1.1)
