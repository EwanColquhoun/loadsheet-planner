from fpdf import FPDF


def get_me_a_pyfpdf():
    title = "This The Doc Title"
    heading = "First Paragraph"
    text = 'bla ' * 10000

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 15)
    pdf.cell(w=210, h=9, txt=title, border=0, ln=1, align='C', fill=0)
    pdf.set_font('Times', 'B', 15)
    pdf.cell(w=0, h=6, txt=heading, border=0, ln=1, align='L', fill=0)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(w=0, h=5, txt=text)
    response = make_response(pdf.output(dest='S'))
    response.headers['Content-Type'] = 'application/pdf'
    return pdf.output(dest='S').encode('latin-1')


pdftest = get_me_a_pyfpdf()
print(pdftest)