"""
This module provides a class for searching folders on the file system.
"""
import os
import re

class FolderFiles:
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
                # Logging
                self.log.info(f"Added path ({filepath}) to the list.") if logger is not None else None

    def get_file_list(self):
        """
        Returns a list of all file paths found in the directory.
        """
        return self.all_files
    
    def get_filtered_file_list(self, pattern: str):
        """
        Filters a list of file paths based on a regular expression pattern.

        Args:
            pattern (str): A regular expression pattern to match against the file paths.

        Returns:
            list: A filtered list of file paths that match the pattern.
        """
        # Compile the regular expression pattern
        regex = re.compile(pattern, flags=re.IGNORECASE | re.MULTILINE)
        
        # Filter the list of file paths based on the pattern
        filtered_paths = [path for path in self.all_files if regex.match(path)]
        return filtered_paths

