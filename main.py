import os
import sys
from ai_pdf_form_filler import PdfFormFiller

# Create an instance of the PdfFormFiller class
filler = PdfFormFiller()

# Fill the form
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python main.py <form.pdf> <output.pdf>')
        sys.exit(1)

    form_path = sys.argv[1]
    output_path = sys.argv[2]

    # Fill the form
    filled_form = filler.fill_form(form_path, {'field1': 'value1', 'field2': 'value2'})
    filled_form.save(output_path)