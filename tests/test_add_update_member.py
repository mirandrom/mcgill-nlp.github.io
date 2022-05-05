import unittest
import json
from ruamel.yaml import YAML

import src.python.add_update_member as mod


class TestAddUpdateMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        yaml = YAML()
        yaml.preserve_quotes = True
        with open("_data/authors.yml") as f:
            cls.authors = yaml.load(f)

    def test_add_member(self):
        with open("tests/data/add_member_issue_body.md") as f:
            issue_body = f.read()

        out = mod.main(issue_body)

        with open("tests/data/add_member_expected.json") as f:
            expected = json.load(f)
        
        output = json.loads(json.dumps(out['John Doe']))
        self.assertEqual(output, expected)

    def test_update_member(self):
        with open("tests/data/update_member_issue_body.md") as f:
            issue_body = f.read()

        out = mod.main(issue_body)

        with open("tests/data/update_member_expected.json") as f:
            expected = json.load(f)
        
        
        output = json.loads(json.dumps(out['John Doe']))

        self.assertEqual(output, expected)
    