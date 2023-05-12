"""
This module provides tests for FolderFiles class
"""
import os
import sys
import shutil # For force removing non-empty directories

# Add the root folder for the system paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__ + "/../../")) + "/"
sys.path.append(ROOT_DIR)

from sources.FileConverter import FileConverter

PDF_FILE_ABS_PATH = os.path.abspath(ROOT_DIR + './tests/pdf2txt/input/sample_01.pdf')
OUTPUT_DIR_PATH = os.path.abspath(ROOT_DIR + './tests/pdf2txt/output/pdf2image')

class TestFileConverter:
    def test_pdf2image_without_output_dir(self):
        ## Arrange
        # Create the expected output directory
        EXPECTED_OUT_DIR_PATH = os.path.splitext(PDF_FILE_ABS_PATH)[0]
        # Delete the output directory if already created by a previous call for this test
        if (os.path.exists(EXPECTED_OUT_DIR_PATH)):
            shutil.rmtree(EXPECTED_OUT_DIR_PATH)
        
        ## Act
        # Convert PDF file to images
        pdf_path = FileConverter.pdf2image(PDF_FILE_ABS_PATH, output_dir="")
        
        ## Assert
        # Check if the folder is created on the name of the PDF file as the output dir is not provided
        assert os.path.exists(EXPECTED_OUT_DIR_PATH) == True
        # Check that the created file inside
    
    def test_pdf2image_with_output_dir(self):
        ## Arrange
        # Create the expected output directory
        EXPECTED_OUT_DIR_PATH = os.path.abspath(OUTPUT_DIR_PATH + '/test_pdf2image_with_output_dir')
        # Delete the output directory if already created by a previous call for this test
        if (os.path.exists(EXPECTED_OUT_DIR_PATH)):
            shutil.rmtree(EXPECTED_OUT_DIR_PATH)
        
        ## Act
        # Convert PDF file to images
        pdf_path = FileConverter.pdf2image(PDF_FILE_ABS_PATH, output_dir=EXPECTED_OUT_DIR_PATH)
        
        ## Assert
        # Check if the folder is created on the name of the PDF file as the output dir is not provided
        assert os.path.exists(EXPECTED_OUT_DIR_PATH) == True
        # Check that the created file inside