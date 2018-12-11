# MODULE:     groups
# PURPOSE:    manages user groups
# CATEGORY:   general
# PROVIDERS:  group.groupadd
# RELATED:    user
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# Manages groups. To control what users are in what groups, see :ref:`module_user`.
# =======================================================================================

from opsmop.core.easy import *

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Basic group operations.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
       return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            Group(name="opsmgrp1"),
            Group(name="opsmgrp2", gid=8008),
            Group(name="opsmgrp3", system=True),
            Group(name="opsmgrp1", absent=True)
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




 
