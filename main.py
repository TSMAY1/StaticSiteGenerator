import os
import shutil

def main():
    print("Hello from static-site-generator!")


if __name__ == "__main__":
    main()

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

    