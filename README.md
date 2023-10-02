# File Converter

This Python script provides a graphical user interface (GUI) for converting files between different formats. It utilizes the tkinter library for the GUI, and various external libraries for file conversion.

## Features

- **PDF to JPG**: Converts a PDF file to a series of JPG images, either as individual files or bundled in a ZIP archive.
- **Images to PDF**: Converts multiple image files (JPG, JPEG, PNG) into a single PDF file.
- **PDF to Word**: Converts a PDF document to a Word document (DOCX).

The script uses the following external libraries:

- `FPDF`: A Python class to generate PDF files.
- `os`: Provides a way to interact with the operating system, including functions for file operations.
- `zipfile`: Allows the creation and extraction of ZIP archives.
- `pdf2image`: Converts PDF pages to images.
- `pdf2docx`: Converts PDF documents to DOCX format.
- `fitz`: Part of PyMuPDF, used for handling PDF documents.

## Getting Started

### Prerequisites

- Python 3.x
- External libraries (`FPDF`, `pdf2image`, `pdf2docx`) can be installed using `pip`.

```bash
pip install fpdf pdf2image pdf2docx
```

### Running the Application

1. Run the `file_converter.py` script using Python.

```bash
python file_converter.py
```

2. The GUI window will appear with the following options:

   - **Convert PDF to JPG**: Allows you to convert PDF files to JPG images.

   - **Convert Images to PDF**: Enables you to convert multiple image files to a single PDF.

   - **Convert PDF to Word**: Converts a PDF document to a Word file.

   - Close the window when you're finished.

## How It Works

- The script utilizes tkinter for the GUI, enabling users to interact with the application through buttons.

- Various external libraries are used for file conversion operations, such as converting PDFs to images or Word documents.

- The selected files are processed based on the chosen conversion option, and success or error messages are displayed accordingly.

## Example Usage

1. Click "Convert PDF to JPG" to convert a PDF file to images.
2. Click "Convert Images to PDF" to convert images to a PDF file.
3. Click "Convert PDF to Word" to convert a PDF document to a Word file.

Success or error messages will be displayed based on the conversion process.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- FPDF: https://pyfpdf.readthedocs.io/en/latest/
- pdf2image: https://github.com/Belval/pdf2image
- pdf2docx: https://github.com/Alir3z4/python-pdf2docx
- PyMuPDF: https://github.com/pymupdf/PyMuPDF

---

Feel free to modify this readme file to suit your specific project details and preferences.
