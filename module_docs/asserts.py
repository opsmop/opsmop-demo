# MODULE:     asserts
# PURPOSE:    fails policy application when certain conditions are not true
# CATEGORY:   special
# PROVIDERS:  asserts
# RELATED:    debug, echo, set, stop
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Assert module will fail a policy application when certain conditions are not true.
# These may be passed in as key=value parameters and also as deferred expressions
# such as Eval()
# =======================================================================================

from opsmop.core.easy import *
import getpass

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Here are various passing asserts and finally one that will end the execution
# of this policy with an error.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        python_var = 2112
        check1 = Eval('b > 5000')
        check2 = Eval("c.upper() == 'BLUE'")

        return Resources(


            Set(c="blue"),
            Debug(),
            Asserts(a=1, b=5150),
            Asserts(Eval('b > 5000')),
            Asserts((python_var > 2000)),
            Asserts(c="blue"),
            Asserts(check2),

            # this will fail
            Asserts(b=3)
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

if __name__ == '__main__':
    Cli(Demo())


