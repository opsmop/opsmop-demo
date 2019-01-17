#
# A very minimal language example
#
# USAGE:
#
# bin/opsmop check hello.py
# bin/opsmop apply hello.py
#

from opsmop.core.easy import *

class HelloRole(Role):

    def set_variables(self):
        return dict(program='OpsMop')

    def main(self):

        msg = T("Hello {{ program }} World! {{ say}}!")

        f1 = File(name="/tmp/foo.txt", from_content=msg)

        if f1.changed:
            Echo("file has changed")

# -----------------

class Hello(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(HelloRole())

if __name__ == '__main__':
    Cli(Hello(say='Congratulations'))
