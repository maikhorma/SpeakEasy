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
from dragonfly.grammar.rule_mapping import MappingRule

"""
    This module demonstrates the use of Dragonfly's CompoundRule class.

    It shows how to use Dragonfly's Grammar, AppContext, and CompoundRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the My Documents\Natlink folder.

"""

from dragonfly import (Grammar, AppContext, CompoundRule, Choice, Dictation,Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

#DON'T give it a context or it will only work once!
#grammar_context = AppContext(executable="notepad")
grammar = Grammar("notepad_example")


#---------------------------------------------------------------------------
# Create a compound rule which demonstrates CompoundRule and Choice types.

class Orders(MappingRule):
    mapping = {
               "Roger [please] start notepad" : "notepad",
               "Roger search [for] <text>" : Text("SEARCH:") + Text("%(text)s")
              }
    extras = [Dictation("text")]
    def _process_recognition(self, node, extras):
        print extras
        print node
        #days_ago  = extras["time"]
        #foodgroup = extras["food"]
        #print "You ate %s %d days ago." % (foodgroup, days_ago)
        #if "opinion" in extras:
        #    print "You thought it was %s." % (extras["opinion"])    

grammar.add_rule(Orders("A"))
#grammar.add_rule(Orders("B"))

#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
#def unload():
#    global grammar
##    if grammar: grammar.unload()
#    grammar = None


import time
import pythoncom

STAY = True

while STAY:
    pythoncom.PumpWaitingMessages()
    time.sleep(1)