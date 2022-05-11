import unittest
import os
import json
import shutil
from ruamel.yaml import YAML

import src.python.add_update_publication as mod


class TestAddUpdatePublication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        yaml = YAML()
        yaml.preserve_quotes = True
        with open("_data/authors.yml") as f:
            cls.authors = yaml.load(f)

    def tearDown(self) -> None:
        if os.path.exists('tests/scratch/_posts/papers'):
            shutil.rmtree('tests/scratch/_posts/papers')

    def test_add_publication(self):
        with open("tests/data/add_publication/in.md") as f:
            issue_body = f.read()

        with open("tests/data/add_publication/out.md") as f:
            expected = f.read()

        formatted = mod.main(issue_body, save_dir='tests/scratch/_posts/papers/')

        self.assertEqual(formatted['content'], expected)


    def test_update_publication(self):
        with open("tests/data/update_publication/in.md") as f:
            issue_body = f.read()

        with open("tests/data/update_publication/out.md") as f:
            expected = f.read()

        formatted = mod.main(issue_body, save_dir='tests/scratch/_posts/papers/')
        
        self.assertEqual(formatted['content'], expected)