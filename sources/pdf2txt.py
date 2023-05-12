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
import click
from tqdm import tqdm

@click.command()
@click.option('-i', '--input-dir', 'dir_path', type=click.Path(exists=True), required=True, help='Input directory containing PDF files')
@click.option('-o', '--output-dir', type=click.Path(), required=True, help='Output directory to store text files')
def extract_text(dir_path, output_dir):
    # Initialize the progress bar
    pbar = tqdm(total=sum([len(files) for r, d, files in os.walk(dir_path)]), unit='file')

    # Iterate over the directories and subdirectories in the directory
    for root, dirs, files in os.walk(dir_path):
        # Iterate over the PDF files in the directory
        for i, file_name in enumerate(files, start=1):
            # Check if the file is a PDF file
            if file_name.endswith(".pdf"):
                # Get the path to the PDF file
                pdf_path = os.path.join(root, file_name)

                # Convert the PDF to images
                images = pdf2image.convert_from_path(pdf_path, dpi=100)
                print(f'PDF ({file_name}) contains ({len(images)}) pages.')

                # Create a directory with the name of the PDF file to store the output text files
                pdf_output_dir = os.path.join(output_dir, os.path.splitext(file_name)[0])
                os.makedirs(pdf_output_dir, exist_ok=True)

                # Iterate over the images
                for j, image in enumerate(images):
                    # OCR the image and save the text to a file
                    text = pytesseract.image_to_string(image)
                    with open(f"{pdf_output_dir}/Page_{j+1}.txt", "w") as f:
                        f.write(text)

                # Update the progress bar
                pbar.update(1)

    # Close the progress bar
    pbar.close()

    print("OCR completed successfully.")

if __name__ == '__main__':
    extract_text()