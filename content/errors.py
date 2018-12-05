# a simple demo showing how to ignore and manipulate the error status of the shell command

from opsmop.core.easy import * 

class Main(Role):

    def set_variables(self):
        return dict(a=5, b=6, c=True)

    def set_resources(self):

        MATCHED_OUTPUT = Eval('"hi" in z.data')

        return Resources(
            
            # a non-zero return code, so this will pass 
            Shell("/usr/bin/true"),
            
            # explicitly ignoring errors
            Shell("/usr/bin/false", ignore_errors=True, register='x'),
            Echo("the result was {{ x }} - {{ x.rc }} - {{ x.data }}"),
            
            # conditionally ignoring errors, in a trivial way
            Shell("/usr/bin/false", failed_when=False),

            # conditionally deciding when to ignore errors
            Shell("/usr/bin/false", register='y', failed_when=Eval('y.rc !=0 and not c')),

            # considering the output to decide when to fail, also showing the condition assigned to a variable
            Shell("echo hi", register='z', failed_when=MATCHED_OUTPUT)
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



