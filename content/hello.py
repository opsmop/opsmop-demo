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

    def set_resources(self):

        msg = T("Hello {{ program }} World! {{ say}}!")

        return Resources(
            File(name="/tmp/foo.txt", from_content=msg, signals="file_changed")
        )

    def set_handlers(self):
        return Handlers(
            file_changed = Echo("file has changed")
        )

# -----------------

class Hello(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(HelloRole())

if __name__ == '__main__':
    Cli(Hello(say='Congratulations'))
