# pdf2txt-ocr
PDF to text files OCR-based Tool

## 🧱 Installation
```bash
make init
make activate # Will print the virtualenv activate command, call the command.
make install # Will print the pip install virtualenv libraries, call the command.
```
## 🏃‍♂️ Using the Script

### Convert One PDF

### Convert All PDFS in a Directory

## 🐞 Troubleshooting

### No such file or directory: 'pdfinfo'

#### Issue
#### Issue
```bash
(.venv) inegm ~/my/pdf2txt-ocr (main)
$ python pdf2txt.py 
Traceback (most recent call last):
  File "/home/inegm/my/pdf2txt-ocr/.venv/lib/python3.8/site-packages/pdf2image/pdf2image.py", line 568, in pdfinfo_from_path
    proc = Popen(command, env=env, stdout=PIPE, stderr=PIPE)
  File "/usr/lib/python3.8/subprocess.py", line 858, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib/python3.8/subprocess.py", line 1704, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'pdfinfo'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pdf2txt.py", line 46, in <module>
    pdf_to_images('./tests/pdf2txt/input_sample/sample.pdf', OUT_IMG_DIR)
  File "pdf2txt.py", line 11, in pdf_to_images
    pages = convert_from_path(pdf_path, dpi=100)
  File "/home/inegm/my/pdf2txt-ocr/.venv/lib/python3.8/site-packages/pdf2image/pdf2image.py", line 127, in convert_from_path
    page_count = pdfinfo_from_path(
  File "/home/inegm/my/pdf2txt-ocr/.venv/lib/python3.8/site-packages/pdf2image/pdf2image.py", line 594, in pdfinfo_from_path
    raise PDFInfoNotInstalledError(
pdf2image.exceptions.PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
(.venv) inegm ~/my/pdf2txt-ocr (main)
```
#### Solution

```bash
make init
```