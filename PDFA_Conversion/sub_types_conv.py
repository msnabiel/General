import streamlit as st
import subprocess
import os
from tempfile import NamedTemporaryFile

# Function to convert PDF to PDF/A
def convert_to_pdfa(uploaded_file, output_pdf, pdfa_standard):
    """
    Convert an uploaded PDF file to PDF/A using Ghostscript.
    
    Parameters:
    - uploaded_file: Streamlit uploaded file object.
    - output_pdf: Path to save the output PDF/A file.
    - pdfa_standard: PDF/A standard (e.g., '1a', '1b', '2a', '2b', '3b').
    
    Returns:
    - Tuple (success: bool, message: str)
    """
    # Save uploaded file to a temporary location
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input:
        temp_input.write(uploaded_file.read())

    input_pdf = temp_input.name
    
    # Define Ghostscript command
    gs_command = [
        'gs',
        '-dPDFA',
        '-dBATCH',
        '-dNOPAUSE',
        '-dNOOUTERSAVE',
        '-dUseCIEColor',
        '-sProcessColorModel=DeviceCMYK',
        '-sDEVICE=pdfwrite',
        '-sOutputFile=' + output_pdf,
        '-dPDFACompatibilityPolicy=' + pdfa_standard,
        input_pdf
    ]

    # Execute Ghostscript command
    try:
        subprocess.run(gs_command, check=True)
        return True, f"Converted {uploaded_file.name} to {output_pdf} with PDF/A-{pdfa_standard} standard."
    except subprocess.CalledProcessError as e:
        return False, f"Failed to convert {uploaded_file.name} to PDF/A-{pdfa_standard}: {e}"
    finally:
        os.remove(input_pdf)  # Clean up temporary file

# Streamlit UI
def main():
    st.title('PDF to PDF/A Converter')

    # File upload and standard selection
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
    if uploaded_file:
        st.write(f"File selected: {uploaded_file.name}")

        standards = ['1a', '1b', '2a', '2b', '3b']
        pdfa_standard = st.selectbox('Select PDF/A standard:', standards)

        if st.button('Convert'):
            # Convert and display result
            output_base = f"output_PDF-{pdfa_standard}"
            os.makedirs(output_base, exist_ok=True)
            output_pdf = os.path.join(output_base, uploaded_file.name)
            success, message = convert_to_pdfa(uploaded_file, output_pdf, pdfa_standard)
            if success:
                st.success(message)
                st.download_button(
                    label="Download PDF/A file",
                    data=output_pdf,
                    file_name=os.path.basename(output_pdf)
                )
            else:
                st.error(message)

if __name__ == "__main__":
    main()
