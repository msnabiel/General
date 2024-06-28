
import fitz  # PyMuPDF
import pdfkit
import streamlit as st
import subprocess
import os
import io

# Function to convert PDF to HTML and save HTML files
def convert_pdf_to_html(pdf_document, base_name):
    html_files = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        html = page.get_text("html")
        html_file = f"{base_name}_page_{page_num + 1}.html"
        html_files.append(html_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)
    return html_files

# Function to convert HTML to PDF
def convert_html_to_pdf(html_files, pdf_output):
    pdfkit.from_file(html_files, pdf_output)

# Function to convert PDF to PDF/A using pdfcpu
def convert_pdf_to_pdfa(pdf_input, pdfa_output):
    subprocess.run(["pdfcpu", "validate", "-mode", "pdfa", "-o", pdfa_output, pdf_input])

# Streamlit Interface
st.title("PDF to PDF/A Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("File uploaded successfully!")
    
    # Get base name without extension
    base_name = os.path.splitext(uploaded_file.name)[0]
    pdf_output = f"{base_name}.pdf"
    pdfa_output = f"{base_name}.pdf"
    
    # Step 1: Convert PDF to HTML
    pdf_document = fitz.open(uploaded_file.name)
    html_files = convert_pdf_to_html(pdf_document, base_name)
    pdf_document.close()
    
    # Step 2: Convert HTML to PDF
    convert_html_to_pdf(html_files, pdf_output)
    
    # Step 3: Convert PDF to PDF/A
    convert_pdf_to_pdfa(pdf_output, pdfa_output)
    
    # Clean up HTML files
    for html_file in html_files:
        os.remove(html_file)
    
    # Provide download link for PDF/A file
    with open(pdfa_output, "rb") as f:
        st.download_button(label="Download PDF/A", data=f, file_name=pdfa_output, mime="application/pdf")
    
    st.write(f"PDF/A file created: {pdfa_output}")
