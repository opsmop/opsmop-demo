# MODULE:     shell
# PURPOSE:    runs arbitrary shell commands, with feeling
# CATEGORY:   general
# PROVIDERS:  shell
# RELATED:    file, package, service, set
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Shell module runs arbitrary shell commands. It is frequently used with template
# expressions "T()" to pass variables in for execution.
# =======================================================================================

from opsmop.core.easy import *
import getpass

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Here are various passing asserts and finally one that will end the execution
# of this policy with an error.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        
        return Resources(
            
            # here is an example of running a command and saving the output and return code
            Shell("date | cut -f1 -d ' '", register='date'),
            Echo("today is {{ date.data }} and the return code was {{ date.rc }}"),

            # you can ignore return codes like this
            Shell("/bin/false", ignore_errors=True),

            # or like this - soon
            # Shell("/bin/false", failed_when=Eval('a > b')),

            # you can use variables in shell commands like this:
            Shell(T("echo {{ a }} {{ b }} {{ c }}")),

        )

# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def set_resources(self):
        return Roles(
        )

# ---------------------------------------------------------------------------------------
# POLICY: loads all of the above roles
# =======================================================================================

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           BasicExample(),
       )

if __name__ == '__main__':
    Cli(Demo())
