import os
import shutil


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

def main():
    print("Hello from static-site-generator!")
    delete_public_directory()
    create_public_directory()
    copy_static_to_public("")



if __name__ == "__main__":
    main()