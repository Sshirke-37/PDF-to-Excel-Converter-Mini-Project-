# PDF-to-Excel-Converter-Mini-Project-
PDF to Excel Converter (Django + Bootstrap) A web application built with Django that allows users to upload PDF files and convert them into Excel spreadsheets. Designed with a clean, Bootstrap‑styled interface, the app provides real‑time feedback during conversion and ensures a beginner‑friendly, modular structure.

Features
- Upload PDF files via a simple, responsive web form.
- Extracts tables from PDFs using pdfplumber.
- Converts extracted data into Excel format with pandas + openpyxl.
- Real‑time feedback with status messages and a spinner while conversion is in progress.
- Clean, card‑based UI styled with Bootstrap and custom CSS.
- Error handling for:
- Password‑protected PDFs
- PDFs without tables
- Invalid file uploads

Tech Stack
- Backend: Django (Python)
- Libraries: pdfplumber, pandas, openpyxl
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Storage: Django FileSystemStorage for handling uploads

