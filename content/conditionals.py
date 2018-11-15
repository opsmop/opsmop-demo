
from opsmop.core.easy import *
import random 

# this is a contrived example designed to teach about conditionals and also templating
# for experienced users of config management systems

class Main(Role):

    def set_variables(self):

        # DEMO: role variables!
        # every role can define some variables that are specific to that role
        # because this is Python they can come from *wherever*
        return dict(a=2, b=1, c="says_go", d="says_go", e=True, f=True, g=False, y=5)

    def set_resources(self):

        # Demo: Conditionals!
        # conditionals are just python classes.
        # for this example we won't assign all conditionals to variables
        # but you easily can, and this can make things more clear

        return Resources(

            # DEMO: Basic Handlers, and also a template demo!            
            File(name="/tmp/foo1.txt", from_template="templates/foo.j2", signals='file1changed', mode=0x777),
            File(name="/tmp/foo2.txt", from_file="files/foo2.txt", signals='file2changed'),
            File(name="/tmp/foo3.txt", from_file="files/foo3.txt", signals='file3changed'),

            # DEMO: Variables in strings and templates! F is for facts, V is for variables.
            Echo("the OS distribution is {{ F.os_type }}"),
            Echo("the value of x is {{ x }}"),

            # DEMO: basic and advanced conditional tests
            # Shell("echo test", when="'/etc/motd.txt' | present"), # we'll need some filters
            Echo("x is true at run time", when='x'),
            Echo("a > b", when="a > b"),
            Echo("c says go", when="c == 'says_go'"),
            Echo("this is unix? {{ F.os_type }}"),
            Echo("all are true?", when="e and f and g"),
            Echo("one is true?", when="e or f or g"),

            # DEMO: Nested Resources with a conditional attached!
            Resources(
                [ Echo("group1"), Echo("group2") ],
                when="a == 2"
            ),
 
            # DEMO: use results in subsequent methods
            Shell(cmd="date", register="date", ignore_errors=True),
            Echo("shell output was {{ date.data }}"),
            Echo("the shell command was ok", when="date.rc == 0"),

            # DEMO: Dynamic Variable Assignment
            # The set operation allows creating variables dynamically.  Strings can contain template
            # expressions which are lazily evaluated at runtime. Other Python things are evaluated
            # at load time, and any Python is fair game. Remember to access anything set with
            # Set() we have to use Jinja2 expressions in quotes, otherwise we don't need to.

            Set(foo=0, bar=random.random(), baz=Eval("x + 2"), glorp=Eval("x + y"), want="tails"),
            
            Echo("want={{ want }}"),

            # working on this...
            # Stop("bar = {{ bar }}", when="0.9 > 0.5")

        )

    def set_handlers(self):

        # DEMO: event handlers!
        return Handlers(
            file1changed = Shell(cmd="echo file1 has changed"),
            file2changed = Shell(cmd="echo file2 has changed"),
            file3changed = Shell(cmd="echo file3 has changed")
        )


class Demo(Policy):

    # DEMO: Scope!
    # Variables set at policy scope are available to all roles under that policy
    def set_variables(self):
        return dict(mouse1='Pinky', mouse2='Brain', place='Acme Labs', x=True, y=False, z=True)

    def set_roles(self):
        return Roles(
            Main()
        )

EXPORTED = [
    Demo()
]

