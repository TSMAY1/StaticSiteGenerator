import unittest
from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImagesAndLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and another [link](https://example.org)"
        )
        self.assertListEqual(
            [("link", "https://example.com"), ("link", "https://example.org")], matches
        )