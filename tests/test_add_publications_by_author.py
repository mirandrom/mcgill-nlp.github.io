import json
import unittest
from textwrap import dedent

import src.python.add_publications_by_author as mod


class TestAddPublicationsByAuthor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('tests/data/add_publications_by_author.json') as f:
            cls.expected = json.load(f)

        issue_body = dedent(
            """
            ### Start

            2020

            ### End

            2020

            ### Author ID

            145732771
            
            """
        )

        cls.out = mod.main(issue_body)
        
    def test_main(self):
        self.assertEqual(self.out['cleaned'], self.expected)

    def test_added_to_ignore(self):
        with open('ignored/semantic_scholar_paper_ids.json') as f:
            ignored = set(json.load(f))
        
        for paper_id in self.out['ignored']:
            self.assertIn(paper_id, ignored)

if __name__ == "__main__":
    unittest.main()
