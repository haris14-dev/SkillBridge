from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)

        if not text or not text.strip():    #if text is empty it becomes false and "not" reverses it so condition becomes if true then it will print no text found
            print("No text found in the PDF.")
            return None

        return text

    except Exception as e:
        print("Error:", e)
        return None
        


   