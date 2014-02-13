#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#

"""
    This file offers an interface to the Win32 cursor control.

"""


import win32gui
import ctypes

from ..log       import get_log


#===========================================================================
# Monitor info retrieval below lightly inspired by the following recipe:
#  http://code.activestate.com/recipes/460509/ by Martin Dengler (2005)
#  More info available here:
#  http://msdn.microsoft.com/en-us/library/ms534809.aspx

class _point_t(ctypes.Structure):
    _fields_ = [
                ('x',  ctypes.c_long),
                ('y',  ctypes.c_long),
               ]

def get_cursor_position():
    point = _point_t()
    result = ctypes.windll.user32.GetCursorPos(ctypes.pointer(point))
    if result:  return (point.x, point.y)
    else:       return None
