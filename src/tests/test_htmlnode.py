import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test__repr__(self):
        node = HTMLNode(tag="div", value="This is a div", children=None, props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=This is a div, children=None, props={'class': 'container'})")

    def test_props_to_html(self):
        node = HTMLNode(tag="span", value="This is a span", props={"style": "color: red;"})
        self.assertEqual(node.props_to_html(), 'style="color: red;"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is a paragraph", props={"id": "para1"})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph, children=None, props={'id': 'para1'})")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag="strong", value="This is bold text", props={"class": "bold"})
        self.assertEqual(node.to_html(), '<strong class="bold">This is bold text</strong>')

    def test_to_html_with_props(self):
        node = LeafNode(tag="a", value="This is a link", props={"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">This is a link</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.to_html(), '<div><span>Child 1</span><span>Child 2</span></div>')

    def test_to_html_with_props(self):
        child = LeafNode(tag="p", value="This is a paragraph")
        parent = ParentNode(tag="section", children=[child], props={"class": "section-class"})
        self.assertEqual(parent.to_html(), '<section class="section-class"><p>This is a paragraph</p></section>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )