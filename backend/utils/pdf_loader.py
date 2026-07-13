from pathlib import Path
import fitz  # PyMuPDF


class DocumentLoader:

    def __init__(self, docs_folder="docs"):

        self.docs_folder = Path(docs_folder)

    def load_documents(self):

        documents = []

        # Load PDF files
        for pdf_file in self.docs_folder.glob("*.pdf"):

            print(f"Loading PDF: {pdf_file.name}")

            document = fitz.open(pdf_file)

            text = ""

            for page in document:

                text += page.get_text()

            documents.append({
                "filename": pdf_file.name,
                "content": text
            })

        # Load TXT files
        for txt_file in self.docs_folder.glob("*.txt"):

            print(f"Loading TXT: {txt_file.name}")

            text = txt_file.read_text(
                encoding="utf-8"
            )

            documents.append({
                "filename": txt_file.name,
                "content": text
            })

        return documents