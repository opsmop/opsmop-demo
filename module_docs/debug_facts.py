# MODULE:     debugfacts
# PURPOSE:    shows the values of lots of variables at once
# CATEGORY:   special
# PROVIDERS:  debug_facts
# RELATED:    debug
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The DebugFacts values show all the current values of the constant facts available
# within OpsMop. It is important to remember that OpsMop facts are not all constants,
# and some useful facts takes parameters.  The Debug facts module will not dump
# all of those values.  See :ref:`facts` for the full list of available facts.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Here's a really easy way to see what the values of some variables are
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            Echo("I am a {{ Facts.system() }} system"),
            DebugFacts(),
        )

# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def set_resources(self):
        return Roles(
        )

# ---------------------------------------------------------------------------------------
# POLICY: loads all of the above roles
# =======================================================================================

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           BasicExample()
       )

def main():
    return [ Demo() ]


