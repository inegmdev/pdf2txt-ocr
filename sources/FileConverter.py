import os # For saving the images
import pdf2image as pdf2img # For converting PDF to image
from tqdm import tqdm # For progress bar
# import click # Raise the exception

class FileConverter:
    """Converts the PDF to Image"""
    @staticmethod
    def pdf2image(pdf_path, output_dir="", page_prefix = "Page_"):
        """
        Convert a PDF file to a series of JPEG images.

        Args:
            pdf_path (str): The path to the PDF file.
            output_dir (str): The directory where the JPEG images will be saved.

        Returns:
            None
        """
        # If output dir is not create a directory with the same file name
        if output_dir == "":
            output_dir = os.path.splitext(pdf_path)[0]
        # Sanity checks
        if not os.path.exists(output_dir): 
            # Create teh directory 
            os.makedirs(output_dir, exist_ok=True)
        else:
            if not os.path.isdir(output_dir):
                raise Exception(f'Output path ({output_dir}) exists and is not a directory.')
        if not os.path.exists(pdf_path):
            raise Exception(f'PDF file ({pdf_path}) does not exist.')

        # Converting all the pages to images
        pages = pdf2img.convert_from_path(pdf_path, dpi=100)
        # Save the images
        i = 1
        FILE_NAME = os.path.basename(pdf_path)
        for page in tqdm(pages, ascii=True, desc=FILE_NAME):
            # Create the dirs if not exists
            image_path = os.path.join(output_dir, page_prefix + str(i) + ".jpg")
            image_abspath = os.path.abspath(image_path)
            # Save the images in JPEG format
            page.save(image_abspath, "JPEG")
            i = i+1
            pass
