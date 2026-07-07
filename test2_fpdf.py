from fpdf import FPDF
import traceback

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=15, style='B')

pdf.cell(w=0, h=10, text="AI Resume Analysis Report", new_x="LMARGIN", new_y="NEXT", align='C')
print("After cell 1:", pdf.get_x(), pdf.get_y())

pdf.multi_cell(w=0, h=10, text="Matched Skills: Python", new_x="LMARGIN", new_y="NEXT")
print("After multicell 1:", pdf.get_x(), pdf.get_y())

try:
    pdf.multi_cell(w=0, h=10, text="Missing Skills: AWS", new_x="LMARGIN", new_y="NEXT")
    print("After multicell 2:", pdf.get_x(), pdf.get_y())
except Exception as e:
    traceback.print_exc()

