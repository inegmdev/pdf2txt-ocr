"""
This module provides a class for searching folders on the file system.
"""
import os

class FolderSearch:
    """
    A class for searching folders on the file system.

    Attributes:
        directory_path (str): The path to the directory to search.
    """
    def __init__(self, directory_path:str, logger=None):
        # Initialize the Logger if passed
        if logger:
            self.log = logger(self.__class__.__name__)

        # Initialize empty list to store file paths
        self.all_files = []

        self.log.info(f'Traversing through the directory {directory_path}') if logger is not None else None

        # Traverse all the files in the directory and save them in `all_files`
        for root, _directories, files in os.walk(directory_path):
            for filename in files:
                # Join the two strings to form the full filepath.
                filepath = os.path.join(root, filename)
                # Append the filepath to the list
                self.all_files.append(filepath)

    def get_file_list(self):
        """
        Returns a list of all file paths found in the directory.

        Returns:
            list: A list of file paths.
        """
        return self.all_files

