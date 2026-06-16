import unittest
from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = """
# this is a test title
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "this is a test title"
        )

    def test_extract_nmissing_title(self):
        md = "## this is an incorrect title"
        with self.assertRaises(Exception):
            extract_title(md)