import unittest
from split_nodes_delimiter import split_nodes_delimiter

from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_text_nodes(self):
        nodes = [
            TextNode("This is a text node with *italics* added", TextType.TEXT),
            TextNode("This is a bold text", TextType.BOLD),
            TextNode("This is another text node", TextType.TEXT)
        ]
        delimiter = "*"
        text_type = TextType.ITALIC
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is a text node with ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" added", TextType.TEXT),
            TextNode("This is a bold text", TextType.BOLD),
            TextNode("This is another text node", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_invalid_delimiter_count(self):
        nodes = [
            TextNode("This is a text node with `code` added", TextType.TEXT),
            TextNode("This is a bold text", TextType.BOLD),
            TextNode("This is another text node with an ``odd` delimiter", TextType.TEXT)
        ]
        delimiter = "`"
        text_type = TextType.CODE
        # Expecting an exception due to odd number of delimiters in the last node
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, delimiter, text_type)
        self.assertTrue("Invalid delimiter count in node text" in str(context.exception))

    def test_no_delimiter(self):
        nodes = [
            TextNode("This is a text node without delimiters", TextType.TEXT),
            TextNode("This is a bold text", TextType.BOLD),
            TextNode("This is another text node", TextType.TEXT)
        ]
        delimiter = "*"
        text_type = TextType.ITALIC
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is a text node without delimiters", TextType.TEXT),
            TextNode("This is a bold text", TextType.BOLD),
            TextNode("This is another text node", TextType.TEXT)
        ]
        self.assertEqual(result, expected)