import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_valid_markdown(self):
        markdown = "# My Title\nThis is some content."
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")

    def test_extract_title_without_title(self):
        markdown = "This is some content without a title."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No title found in markdown content." in str(context.exception))

    def test_extract_title_with_multiple_lines(self):
        markdown = "# First Title\n# Second Title\nContent here."
        title = extract_title(markdown)
        self.assertEqual(title, "First Title")