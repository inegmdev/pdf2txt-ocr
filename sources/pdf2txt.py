import os
import re
from pdf2image import convert_from_path


def save_txt_page(img_path, txt_path):
  page_text = ocr_page(img_path)
  with open(txt_path, 'w') as file:
    file.write(page_text)

OUT_IMG_DIR = './tests/pdf2txt/output/sample.pdf.out.images'
OUT_TXT_DIR = './tests/pdf2txt/output/sample.pdf.out.text'

os.makedirs(os.path.join(os.getcwd(),OUT_TXT_DIR), exist_ok=True)

pdf_to_images('./tests/pdf2txt/input_sample/sample.pdf', OUT_IMG_DIR)
pdf_output_all_files = os.listdir(OUT_IMG_DIR)
pdf_output_images = list(filter(lambda file: (re.search(r"^[^\.]+\.jpg", file)), pdf_output_all_files)) 

for page in pdf_output_images:
  page_name, _ = os.path.splitext(os.path.basename(OUT_IMG_DIR + "/" + page))
  print(f"{OUT_IMG_DIR}/{page}")
  save_txt_page (f"{OUT_IMG_DIR}/{page}", f"{OUT_TXT_DIR}/{page_name}.txt")
