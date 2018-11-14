from opsmop.core.easy import *

# bin/opsmop check hello.py
# bin/opsmop apply hello.py

class HelloRole(Role):

    def set_variables(self):
        return dict(program='OpsMop')

    def set_resources(self):
        return Resources(
            File(name="/tmp/foo.txt", from_content="Hello {{ V.program }} World! {{ V.ready }}")
        )

    def set_handlers(self):
        return Handlers()

class Hello(Policy):

    def set_variables(self):
        return dict(ready='Congratulations')

    def set_roles(self):
        return Roles(HelloRole())
   
EXPORTED = [
    Hello(),
]

