#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2014-12-21 15:21:07
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-01-08 00:44:55

from funcpy import *

print(fp.strlen('Hello'))
print(fp.ucfirst('hello'))
print (fp.substr('Hello',1,2))

data = 'He,l,lo'

print ( fp.explode(' ', data))

print(fp.uclast('hello'))

nums = [1,2,3,23,53,6,7,8,9,10]


print(fp.max(nums))

print(fp.min(nums))

print(fp.mid(nums))

print(fp.sizeof('2'))

print(fp.str_replace("Hello","e","H"))

print(fp.str_reverse("Hello"))