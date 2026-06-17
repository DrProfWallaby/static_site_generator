import os
import shutil
import sys

from block_markdown import markdown_to_html_node

def main():
        basepath = "/"
        if sys.argv[1]:
            basepath = sys.argv[1]
        static = os.path.abspath("./static")
        public = os.path.abspath("./docs")
        template = os.path.abspath("./template.html")
        content = os.path.abspath("./content")
        if os.path.exists(public):
            shutil.rmtree(public)
        static_to_public(static, public)
        generate_pages_recursive(content, template, public, basepath)

def static_to_public(src: str, dst: str) -> None:
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        if os.path.isdir(os.path.join(src, item)):
            static_to_public(os.path.join(src, item), os.path.join(dst, item))
        else:
            shutil.copy(os.path.join(src, item), os.path.join(dst, item))

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Error: Expected <h1> missing.")

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    with_title = template.replace("{{ Title }}", title)
    page = with_title.replace("{{ Content }}", html)
    page_href = page.replace('href="/', f'href="{basepath}')
    page_final = page_href.replace('src="/', f'src="{basepath}')
    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(page)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for item in os.listdir(dir_path_content):
        if os.path.isdir(os.path.join(dir_path_content, item)):
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)
        else:
            root, ext = os.path.splitext(item)
            if ext == ".md":
                html_item = root + ".html"
            generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, html_item), basepath)

if __name__ == "__main__":
    main()