from block_markdown import markdown_to_html_node

def main():
    md = """
```
this is a code block
that runs on two lines
```
"""

    node = markdown_to_html_node(md)
    print(node.to_html())

if __name__ == "__main__":
    main()