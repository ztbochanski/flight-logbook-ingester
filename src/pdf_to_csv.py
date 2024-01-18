
import os
from img2table.ocr import VisionOCR
from img2table.document import PDF

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/zachbochanski/.config/gcloud/application_default_credentials.json"


# directory = 'data'
file = 'logbook.pdf'


def convert_pdfs(directory):
    path = os.path.join(directory, file)
    pdf = PDF(src=path)
    print('Calling Google Cloud Vision API')
    vision_ocr = VisionOCR(api_key=None)
    extracted_tables = pdf.extract_tables(ocr=vision_ocr,
                                          implicit_rows=False,
                                          borderless_tables=False,
                                          min_confidence=50)
    print('Converting PDFs to CSVs')
    for page, tables in extracted_tables.items():
        for idx, table in enumerate(tables):
            table.df.to_csv(f"output/{page+1}_{file.replace('.pdf', '.csv')}", index=False)
