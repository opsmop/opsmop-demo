#
# this is a contrived example designed to teach variable scoping behavior.
#
# usage:
#
#     opsmop apply content/var_scoping.py
#
# ==============================================================================

from opsmop.core.easy import *

# ==============================================================================

class One(Role):

    def set_variables(self):

        return dict(glorp='fizz', level='one')

    def set_resources(self):

        return Resources(
            
            Echo("Role parameterization can work by kwargs. foosball={{ foosball }}"),
            Echo("Role parameterization can work by set_variables. glorp={{ glorp }}"),
            Echo("Policies can be parameterized, blarg={{ blarg }}"),
            Echo("Policy scope is available, other={{ other }} and should be True"),

            # Global(global_var='blippy')

            Echo("Inside the Role 'One', level={{ level }} and should be 'one'"),

            Set(level='runtime'),

            Resources(
                Set(level='nested'),
                Echo("Inside a nested scope, level={{ level }} and should be 'nested'")
            ),

            Echo("Back outside that scope, level={{ level }} and should be 'runtime'")
        )

# ==============================================================================

class Two(Role):

    def set_variables(self):
        return dict(level='two')

    def set_resources(self):

        return Resources(

            Echo("Policies can be parameterized, blarg={{ blarg }}"),
            Echo("Roles can be parameterized. foosball={{ foosball }} and should be 2 or 3"),

            # future feature (soon):
            # SetGlobal(blippy='foo'),
            # Echo("Global variables can be set. global_var={{ blippy }}"),
 
            Echo("This role defines level differently than the Role 'One'. level={{ level }} and should be two")

        )

# ==============================================================================

class ScopeTest(Policy):

    def set_variables(self):
        return dict(level='Scope', other=True)

    def set_roles(self):

        return Roles(

            One(foosball=1),

            Two(foosball=2),

            Two(foosball=3)
        )

EXPORTED = [
    ScopeTest(blarg=5150)
]

