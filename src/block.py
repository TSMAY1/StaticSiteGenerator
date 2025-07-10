from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit():
        expected_number = 1
        for line in block.split("\n"):
            index = line.find(".")
            if index == -1:
                return BlockType.PARAGRAPH
            number = int(line[:index])
            if len(line) <= index + 1:
                return BlockType.PARAGRAPH
            if line[index] == "." and line[index + 1] == " ":
                if number != expected_number:
                    return BlockType.PARAGRAPH
                expected_number += 1
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
