# this is a demo of UserFacts which uses files baked into 
# /etc/opsmop/facts.d to implement feature flags

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

class FeatureOne(Role):

    def should_process_when(self):
        return UserFacts.feature_flags.get('ff01', False)

    def main(self):

        command = T("Set warp speed to {{ UserFacts.warp_factor }}, Engage!")
        DebugFacts()
        Echo("The security officer is {{ UserFacts.crew.officers.security }}")
        Echo("The singularity is becoming unstable. {{ command }}")

class FeatureTwo(Role):

    def main(self):

        if not UserFacts.feature_flags.get('ff02', False):
            return

        Echo("This won't actually run until you modify feature_flags.json to enable ff02")
        DebugFacts()

class CommonSetup(Role):

    def main(self):
        f1 = Directory("/etc/opsmop/facts.d", owner=USERNAME)
        f2 = File("/etc/opsmop/facts.d/feature_flags.json", from_file="files/feature_flags.json", owner=USERNAME, mode=0o644),
        f3 = File("/etc/opsmop/facts.d/star_trek.yml", from_file="files/star_trek.yml", owner=USERNAME, mode=0o644),
        f4 = File("/etc/opsmop/facts.d/dynamic_facts.sh", from_file="files/dynamic_facts.sh", owner=USERNAME, mode=0o755)

        if f1.changed or f2.changed or f3.changed or f4.changed:
            Echo("fyi, we just set up /etc/opsmop/facts.d for you")
            Echo("check out the file contents and edit them if you like")

        UserFacts.invalidate()

class Demo(Policy):

    def set_roles(self):
        return Roles(
            CommonSetup(),
            FeatureOne(),
            FeatureTwo()
        )

if __name__ == '__main__':
    Cli(Demo())



 
