import os
import shutil
from markdown_to_html_node import markdown_to_html_node


def delete_public_directory():
    print("Deleting existing public directory.")
    
    if os.path.exists("public"):
        shutil.rmtree("public")
        print("Public directory deleted successfully.")
    else:
        print("Public directory does not exist.")

def create_public_directory():
    print("Creating public directory.")
    
    if not os.path.exists("public"):
        os.mkdir("public")
        print("Public directory created successfully.")
    else:
        print("Public directory already exists.")

def copy_static_to_public(static):
    static_path = os.path.join("static", static)
    public_path = os.path.join("public", static)

    for file in os.listdir(static_path):
        full_file_path = os.path.join(static_path, file)
        
        if os.path.isfile(full_file_path):
            destination_path = os.path.join(public_path, file)
            print(f"Copying {full_file_path} to {destination_path}")
            shutil.copy(full_file_path, destination_path)

        if os.path.isdir(full_file_path):
            destination_path = os.path.join(public_path, file)
            if not os.path.exists(destination_path):
                print(f"Creating directory {destination_path}")
                os.mkdir(destination_path)

            copy_static_to_public(file)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No title found in markdown content.")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    markdown_content = open(from_path, 'r').read()
    template_content = open(template_path, 'r').read()

    root_html_node = markdown_to_html_node(markdown_content)
    html_content = root_html_node.to_html()

    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    for root, dirs, files in os.walk(from_path):
        for file in files:
            ## WORK ON RECURSION TO MAKE IT GENERATE HTML FOR ALL PAGES

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
        print(f"Created directory for {dest_path}.")
    with open(dest_path, 'w') as dest_file:
        print(f"Writing final HTML to {dest_path}.")
        dest_file.write(final_html)
    

def main():
    print("Hello from static-site-generator!")
    delete_public_directory()
    create_public_directory()
    copy_static_to_public("")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()