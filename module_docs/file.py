#
# Module:     File
# Type:       file
# Provider:   file
#
# //TODO: (auto-load the parameters by instantiating the type, sort and pull off the help texts)
#
# Description:
# 
# The File module handles all major types of file operations in OpsMop.
#

from opsmop.core.easy import *

# Example: Template
#
# Templating a file from a jinja2 template
#
# Embed: templates/foo.txt.j2

class Jinja2Example(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def set_resources(self):
        return Resources(
            File(name="/tmp/opsmop-demo/foo1.txt", from_template="templates/foo.txt.j2"),
            Shell("cat /tmp/opsmop-demo/foo1.txt"
        )

# Example: Copy
#
# Copying a file with owner, permission, and mode

class CopyExample(Role):

    def resources(self):
        return Resources(
             File(name="/tmp/opsmop-demo/foo2.txt", from_file="files/foo.txt", owner=root, mode=0x755),
             Shell("cat /tmp/opsmop-demo/foo2.txt")
        )    

# Example: Copy From String
#
# For very small files, this is also possible

class ContentExample(Role):

    def resources(self):
        return Resources(
             File(name="/tmp/opsmop-demo/foo3.txt", content="Happy Birthday"),
             Shell("cat /tmp/opsmop-demo/foo3.txt")
        )

# Prepare: This is a common role that is used to setup for the examples below

class CommonSetup(Role):

    def resources(self):
        return Directory(name="/tmp/opsmop-demo/")

# Policy: This runs the Demo

class Demo(Policy):

    def roles(self):
       return Roles(
           CommonSetup(),
           Jinja2TemplateExample(d=4, e=5, f=6),
           CopyExample(),
           ContentExample()
       )

def main():
    return [ Demo() ]








 
