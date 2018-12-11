# MODULE:     debug
# PURPOSE:    shows the values of lots of variables at once
# CATEGORY:   special
# PROVIDERS:  debug
# RELATED:    asserts, echo, set
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Debug module is a powerful way to figure out what the value of a variable
# is at runtime inside OpsMop.
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
            Set(d=1234),
            # show everything in variable memory for this scope
            Debug(),
            # just show some things
            Debug('a', 'b', 'c'),
            # also debug some evaluated results and platform Facts
            Debug('a', 'b', 'c', os_type=Platform.system(), expr=Eval('a + 1000'))
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


