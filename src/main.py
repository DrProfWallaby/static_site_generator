from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    test = HTMLNode(props={"href": "https://www.google.com"})
    print(test.props_to_html())

if __name__ == "__main__":
    main()