# MODULE:     user
# PURPOSE:    manages user accounts
# CATEGORY:   general
# PROVIDERS:  user.useradd
# RELATED:    group
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The user module manages user accounts. Certain parameters can only be set at creation time.
# Also see the group module for additional capabilities.
# =======================================================================================

from opsmop.core.easy import *

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Creating and removing some users
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
       return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            User(name="opsmguest1"),
            User(name="opsmguest2", uid=3003, group="sudo", groups=['vespene'], shell="/bin/bash"),
            User(name="opsmguest3", system=True),
            User(name="opsmguest1", absent=True)
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




 
