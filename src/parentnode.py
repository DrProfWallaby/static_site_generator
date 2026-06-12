from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Error: ParentNode has no tag.")
        if not self.children:
            raise ValueError("Error: ParentNode is not a parent.")
        