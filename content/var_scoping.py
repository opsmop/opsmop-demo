#
# this is a contrived example designed to teach variable scoping behavior.
#
# usage:
#
#     opsmop apply content/var_scoping.py
#
# ==============================================================================

from opsmop.core.easy import *

# ==============================================================================

class One(Role):

    def set_variables(self):
        # here these are hard coded but they could also come from a database lookup
        # or from a config file
        return dict(some_unused_variable='...', level=1, foo=dict(x=1, y=2))

    def main(self):
        car = "DeLorean"

        Echo("level={{ level }}, color={{ color }}, car={{ car }}, code={{ code }}, y={{ foo.y }} ") 
        # direct variable access from Python works like this:
        # Echo("level = %s" % self.vars.level)
        # Echo("color = %s" % self.vars.color)

# ==============================================================================

class Two(Role):

    def set_variables(self):
        return dict(level='two', foo=dict(x=3,y=4))

    def main(self):
        car = "NSX"
        code = 8675309
        Echo("level={{ level }}, color={{ color }}, car={{ car }}, code={{ code }}, y={{ foo.y }}")

# ==============================================================================

class ScopeTest(Policy):

    def set_variables(self):
        return dict(level=0, other=True)

    def set_roles(self):
        return Roles(
            One(color='red'),
            Two(color='green'),
            Two(color='blue')
        )

if __name__ == '__main__':
    Cli(ScopeTest(code=5150))

