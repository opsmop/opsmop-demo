# push mode support for OpsMop is still under development.
# here is an example of what inventory and push mode might look like

from opsmop.core.easy import *

# for local usage:
#   bin/opsmop --apply filename.py
# for push usage
#   bin/opsmop-push --apply filename.py

class WebServers(Role):

    def set_variables(self):
        return dict(what='bar', code=1234)

    def set_resources(self):

        return Resources(
            Shell("uname -a")
        )

    def set_handlers(self):
        return Handlers(
        )

class Demo(Policy):

    def set_variables(self):
        return dict(asdf = 'jkl;')

    def set_roles(self):
        return Roles(
            WebServers(name='webservers', tag='webservers')
        )
   
def main():

    # the inventory is global and you can load as many inventories as you want

    inventory = TomlInventory().load("inventory/inventory.toml")
    # inventory.map(group='webservers', tag='webservers')

    # now return the policies that you want to use in local mode (with --tags)
    # or in push mode (the tags will be automatically applied)

    return [ Demo() ]

