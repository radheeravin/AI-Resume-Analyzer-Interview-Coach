from fpdf import FPDF
import traceback

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=15, style='B')

pdf.cell(200, 10, txt="Skill Match: 80%", ln=True)
print("After cell:", pdf.get_x())

pdf.multi_cell(0, 10, txt="Matched Skills: Python")
print("After multi_cell 1:", pdf.get_x())

try:
    pdf.multi_cell(0, 10, txt="Missing Skills: AWS")
    print("After multi_cell 2:", pdf.get_x())
except Exception as e:
    traceback.print_exc()
