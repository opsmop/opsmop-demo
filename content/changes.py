# a simple demo showing change controls
# 
# normally a shell command will always notify a handler
# how do we control that based on return codes or  output?

from opsmop.core.easy import *
import random 

class Main(Role):

    def set_variables(self):
        return dict(a=5, b=6, c=True)

    def set_resources(self):

        VELOCIRAPTOR_DANGER = Eval("z.rc == 7 or 'fence power down' in z.data")

        return Resources(
            
            Shell("echo 'fence power down'", register='z', changed_when=VELOCIRAPTOR_DANGER, signals='evt_01'),
            Shell("echo 'all good'", register='z', changed_when=VELOCIRAPTOR_DANGER, signals='evt_02'),
        )


    def set_handlers(self):
        return Handlers(
            evt_01 = Echo("Sound the alarm!"),
            evt_02 = Echo("Sound the alarm, also!"),
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



