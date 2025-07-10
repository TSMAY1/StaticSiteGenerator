import unittest
from markdown_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):

        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_empty(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        def test_markdown_to_blocks_single_line(self):
            md = "This is a single line"
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["This is a single line"])

        def test_markdown_to_blocks_multiple_empty_lines(self):
            md = "\n\nThis is a paragraph with multiple empty lines\n\n\n"
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["This is a paragraph with multiple empty lines"])

class TestBlockType(unittest.TestCase):

    def test_block_type_paragraph(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_type_heading(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_block_type_code(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("```python\nprint('Hello World')\n```"), BlockType.CODE)

    def test_block_type_quote(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_block_type_unordered_list(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_block_type_ordered_list(self):
        from block import block_to_block_type, BlockType
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)