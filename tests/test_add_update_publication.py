import unittest
import json
from ruamel.yaml import YAML

import src.python.add_update_publication as mod


class TestAddUpdatePublication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        yaml = YAML()
        yaml.preserve_quotes = True
        with open("_data/authors.yml") as f:
            cls.authors = yaml.load(f)

    def test_add_publication(self):
        with open("tests/data/add_publication_issue_body.md") as f:
            issue_body = f.read()

        with open("tests/data/add_publication_expected.md") as f:
            expected = f.read()

        formatted = mod.main(issue_body)

        self.assertEqual(formatted['content'], expected)


    def test_update_publication(self):
        with open("tests/data/update_publication_issue_body.md") as f:
            issue_body = f.read()

        with open("tests/data/update_publication_expected.md") as f:
            expected = f.read()

        formatted = mod.main(issue_body)
        
        self.assertEqual(formatted['content'], expected)