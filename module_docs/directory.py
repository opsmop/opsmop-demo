# MODULE:     directory
# PURPOSE:    creates directories, removes them, and modifies metadata
# CATEGORY:   general
# PROVIDERS:  file
# RELATED:    directory
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Directory module has all of the capabilities of the file module, but is
# used for directories instead of files.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# This should be reasonably self explanatory...
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            Directory(name="/tmp/opsmop-demo/sample_dir", absent=True),
            Directory(name="/tmp/opsmop-demo/sample_dir", owner=USERNAME, mode=0x755)
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


