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

class TestFolderFiles:
    """
    This class provides unit tests for the FolderFiles utility.
    """
    def test_list_all_files(self):
        """
        Test the list_all_files method of the FolderFiles utility.
        """
        folder_seach = FolderFiles(os.path.dirname(os.path.abspath(ROOT_DIR + './tests/pdf2txt/input' )), logger=Logger)
        print(folder_seach.get_file_list())
        assert True