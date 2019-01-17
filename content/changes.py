# a simple demo showing change controls
# 
# normally a shell command will always notify a handler
# how do we control that based on return codes or  output?

from opsmop.core.easy import *
import random 

class Main(Role):

    def set_variables(self):
        return dict(a=5, b=6, c=True)

    def main(self):

        def danger(x):
            return x.rc == 7 or 'fence power down' in x.data

        s1 = Shell("echo 'fence power down'", ignore_errors=True, changed_when=danger)
        s2 = Shell("echo 'all good'", ignore_errors=True, changed_when=danger)
        
        if s1.changed or s2.changed:
            Echo("Sound the alarm!")

class Demo(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(
            Main()
        )

if __name__ == '__main__':
    Cli(Demo())


