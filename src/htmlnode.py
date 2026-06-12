

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error: Not yet implemented.")
    
    def props_to_html(self) -> str:
        html_string = ""
        for attribute in self.props:
            html_string += f' {attribute}="{self.props[attribute]}"'
        return html_string
    
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
    def __eq__(self, other: HTMLNode) -> bool:
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )