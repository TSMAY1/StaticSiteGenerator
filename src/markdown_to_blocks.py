
def markdown_to_blocks(markdown):
    blocks_list = []
    blocks = markdown.split('\n\n')

    for block in blocks:
        block = block.strip()

        if block != "":
            blocks_list.append(block)

    return blocks_list