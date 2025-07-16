import unittest

from main import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_heading(self):
        md = """
# This is a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )   

    def test_unordered_list(self):
        md = """
- This is an unordered list item
- This is another item
* This is a third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list item</li><li>This is another item</li><li>This is a third item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list item
2. This is another item
3. This is a third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list item</li><li>This is another item</li><li>This is a third item</li></ol></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )   

        