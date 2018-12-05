from opsmop.core.easy import *

# bin/opsmop --validate filename.py
# bin/opsmop --check filename.py
# bin/opsmop --apply filename.py

class WebServers(Role):

    def set_variables(self):
        return dict(what='bar', code=1234)

    def set_resources(self):

        # this is not a real example and is just a bunch of resources thrown together
        # a more complete example installing a popular-application  may be added later.

        return Resources(

            File(name="/tmp/opsmop-foo.txt", from_content="Hello World!", signals="restart_foo"),

            File(name=T("/tmp/opsmop-{{ what }}.txt"), from_content="Hello World 2!"), # a dynamic path

            Shell("cat /tmp/opsmop-bar.txt", register="bar_contents"),

            Echo("{{ bar_contents.data }}"),

            Package(name="cowsay", method="brew", signals="restart_nginx"),

            Echo("resources complete!")

        )

    def set_handlers(self):
        return Handlers(
            restart_nginx = Service(name='nginx', restarted=True),
            restart_foo   = Service(name='foo', restarted=True),
        )

class Demo(Policy):

    def set_variables(self):
        return dict(asdf = 'jkl;')

    def set_roles(self):
        roles = [ WebServers(name='webservers'), ]
        return Roles(*roles)
   
def main():
    return [ Demo() ]

