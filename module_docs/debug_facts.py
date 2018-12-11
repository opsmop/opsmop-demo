# MODULE:     debugfacts
# PURPOSE:    shows the values of lots of variables at once
# CATEGORY:   special
# PROVIDERS:  debug_facts
# RELATED:    debug
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The DebugFacts module shows most of the values of the basic facts available
# within OpsMop. It is important to remember that OpsMop facts are not all constants,
# and some useful facts take parameters.  The DebugFacts module will not dump
# those facts that take parameters. See :ref:`facts` for the full list of available facts.
# Using the DebugFacts modules is a great way to figure out what Fact to use in a
# template, or what value to check against in a conditional.
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
            Echo("I am a {{ Platform.system() }} system"),
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

if __name__ == '__main__':
    Cli(Demo())


