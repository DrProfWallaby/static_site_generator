from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str]=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Error: Leaf Node missing required value")
        if not self.tag:
            return self.value
        if self.props:
            return f'<{self.tag}{self.props}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def __eq__(self, other: HTMLNode) -> bool:
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )