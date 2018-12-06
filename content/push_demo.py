# push mode support for OpsMop is still under development.
# here is an example of what inventory and push mode might look like

from opsmop.core.easy import *

# for local usage:
#   bin/opsmop --apply filename.py
# for push usage
#   bin/opsmop-push --apply filename.py
    
inventory = TomlInventory("inventory/inventory.toml")

class WebServers(Role):

    def push_to(self):
        return inventory.filter('webservers*')

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
    return [ Demo() ]

