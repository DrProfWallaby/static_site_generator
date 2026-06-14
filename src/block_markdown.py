from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip() != ""]

def block_to_block_type(block: str) -> BlockType:
    headers = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headers):
        return BlockType.HEADING
    elif block.startswith("```"):
        split_block = block.split("\n")
        if len(split_block) < 2:
            return BlockType.PARAGRAPH
        if split_block[0] == "```" and split_block[-1] == "```":
            return BlockType.CODE
        return BlockType.PARAGRAPH
    elif block.startswith(">") or block.startswith("> "):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith(">") or line.startswith("> "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        split_block = block.split("\n")
        for i in range(len(split_block)):
            if split_block[i].startswith(f"{i + 1}. "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH