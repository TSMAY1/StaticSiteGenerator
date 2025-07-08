from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid delimiter count in node text")

        if node.text_type != TextType.TEXT:
            new_list.append(node)
    
        elif node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                new_list.append(node)
                continue
            parts = node.text.split(delimiter)
            for i in range(0, len(parts)):
                if (i % 2 == 0) and parts[i] != "":
                    new_list.append(TextNode(parts[i], TextType.TEXT))
                elif (i % 2 != 0) and parts[i] != "":
                    new_list.append(TextNode(parts[i], text_type))
    return new_list

