import os
import json
import unittest
from textwrap import dedent

import src.python.add_publications_by_author as mod


class TestAddPublicationsByAuthor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        papers = self.out['cleaned']
        file2paper = {x['filename']:x for x in papers}

        expected_papers_dir = 'tests/data/add_publications_by_author_expected'

        for file in os.listdir(expected_papers_dir):
            with open(os.path.join(expected_papers_dir, file)) as f:
                expected_paper = f.read()
            self.assertIn(file, file2paper)
            self.assertEqual(file2paper[file]['content'], expected_paper)

    def test_added_to_ignore(self):
        with open('ignored/semantic_scholar_paper_ids.json') as f:
            ignored = set(json.load(f))
        
        for paper_id in self.out['ignored']:
            self.assertIn(paper_id, ignored)

if __name__ == "__main__":
    unittest.main()
