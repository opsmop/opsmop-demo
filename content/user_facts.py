# this is a demo of UserFacts which uses files baked into 
# /etc/opsmop/facts.d to implement feature flags

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

class FeatureOne(Role):

    def should_process_when(self):
        return UserFacts.get('feature_flags','ff01')

    def set_resources(self):

        command = T("Set warp speed to {{ UserFacts.warp_factor }}, Engage!")

        return Resources(
            DebugFacts(),
            Echo("The security offer is {{ UserFacts.crew.officers.security }}"),
            Set(command=command),
            Echo("The singularity is becoming unstable. {{ command }}")
        )

class FeatureTwo(Role):

    def should_process_when(self):
        return UserFacts.feature_flags.get('ff02',False)

    def set_resources(self):
        return Resources(
            Echo("This won't actually run until you modify feature_flags.json to enable ff02"),
            DebugFacts()
        )

class CommonSetup(Role):

    def set_resources(self):
        resources = Resources()
        resources.add([
            Directory("/etc/opsmop/facts.d", owner=USERNAME),
            File("/etc/opsmop/facts.d/feature_flags.json", from_file="files/feature_flags.json", owner=USERNAME, mode=0o644, signals='yep'),
            File("/etc/opsmop/facts.d/star_trek.yml", from_file="files/star_trek.yml", owner=USERNAME, mode=0o644, signals='yep'),
            File("/etc/opsmop/facts.d/dynamic_facts.sh", from_file="files/dynamic_facts.sh", owner=USERNAME, mode=0o755, signals='yep')
        ])
        return resources

    def set_handlers(self):
        return Handlers(
            yep = Resources(
                Echo("fyi, we just set up /etc/opsmop/facts.d for you"),
                Echo("check out the file contents and edit them if you like")
            )
        )

    def post(self):
        UserFacts.invalidate()

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           FeatureOne(),
           FeatureTwo(),
       )

def main():
    policies = [ Demo() ]
    return policies




 
