# push mode support for OpsMop is still under development.
# here is an example of what inventory and push mode might look like

from opsmop.core.easy import *

# cd thisdir
# python3 push_demo.py --push --check
# python3 push_demo.py --push --apply
    
inventory = None

class BaseRole(Role):

    def ssh_as(self):
        # most users will want to omit this method and instead have a ~/.opsmop/defaults.toml
        return ('mpdehaan', None)

    def sudo(self):
        return True

    def sudo_as(self):
        # if required, a password can be read from ~/.opsmop/defaults.toml
        return ('root', None)

class WebServers(Role):

    def inventory(self):
        return inventory.filter('webservers*')

    def set_variables(self):
        return dict(x=5, y=6)

    def set_resources(self):
        return Resources(
            Debug(),
            File("/tmp/foo1.txt", from_template="templates/foo.j2"),
            File("/tmp/foo2.txt", from_file="files/foo2.txt", mode=0o770),
			File("/tmp/foo3.txt", from_content="Hey!"),
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
   
if __name__ == '__main__':
    inventory = TomlInventory("inventory/inventory.toml")
    Cli(Demo())

