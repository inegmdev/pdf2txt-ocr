"""
This module provides tests for FolderSearch class
"""

import sys
import os

# Add the root folder for the system paths
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from sources.find import FolderSearch
from sources.helpers.Logger import Logger

class TestFolderSearch:
    """
    This class provides unit tests for the FolderSearch utility.
    """
    def test_list_all_files(self):
        """
        Test the list_all_files method of the FolderSearch utility.
        """
        folder_seach = FolderSearch(os.path.dirname(os.path.abspath(__file__ + '/../pdf2txt/inputs')), logger=Logger)
        print(folder_seach.get_file_list())
        assert True