"""
This module provides tests for FolderFiles class
"""
import os
import sys

# Add the root folder for the system paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__ + "/../../")) + "/"
sys.path.append(ROOT_DIR)

from sources.Ocr import Ocr
# from tests.unit.test_file_converter import TestFileConverter

OUTPUT_DIR_PATH = os.path.abspath(ROOT_DIR + './tests/pdf2txt/output/pdf2image')

class TestOcr:
    def test_ocr_img2text():
        ## Arrange
        # Create the expected output directory
        EXPECTED_OUT_DIR_PATH = os.path.abspath(OUTPUT_DIR_PATH + '/test_pdf2image_with_output_dir')
        # Run the file conversion test before this
        # TestFileConverter.test_pdf2image_with_output_dir()
        
        ## Act
        text = Ocr.img2txt(os.path.abspath(EXPECTED_OUT_DIR_PATH + '/Page_1.jpg'))
        assert True