import os
import unittest
import json

from analysis import extract_article_metadata

HERE = os.path.dirname(os.path.abspath(__file__))
test_doc_path = os.path.join(HERE, 'test-doc.json')


class TestAnalysis(unittest.TestCase):
    def setUp(self) -> None:

        with open(test_doc_path, 'r') as f:
            self.doc = json.load(f)

    def test_extract_article_metadata(self):

        meta = extract_article_metadata(self.doc)

        self.assertEqual(meta['word_count'], 2248)
        self.assertEqual(meta['section_name'].lower(), 'opinion')

