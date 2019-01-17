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

class WebServers(BaseRole):
    
    def inventory(self):
        return inventory.filter(groups='webservers*')

    def set_variables(self):
        return dict(x=5, y=6, z=7)

    def main(self):
        Debug()
        f1 = File("/tmp/foo3.txt", from_content="Hey!")
        f2 = File("/tmp/foo1.txt", from_template="templates/foo.j2")
        Shell("uname -a", changed_when=False)

        if f1.changed:
            Echo("one")
            Echo("two")
        if f2.changed:
            Echo("three")

    def allow_fileserving_paths(self):
        # this is optional, the default is just '.' which means where this file is
        # if you want to allow things like from_file='/opt/foo/bar.txt'
		# return [ '.', '/opt/foo' ]
        return [ '.' ]

class AnotherRole(BaseRole):

    # this example demonstrates load balancing hooks
    def should_contact(self, host):
        # optional. this is like should_process_when but executes before we try to connect to the host
        return True
    
    def after_contact(self, host):
        # optional. hook that can be used to put a node back in a load balancer, etc
        # print("balance %s" % host.hostname())
        pass    

    def before_contact(self, host):
        # optional hook. that can be used to pull a node out of a load balancer, etc
        # print("unbalance %s" % host.hostname())
        pass

    def serial(self):
        # number of hosts to process at once
        return 5

    def inventory(self):
        return inventory.filter(groups=['webservers*','dbservers*'])

    def main(self):
        Echo("hi")
        File("/tmp/foo2.txt", from_file="files/foo2.txt", mode=0o770)
        Echo("that was easy")

class Demo(Policy):

    def set_variables(self):
        return dict(asdf = 'jkl;')

    def set_roles(self):
        return Roles(
            WebServers(name='webservers', tag='webservers'),
            AnotherRole(tag='another')
        )

    def allow_fileserving_patterns(self):
        # this is totally optional, the default is '*'
        return [ '*.txt', '*.j2' ]

    def deny_fileserving_patterns(self):
        # this is also optional, the defaults are already set
        return Policy.DEFAULT_DENY_FILESERVING_PATTERNS
   
if __name__ == '__main__':
    inventory = TomlInventory("inventory/inventory.toml")
    Cli(Demo())

