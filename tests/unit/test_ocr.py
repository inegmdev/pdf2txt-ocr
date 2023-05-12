"""
This module provides tests for FolderFiles class
"""
import os
import sys

# Add the root folder for the system paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__ + "/../../")) + "/"
sys.path.append(ROOT_DIR)

from sources.Ocr import Ocr

OUTPUT_DIR_PATH = os.path.abspath(ROOT_DIR + './tests/pdf2txt/output/pdf2image')

class TestOcr:
    def test_ocr_img2text(self):
        ## Arrange
        # Create the expected output directory
        EXPECTED_OUT_DIR_PATH = os.path.abspath(OUTPUT_DIR_PATH + '/test_pdf2image_with_output_dir')
        
        ## Act
        text = Ocr.img2txt(os.path.abspath(EXPECTED_OUT_DIR_PATH + '/Page_1.jpg'))
        expected_text = 'This is a small demonstration .padf file -\n\njust for use in the Virtual Mechanics tutorials. More text. And more\n\ntext. And more text, And more text, And more text.\n\nAnd more text, And more text, And more text, And more text, And mare\ntext, And more text, Boring, 22222. And mare text. And more text. And\nmore text, And more text. And more text. And more text. And more text.\nAnd more text, And more text,\n\nAnd more text, And more text, And more text, And more text, And mare\ntext. And more text. And more text, Even more, Continued on page 2\n\x0c'
        assert text == expected_text