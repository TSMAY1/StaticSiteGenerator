from .extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links
from .textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_list = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_list.append(node)

        else: 
            images = extract_markdown_images(node.text)

            if not images:
                new_list.append(node)
                
            else:
                current_text = node.text
                for image_alt, image_url in images:
                    sections = current_text.split(f"![{image_alt}]({image_url})", 1)
                    current_text = sections[1]
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(image_alt, TextType.IMAGE, image_url))
                if current_text != "":
                    new_list.append(TextNode(current_text, TextType.TEXT))
                
    return new_list


def split_nodes_link(old_nodes):
    new_list = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_list.append(node)

        else:
            links = extract_markdown_links(node.text)

            if not links:
                new_list.append(node)
                
            else:
                current_text = node.text
                for anchor_text, link_url in links:
                    sections = current_text.split(f"[{anchor_text}]({link_url})", 1)
                    current_text = sections[1]
                    if sections[0] != "":
                        new_list.append(TextNode(sections[0], TextType.TEXT))
                    new_list.append(TextNode(anchor_text, TextType.LINK, link_url))
                if current_text != "":
                    new_list.append(TextNode(current_text, TextType.TEXT))
                
    return new_list


