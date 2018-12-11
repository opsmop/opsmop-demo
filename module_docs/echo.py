# MODULE:     echo
# PURPOSE:    prints strings and status to the user
# CATEGORY:   special
# PROVIDERS:  echo
# RELATED:    debug, file
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Echo module shows strings during the application of an OpsMop policy.
# Unlike other modules, strings are automatically assumed to be templates.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# If you install cowsay and export "MOO=1" this example will be more entertaining.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            Debug(),
            Echo("The value of a is {{ a }}")
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




 
