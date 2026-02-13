
# views.py
#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import pdfplumber
import pandas as pd
from django.core.files.storage import FileSystemStorage

def upload_pdf(request):
    if request.method == "POST" and request.FILES.get("pdf_file"):
        pdf_file = request.FILES["pdf_file"]

        # Save uploaded file temporarily
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        file_path = fs.path(filename)

        # Extract tables from PDF
        pdf = pdfplumber.open(file_path)
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

        # Write to Excel
        output_file = "converted.xlsx"
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            for i, df in enumerate(all_tables):
                df.to_excel(writer, sheet_name=f"Page_{i+1}", index=False)

        # Return file as response
        with open(output_file, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = f'attachment; filename="{output_file}"'
            return response

    # If GET request → show upload form
    return render(request, "converter_app/upload.html")
