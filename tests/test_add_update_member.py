import unittest
from textwrap import dedent

import src.python.add_update_member as mod


class TestAddUpdateMember(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     with open('tests/data/expected_post.md') as f:
    #         cls.expected = f.read()

    def test_update_member(self):
        issue_body = dedent(
            """
            ### Action

            Update member

            ### Name

            Nicholas Meade

            ### Role

            PhD

            ### Status

            Current Member

            ### Avatar

            https://ncmeade.github.io/images/profile.png

            ### Advisor

            _No response_

            ### Date

            _No response_

            ### Bio

            _No response_

            ### Note

            _No response_

            ### GitHub

            _No response_

            ### Twitter

            _No response_

            ### Scholar

            _No response_

            ### Website

            _No response_

            ### New Role

            _No response_
            """
        )
        out = mod.main(issue_body)
        import json
        with open('tests/data/add_update_member_expected.json', 'w') as f:
            json.dump(out, f, indent=2)
