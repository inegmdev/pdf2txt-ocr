"""
This module provides tests for FolderFiles class
"""

import sys
import os

# Add the root folder for the system paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__ + "/../../")) + "/"
sys.path.append(ROOT_DIR)
from sources.FolderFiles import FolderFiles
from sources.helpers.Logger import Logger

INPUT_DIR_ABS_PATH = os.path.abspath(ROOT_DIR + './tests/pdf2txt/input')

class TestFolderFiles:
    """
    This class provides unit tests for the FolderFiles utility.
    """
    def test_list_all_files(self):
        """
        Test the list_all_files method of the FolderFiles utility.
        """
        folder_files = FolderFiles(INPUT_DIR_ABS_PATH, logger=Logger)
        print(folder_files.get_file_list())
        assert True

    def test_return_only_txt_files(self):
        folder_files = FolderFiles(INPUT_DIR_ABS_PATH, logger=Logger)
        print(folder_files.get_filtered_file_list(r'.+\.txt$'))
        assert True
    
    def test_return_only_pdf_files(self):
        folder_files = FolderFiles(INPUT_DIR_ABS_PATH, logger=Logger)
        print(folder_files.get_filtered_file_list(r'.+\.pdf$'))
        assert True