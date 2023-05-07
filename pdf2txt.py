import os
import re
from pdf2image import convert_from_path
import pytesseract
import matplotlib.pyplot as plt
import cv2

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def pdf_to_images(pdf_path, output_dir):
  # Converting all the pages to images
  pages = convert_from_path(pdf_path, dpi=100)
  # Save the images
  i = 1
  for page in pages:
    output_dir = os.path.join(os.getcwd(), output_dir)
    # Create the dirs if not exists
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, "Page_" + str(i) + ".jpg")
    image_abspath = os.path.abspath(image_path)
    # Save the images in JPEG format
    page.save(image_abspath, "JPEG")
    i = i+1

def ocr_page(img_path):
  """
  Takes in img_path returns text extracted from this page.
  """
  # load the original image
  img = cv2.imread(img_path)
  # convert the image to black and white for better OCR
  ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
  # pytesseract image to string to get results
  text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
  return text

def save_txt_page(img_path, txt_path):
  page_text = ocr_page(img_path)
  with open(txt_path, 'w') as file:
    file.write(page_text)

OUT_IMG_DIR = './sample.pdf.out.images'
OUT_TXT_DIR = './sample.pdf.out.text'

os.makedirs(os.path.join(os.getcwd(),OUT_TXT_DIR), exist_ok=True)

pdf_to_images('sample.pdf', OUT_IMG_DIR)
pdf_output_all_files = os.listdir(OUT_IMG_DIR)
pdf_output_images = list(filter(lambda file: (re.search(r"^[^\.]+\.jpg", file)), pdf_output_all_files)) 

for page in pdf_output_images:
  page_name, _ = os.path.splitext(os.path.basename(OUT_IMG_DIR + "/" + page))
  print(f"{OUT_IMG_DIR}/{page}")
  save_txt_page (f"{OUT_IMG_DIR}/{page}", f"{OUT_TXT_DIR}/{page_name}.txt")
