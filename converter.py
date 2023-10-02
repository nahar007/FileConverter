import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from fpdf import FPDF  # Import FPDF
import os
import zipfile
from pdf2image import convert_from_path
from pdf2docx import Converter
import fitz

def pdf_to_images(pdf_file, output_folder):
    pages = convert_from_path(pdf_file)
    image_paths = []
    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        page.save(image_path, "JPEG")
        image_paths.append(image_path)
    return image_paths

def create_zip(pdf_file, output_folder):
    images = pdf_to_images(pdf_file, output_folder)
    with zipfile.ZipFile(os.path.join(output_folder, 'output.zip'), 'w') as zipf:
        for image in images:
            zipf.write(image)

    messagebox.showinfo("Success", "PDF pages converted to images and saved in output.zip!")

def pdf_to_jpg():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            # Check if PDF has only one page
            pages = convert_from_path(pdf_file)
            if len(pages) == 1:
                # If only one page, convert to JPG directly
                image_path = os.path.join(output_folder, os.path.basename(pdf_file).replace(".pdf", ".jpg"))
                pages[0].save(image_path, "JPEG")
                messagebox.showinfo("Success", "PDF converted to JPG!")
            else:
                # If multiple pages, create a ZIP file
                create_zip(pdf_file, output_folder)

def images_to_pdf():
    image_files = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if image_files:
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_file:
            pdf = FPDF()  # Initialize FPDF
            for image_file in image_files:
                pdf.add_page()
                pdf.image(image_file, x=10, y=10, w=190)
            
            pdf.output(pdf_file)
            messagebox.showinfo("Success", "Images converted to PDF!")

def pdf_to_word():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        output_word_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
        if output_word_file:
            try:
                cv = Converter(pdf_file)
                cv.convert(output_word_file, start=0, end=None)
                cv.close()
                messagebox.showinfo("Success", "PDF converted to Word!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("File Converter Developed By NaharInfocom")
root.geometry("400x300")  # Set window size to 400x300 pixels

# PDF to JPG button
pdf_to_jpg_button = tk.Button(root, text="Convert PDF to JPG", command=pdf_to_jpg)
pdf_to_jpg_button.pack()

# Images to PDF button
images_to_pdf_button = tk.Button(root, text="Convert Images to PDF", command=images_to_pdf)
images_to_pdf_button.pack()

# PDF to Word button
pdf_to_word_button = tk.Button(root, text="Convert PDF to Word", command=pdf_to_word)
pdf_to_word_button.pack()

# Run the main loop
root.mainloop()
