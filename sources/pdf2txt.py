# import os
# import re
# from pdf2image import convert_from_path

# def save_txt_page(img_path, txt_path):
#   page_text = ocr_page(img_path)
#   with open(txt_path, 'w') as file:
#     file.write(page_text)

# OUT_IMG_DIR = './tests/pdf2txt/output/sample.pdf.out.images'
# OUT_TXT_DIR = './tests/pdf2txt/output/sample.pdf.out.text'

# os.makedirs(os.path.join(os.getcwd(),OUT_TXT_DIR), exist_ok=True)

# pdf_to_images('./tests/pdf2txt/input_sample/sample.pdf', OUT_IMG_DIR)
# pdf_output_all_files = os.listdir(OUT_IMG_DIR)
# pdf_output_images = list(filter(lambda file: (re.search(r"^[^\.]+\.jpg", file)), pdf_output_all_files)) 

# for page in pdf_output_images:
#   page_name, _ = os.path.splitext(os.path.basename(OUT_IMG_DIR + "/" + page))
#   print(f"{OUT_IMG_DIR}/{page}")
#   save_txt_page (f"{OUT_IMG_DIR}/{page}", f"{OUT_TXT_DIR}/{page_name}.txt")

import pdf2image
import pytesseract
import os
import argparse
from tqdm import tqdm

# Create an argument parser to get the directory path and output directory from the user
parser = argparse.ArgumentParser(description='Extract text from PDF files using OCR')
parser.add_argument('dir_path', type=str, help='Path to the directory containing PDF files')
parser.add_argument('output_dir', type=str, help='Path to the output directory')

# Parse the arguments
args = parser.parse_args()

# Get the directory path and output directory from the user
dir_path = args.dir_path
output_dir = args.output_dir

# Check if the directory exists
if not os.path.exists(dir_path):
  raise Exception(f'Directory ({dir_path}) not found.')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the PDF files in the directory
for file_name in os.listdir(dir_path):
    # Check if the file is a PDF file
    if file_name.endswith(".pdf"):
        # Get the path to the PDF file
        pdf_path = os.path.join(dir_path, file_name)
        
        # Convert the PDF to images
        images = pdf2image.convert_from_path(pdf_path, dpi=100)
        print(f'PDF ({file_name}) contains ({len(images)}) pages.')
        
        # Create a directory with the name of the PDF file to store the output text files
        pdf_output_dir = os.path.join(output_dir, os.path.splitext(file_name)[0])
        os.makedirs(pdf_output_dir, exist_ok=True)
        
        # Iterate over the images
        for i, image in enumerate(tqdm(images, desc=f"Processing {file_name}")):
            # OCR the image and save the text to a file
            text = pytesseract.image_to_string(image)
            with open(f"{pdf_output_dir}/Page_{i}.txt", "w") as f:
                f.write(text)

print("OCR completed successfully.")

