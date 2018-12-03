# a simple demo showing how to ignore the errors of a shell command

from opsmop.core.easy import *
import random 

class Main(Role):

    def set_variables(self):
        return dict()

    def set_resources(self):

        return Resources(
            Shell("/usr/bin/true"),
            Shell("/usr/bin/false", ignore_errors=True, register='x'),
            Echo("the result was {{ x }} - {{ x.rc }} - {{ x.data }}"),
            Shell("/usr/bin/false")
        )


class Demo(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(
            Main()
        )

def main():
    return [ Demo() ]



