import PyPDF2
import pdfplumber
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Define the PdfFormFiller class
class PdfFormFiller:
    def __init__(self):
        self.model = RandomForestClassifier()

    # Define the fill_form method
    def fill_form(self, form_path, fields):
        # Load the form
        form = pdfplumber.open(form_path)

        # Extract the form fields
        form_fields = form.pages[0].extract_words()

        # Fill the form fields
        filled_form = PyPDF2.PdfFileReader(form_path)
        for field in form_fields:
            if field['text'] in fields:
                filled_form.pages[0].__setitem__(field['text'], fields[field['text']])

        # Save the filled form
        with open('filled_form.pdf', 'wb') as f:
            filled_form.write(f)

        return filled_form