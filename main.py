from pathlib import Path
from PyPDF2 import PdfMerger

count = int(input("How many PDFs do you want to merge?\n").strip())

pdf_paths = []
for i in range(count):
    file_name = input(f"Enter the name/path of PDF {i + 1}: ").strip()
    if not file_name:
        continue
    path = Path(file_name)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_name}")
    pdf_paths.append(str(path))

if not pdf_paths:
    raise ValueError("No valid PDF files were provided for merging.")

merger = PdfMerger()
for pdf in pdf_paths:
    merger.append(pdf)

output_path = Path("merged-pdf.pdf")
with output_path.open("wb") as output_file:
    merger.write(output_file)

merger.close()
print(f"Merged PDF saved to: {output_path.resolve()}")
