# main.py
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()

    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    merger.write(output)
    merger.close()
    print(f"\n✅ Merged PDF saved as: {output}")

def main():
    print("📑 PDF Merger")

    pdfs = []
    while True:
        path = input("Enter PDF path (or 'done' to finish): ").strip()
        if path.lower() == "done":
            break
        pdfs.append(path)

    if not pdfs:
        print("No PDFs provided.")
        return

    output = input("Enter output PDF filename (e.g., merged.pdf): ").strip()
    merge_pdfs(pdfs, output)

if __name__ == "__main__":
    main()
