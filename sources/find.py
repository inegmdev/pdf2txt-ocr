import os



for root, dirs, files in os.walk("path/to/folder"):
    for file in files:
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(root, file))

for pdf_file in pdf_files:
    print(pdf_file)


class FolderSearch:
    def __init__(self, directory_path:str):
        # Initialize empty list to store file paths
        self.all_files = []

        # Traverse all the files in the directory and save them in `all_files`
        for root, _directories, files in os.walk(directory_path):
            for filename in files:
                # Join the two strings to form the full filepath.
                filepath = os.path.join(root, filename)
                # Append the filepath to the list
                self.all_files.append(filepath)

    def get_file_list(self):
        return self.all_files
            
    # def list_all_files_by_extension(extension: str):
        
