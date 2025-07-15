import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is a **bold** text with _italics_ and `code`."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_with_image(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_with_link(self):
        text = "This is a text with a [link](https://example.com)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_with_multiple_formats(self):
        text = "This is a **bold** text with _italics_ and ![image](https://i.imgur.com/zjjcJKZ.png) and [link](https://example.com)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)


