import PyPDF2

# Open the PDF file and read its contents
pdf_file = open('previewlease1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Check if the PDF file is encrypted
if pdf_reader.is_encrypted:
    # Try to decrypt the PDF file with an empty password
    pdf_reader.decrypt('')

# Create a new PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Copy the pages from the original PDF reader to the new PDF writer
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Save the new PDF file without password protection
new_pdf_file = open('new_filename.pdf', 'wb')
pdf_writer.write(new_pdf_file)

# Close the files
pdf_file.close()
new_pdf_file.close()
