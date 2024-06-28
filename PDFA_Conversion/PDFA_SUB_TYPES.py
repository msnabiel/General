import subprocess
import streamlit as st

def convert_pdf_to_pdfa(input_file, output_file, pdfa_level):
  """Converts a PDF to a specified PDF/A level using Ghostscript."""
  pdfa_options = {
      "1a": "-dPDFA=1 -dPDFACompatibilityPolicy=1",
      "1b": "-dPDFA=1",
      "2a": "-dPDFA=2 -dPDFACompatibilityPolicy=1",
      "2b": "-dPDFA=2",
      "3b": "-dPDFA=3"
  }
  command = f"gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sProcessColorModel=DeviceRGB {pdfa_options[pdfa_level]} -sOutputFile={output_file} {input_file}"
  subprocess.run(command.split())

st.title("PDF to PDF/A Converter")

uploaded_file = st.file_uploader("Choose a PDF file to convert:")

if uploaded_file is not None:
  # Save uploaded file with a random name to avoid conflicts
  import tempfile
  with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
    temp_file.write(uploaded_file.read())
    input_file = temp_file.name

  # Select PDF/A level
  pdfa_level = st.selectbox("Select PDF/A level:", ("1a", "1b", "2a", "2b", "3b"))

  # Generate output filename based on input filename and PDF/A level
  output_file = f"{input_file[:-4]}-PDFA-{pdfa_level}.pdf"

  if st.button("Convert"):
    try:
      convert_pdf_to_pdfa(input_file, output_file, pdfa_level)
      st.success("PDF converted successfully! Download the converted file:")
      st.download_button("Download", data=open(output_file, "rb").read(), file_name=output_file)
    except Exception as e:
      st.error(f"An error occurred: {e}")
    finally:
      # Clean up temporary file
      import os
      os.remove(input_file)


