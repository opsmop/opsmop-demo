from opsmop.core.easy import *

# cd thisdir
# python3 basics.py --local --check
# python3 basics.py --local --apply

class WebServers(Role):

    def set_variables(self):
        return dict(what='bar', code=1234)

    def main(self):

        # this is not a real example and is just a bunch of resources thrown together
        # illustrating syntax, basic variables, and change detection.
        # a more complete example installing a popular-application may be added later.

        p1 = File(name="/tmp/opsmop-foo.txt", from_content="Hello World!")

        File(name=T("/tmp/opsmop-{{ what }}.txt"), from_content="Hello World 2!") # a dynamic path

        bar_contents = Shell("cat /tmp/opsmop-bar.txt")

        Echo("{{ bar_contents.data }}")

        p2 = Package(name="cowsay", method="brew")

        if p1.changed:
            Service(name='foo', restarted=True)

        if p2.changed:
            Service(name='nginx', restarted=True)
        

class Demo(Policy):

    def set_variables(self):
        return dict(asdf = 'jkl;')

    def set_roles(self):
        return Roles(
            WebServers(name='webservers')
        )
   
if __name__ == '__main__':
    Cli(Demo())

