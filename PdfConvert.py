from fpdf import FPDF

pdf = FPDF()
# Add a page
pdf.add_page()
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)
# open the text file in read mode
f = open("C:\\Users\\Saransh\\PycharmProjects\\Text_Summarizer\\readme.txt", "r")
# insert the texts in pdf
for x in f:
    pdf.cell(50, 5, txt=x, ln=1, align='C')
# save the pdf with name .pdf
pdf.output("C:\\Users\\Saransh\\PycharmProjects\\Text_Summarizer\\result.pdf")
