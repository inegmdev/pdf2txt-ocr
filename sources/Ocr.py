import os # Needed for checking file existence
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

class Ocr:
    @staticmethod
    def img2txt(img_path):
        """
        Takes in img_path returns text extracted from this page.
        """
        # Sanity checks
        if (not os.path.exists(img_path)):
            raise Exception(f'Image file ({img_path}) does not exist.')
        
        if (os.path.isdir(img_path)):
            raise Exception(f'Image file ({img_path}) is not a file.')
        
        # load the original image
        img = cv2.imread(img_path)
        # convert the image to black and white for better OCR
        ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
        # pytesseract image to string to get results
        text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
        return text
