import os
import shutil
from src.markdown_to_html_node import markdown_to_html_node
import sys

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def delete_docs_directory():
    print("Deleting existing docs directory.")
    
    if os.path.exists("docs"):
        shutil.rmtree("docs")
        print("Docs directory deleted successfully.")
    else:
        print("Docs directory does not exist.")

def create_docs_directory():
    print("Creating docs directory.")
    
    if not os.path.exists("docs"):
        os.mkdir("docs")
        print("Docs directory created successfully.")
    else:
        print("Docs directory already exists.")

def copy_static_to_docs(static):
    static_path = os.path.join("static", static)
    docs_path = os.path.join("docs", static)

    for file in os.listdir(static_path):
        full_file_path = os.path.join(static_path, file)
        
        if os.path.isfile(full_file_path):
            destination_path = os.path.join(docs_path, file)
            print(f"Copying {full_file_path} to {destination_path}")
            shutil.copy(full_file_path, destination_path)

        if os.path.isdir(full_file_path):
            destination_path = os.path.join(docs_path, file)
            if not os.path.exists(destination_path):
                print(f"Creating directory {destination_path}")
                os.mkdir(destination_path)

            copy_static_to_docs(file)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No title found in markdown content.")
    
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    markdown_content = open(from_path, 'r').read()
    template_content = open(template_path, 'r').read()

    root_html_node = markdown_to_html_node(markdown_content)
    html_content = root_html_node.to_html()

    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
        print(f"Created directory for {dest_path}.")
    with open(dest_path, 'w') as dest_file:
        print(f"Writing final HTML to {dest_path}.")
        dest_file.write(final_html)

def generate_pages_recursive(from_path, template_path, destination_html_path, basepath):
    
    for root, dirs, files in os.walk(from_path):
        for file in files:
            if file.endswith(".md"):
                full_file_path = os.path.join(root, file)
                destination_html_path = full_file_path.replace("content", "docs")
                destination_html_path = destination_html_path.replace(".md", ".html")
                generate_page(full_file_path, template_path, destination_html_path, basepath)

def main():
    print("Hello from static-site-generator!")
    delete_docs_directory()
    create_docs_directory()
    copy_static_to_docs(".")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()