# MODULE:     set
# PURPOSE:    adds variables into the OpsMop namespace
# CATEGORY:   special
# PROVIDERS:  set
# RELATED:    template, debug
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Set module can store arbitrary variables.  These can be constants or the
# results of Eval() calls. For another good example see the 'var_scoping'
# example in the content/ directory of the opsmop-demo repo.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            Debug(),
            Set(a=5, b=2112, c="ood", d=8675309),
            Debug(),
            Set(e=Eval('a+b'), f=Eval('c.upper()'), g=Facts.os_type()),
            Debug(),
            Echo("The values are now, {{ e }}, {{ f }}, and {{ g }}")
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




 
