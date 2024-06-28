# PDF to PDF/A Converter

This repository contains a Streamlit application for converting PDF files to various PDF/A standards (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-3b) using Ghostscript.

## Table of Contents
- [PDF to PDF/A Converter](#pdf-to-pdfa-converter)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux/Ubuntu](#linuxubuntu)
  - [Usage](#usage)
  - [Notes](#notes)
  - [Troubleshooting](#troubleshooting)
  - [Contributors](#contributors)
  - [License](#license)

## Overview

The application provides a user-friendly interface to upload a PDF file, select the desired PDF/A compliance level, and convert the file using Ghostscript. It ensures long-term archiving and accessibility of PDF documents.

## Requirements

- Python 3.x
- Streamlit
- Ghostscript (Ensure Ghostscript is installed and the `gs` command is available in your system's PATH)

## Installation

### Windows

1. **Clone the repository**:

   ```bash
   git clone https://github.com/msnabiel/General.git
   cd General/PDFA_Conversion
   ```

2. **Install Python**:
   - Download and install Python from [python.org](https://www.python.org/downloads/windows/).
   - Ensure `python` and `pip` are added to your PATH.

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ghostscript**:
   - Download the installer from [Ghostscript](https://www.ghostscript.com/download/gsdnld.html) and follow the installation instructions.
   - Ensure the `gs` command is added to your PATH.

### macOS

1. **Clone the repository**:

   ```bash
   git clone https://github.com/msnabiel/General.git
   cd General/PDFA_Conversion
   ```

2. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Python**:
   ```bash
   brew install python
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Ghostscript**:
   ```bash
   brew install ghostscript
   ```

### Linux/Ubuntu

1. **Clone the repository**:

   ```bash
   git clone https://github.com/msnabiel/General.git
   cd General/PDFA_Conversion
   ```

2. **Update package lists**:

   ```bash
   sudo apt-get update
   ```

3. **Install Python and pip**:

   ```bash
   sudo apt-get install python3 python3-pip
   ```

4. **Install dependencies**:

   ```bash
   pip3 install -r requirements.txt
   ```

5. **Install Ghostscript**:

   ```bash
   sudo apt-get install ghostscript
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run PDFA_SUB_TYPES.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Follow these steps in the application:

   - **Upload a PDF**: Use the file uploader to select a PDF file.
   - **Select PDF/A Level**: Choose the desired PDF/A compliance level from the dropdown menu.
   - **Convert**: Click the "Convert" button to start the conversion process.
   - **Download**: Once the conversion is complete, a download button will appear for you to save the converted PDF/A file.

## Notes

- The uploaded PDF file is temporarily saved for the conversion process and is deleted afterward to maintain system cleanliness.
- The output file will have a name based on the input file name and the chosen PDF/A compliance level.

## Troubleshooting

- **Conversion Issues**: Ensure that Ghostscript is correctly installed and that the `gs` command works from your command line.
- **File Permissions**: Make sure you have the necessary permissions to read, write, and delete files in the directory you are working in.
- **Debugging**: For detailed error messages, you can add debug output in `pdfa_converter.py` using print statements or Streamlit's `st.write()` function.

## Contributors

- [Syed Nabiel Hasaan M.](https://github.com/msnabiel)
- Contact - [msyednabiel@gmail.com](mailto:msyednabiel@gmail.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
