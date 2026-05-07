import os

# Define the save_form function
def save_form(form, output_path):
    with open(output_path, 'wb') as f:
        form.write(f)