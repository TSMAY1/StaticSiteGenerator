from .textnode import TextNode, TextType, text_node_to_html_node

from .block import BlockType, block_to_block_type
from .split_nodes_delimiter import split_nodes_delimiter
from .text_to_textnodes import text_to_textnodes
from .markdown_to_blocks import markdown_to_blocks
from .htmlnode import HTMLNode, ParentNode, LeafNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    new_list = []
    for node in text_nodes:
        new_node = text_node_to_html_node(node)
        new_list.append(new_node)
    return new_list


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes_list = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            new_node = ParentNode(tag="p", children=text_to_children(block), props=None)
            html_nodes_list.append(new_node)
        if block_type == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char == "#":
                    hash_count += 1
                else:
                    break
            heading_text = block.lstrip("# ")
            new_node = ParentNode(tag="h" + str(hash_count), children=text_to_children(heading_text), props=None)
            html_nodes_list.append(new_node)

        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            line_list = []
            for line in lines:
                if line.startswith("- "):
                    line_text = line.lstrip("- ")
                else:
                    line_text = line.lstrip("* ")
                line_node = ParentNode(tag="li", children=text_to_children(line_text), props=None)
                line_list.append(line_node)
            new_node = ParentNode(tag="ul", children=line_list, props=None)
            html_nodes_list.append(new_node)

        if block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            line_list = []
            for line in lines:
                line_text = line.lstrip("1234567890" + ". ")
                line_node = ParentNode(tag="li", children=text_to_children(line_text), props=None)
                line_list.append(line_node)
            new_node = ParentNode(tag="ol", children=line_list, props=None)
            html_nodes_list.append(new_node)

        if block_type == BlockType.QUOTE:
            quote_text = block.strip("> ")
            new_node = ParentNode(tag="blockquote", children=text_to_children(quote_text), props=None)
            html_nodes_list.append(new_node)

        if block_type == BlockType.CODE:
            code_text = block.strip("`")
            code_text = code_text.lstrip("\n")
            text_node = TextNode(code_text, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            new_node = ParentNode(tag="pre", children=[html_node], props=None)
            html_nodes_list.append(new_node)

    div_node = ParentNode(tag="div", children=html_nodes_list, props=None)

    return div_node
