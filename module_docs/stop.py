# MODULE:     stop
# PURPOSE:    stop aborts an execution, sharing a specific message
# CATEGORY:   special
# PROVIDERS:  stop
# RELATED:    asserts
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The stop module can be used to end the execution of a policy when it really
# should not continue.  For instance, if your policy really should not run
# on submarines, this is one way how you could do it.
# =======================================================================================

from opsmop.core.easy import *
import getpass

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Here is a really minimal stop example.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        
        return Resources(
            
            Stop("the value of b is too high", when=Eval("b > 100"))

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
           BasicExample(),
       )

def main():
    return [ Demo() ]
