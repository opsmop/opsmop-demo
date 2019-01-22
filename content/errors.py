# a simple demo showing how to ignore and manipulate the error status of the shell command

from opsmop.core.easy import * 

class Main(Role):

    def set_variables(self):
        return dict(a=5, b=6, c=True)

    def main(self):

        # a non-zero return code, so this will pass 
        Shell("/usr/bin/true"),
            
        # explicitly ignoring errors
        x = Shell("/usr/bin/false", ignore_errors=True)
        Echo("the result was {{ x }} - {{ x.rc }} - {{ x.data }}")
        if x.rc == 42:
            # this won't happen, but you can raise arbitrary exceptions
            raise Exception("failed")
        
        # conditionally ignoring errors, in a trivial way
        Shell("/usr/bin/false", failed_when=False)

        # conditionally deciding when to ignore errors
        Shell("/usr/bin/false", failed_when=lambda o: o.rc == 0)

        # considering the output to decide when to fail, also showing the condition assigned to a variable
        Shell("echo hi", failed_when=lambda o: 'hi' not in o.data)

        # exception handling
        try:
            Shell("/usr/bin/false")
        except:
            Echo("exception recovered")

        Echo("this next step will fail")

        Shell("/usr/bin/false")

class Demo(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(
            Main()
        )
        
if __name__ == '__main__':
    Cli(Demo())



