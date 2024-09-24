import pdfplumber

def extract_pdf_data(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):
                
                text = page.extract_text()
                print(f"--- Page {page_number} ---")
                print(text)
                print("\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    extract_pdf_data(pdf_path)
