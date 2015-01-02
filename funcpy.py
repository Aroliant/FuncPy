#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2014-12-21 15:19:44
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-01-03 00:22:54
import math
	
class fp(object):
	def __init__(self, arg):
		super(fp, self).__init__()
		self.arg = arg

	def max(list):
		return max(list)

	def min(list):
		return min(list)

	def mid(list):
		loc = math.floor((len(list)-1)/2)
		return list[loc]

	def strlen(string):
		return len(string)

	def substr(data,start,length):
		return data[start:length]

	def ucfirst(data):
		return data[0].upper()+data[1:]

	def uclast(data):
		return data[0:len(data)-1]+data[len(data)-1:].upper()

	def explode(splitter, string):
	    if splitter == '':
	        return list(string)
	    else:
	        return string.split(splitter, len(string))	
		