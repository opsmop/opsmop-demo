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
            Debug('foosball', 'glorp', 'blarg', 'other', 'level'),
            Assert(foosball=1),
            Assert(glorp='fizz'),
            Assert(blarg=5150),
            Assert(other=True),
            Assert(level='one'),
            Set(level='runtime'),
            # SetGlobal(blippy='foo'),
            Resources(
                Set(level='nested'),
                # Assert(level='nested'),
            ),
            Assert(level='runtime'),
        )

# ==============================================================================

class Two(Role):

    def set_variables(self):
        return dict(level='two')

    def set_resources(self):

        return Resources(
            Debug('foosball', 'glorp', 'blarg', 'other', 'level'),
            Assert(blarg=5150),
            Echo("foosball={{ foosball }}"),
            # Assert(blippy='foo'),   
            Assert(level='two'),
            # some alternate ways to do things, more as a proof of internals
            Assert('blarg > 3000'),
            Debug('blarg', 'foosball', random=Eval('2 * blarg + 1000'))
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

