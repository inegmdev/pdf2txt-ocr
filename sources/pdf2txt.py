import pdf2image
import pytesseract
import os
import click
from tqdm import tqdm

@click.command()
@click.option('-i', '--input-dir', 'dir_path', type=click.Path(exists=True), required=True, help='Input directory containing PDF files')
@click.option('-o', '--output-dir', type=click.Path(), required=True, help='Output directory to store text files')
@click.option('-d', '--dpi', type=int, default=100, show_default=True, help='DPI level for converting PDF to images')
def extract_text(dir_path, output_dir, dpi):
    # Count the number of PDF files in the input directory
    num_files = sum([len(files) for r, d, files in os.walk(dir_path) if any(file.endswith('.pdf') for file in files)])

    # Initialize the progress bar for all files
    all_files_pbar = tqdm(total=num_files, unit='file', leave=False)

    # Iterate over the directories and subdirectories in the directory
    for root, dirs, files in os.walk(dir_path):
        # Iterate over the PDF files in the directory
        for i, file_name in enumerate(files, start=1):
            # Check if the file is a PDF file
            if file_name.endswith(".pdf"):
                # Get the path to the PDF file
                pdf_path = os.path.join(root, file_name)

                # Convert the PDF to images with the specified DPI level
                images = pdf2image.convert_from_path(pdf_path, dpi=dpi)

                # Create a directory with the name of the PDF file to store the output text files
                pdf_output_dir = os.path.join(output_dir, os.path.splitext(file_name)[0])
                os.makedirs(pdf_output_dir, exist_ok=True)

                # Display the number of pages in the PDF file
                print(f"PDF {file_name} contains {len(images)} pages.")

                # Initialize the progress bar for the current file
                file_pbar = tqdm(total=len(images), unit='page')

                # Iterate over the images
                for j, image in enumerate(images):
                    # OCR the image and save the text to a file
                    text = pytesseract.image_to_string(image)
                    with open(f"{pdf_output_dir}/Page_{j+1}.txt", "w") as f:
                        f.write(text)

                    # Update the progress bar for the current file
                    file_pbar.update(1)

                # Close the progress bar for the current file
                file_pbar.close()

                # Remove the statement about the number of pages in the PDF file
                print("\033[F\033[K", end="")

                # Update the progress bar for all files
                all_files_pbar.update(1)

    # Close the progress bar for all files
    all_files_pbar.close()

    print("pdf2txt completed successfully.")
    print(f"Input PDF directory   ({dir_path}).")
    print(f"Text output directory ({output_dir}).")

if __name__ == '__main__':
    extract_text()