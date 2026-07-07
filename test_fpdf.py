from fpdf import FPDF
import traceback

try:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=15, style='B')
    
    # Title
    pdf.cell(w=0, h=10, txt="AI Resume Analysis Report", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)
    
    # ATS Score Section
    pdf.set_font("helvetica", size=12, style='B')
    pdf.cell(w=0, h=10, txt=f"ATS Score: 82 / 100", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=11)
    
    pdf.cell(w=0, h=10, txt=f"  - Skill Match: 28", new_x="LMARGIN", new_y="NEXT")
        
    pdf.ln(5)
    
    # Skill Gap Section
    pdf.set_font("helvetica", size=12, style='B')
    pdf.cell(w=0, h=10, txt=f"Skill Match: 80%", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", size=11)
    
    pdf.multi_cell(w=0, h=10, txt="Matched Skills: Python", new_x="LMARGIN", new_y="NEXT")
    pdf.multi_cell(w=0, h=10, txt="Missing Skills: AWS", new_x="LMARGIN", new_y="NEXT")
    
    pdf.output("test.pdf")
    print("SUCCESS")
except Exception as e:
    traceback.print_exc()
