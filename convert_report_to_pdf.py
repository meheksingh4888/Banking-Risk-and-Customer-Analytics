"""
Convert markdown report to PDF
"""
import os

# Try different methods to convert markdown to PDF
def convert_md_to_pdf():
    md_file = r"c:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\docs\09_Project_Report.md"
    pdf_file = r"c:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\docs\09_Project_Report.pdf"
    
    # Method 1: Try using pandoc (most professional output)
    try:
        import subprocess
        result = subprocess.run(
            ["pandoc", md_file, "-o", pdf_file, "-V", "geometry:margin=1in"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ Successfully converted to PDF using pandoc: {pdf_file}")
            return True
    except FileNotFoundError:
        print("pandoc not found, trying alternative method...")
    
    # Method 2: Try using weasyprint
    try:
        import markdown
        from weasyprint import HTML, CSS
        import tempfile
        
        # Read markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Add CSS styling
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    margin: 1in;
                }}
                h1 {{
                    color: #0066cc;
                    border-bottom: 3px solid #0066cc;
                    padding-bottom: 10px;
                    margin-top: 30px;
                }}
                h2 {{
                    color: #0066cc;
                    margin-top: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 15px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #0066cc;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                ul, ol {{
                    margin: 10px 0;
                    padding-left: 20px;
                }}
                li {{
                    margin: 5px 0;
                }}
                hr {{
                    border: none;
                    border-top: 2px solid #0066cc;
                    margin: 30px 0;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as tmp:
            tmp.write(html_with_style)
            tmp_path = tmp.name
        
        try:
            # Convert to PDF
            HTML(tmp_path).write_pdf(pdf_file)
            print(f"✓ Successfully converted to PDF using weasyprint: {pdf_file}")
            return True
        finally:
            os.unlink(tmp_path)
            
    except ImportError as e:
        print(f"weasyprint/markdown not available: {e}")
    
    # Method 3: Try using reportlab (basic conversion)
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        import re
        
        # Read markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Create PDF
        doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
        styles = getSampleStyleSheet()
        elements = []
        
        # Custom styles
        heading1_style = ParagraphStyle(
            'Heading1Custom',
            parent=styles['Heading1'],
            fontSize=20,
            textColor=colors.HexColor('#0066cc'),
            spaceAfter=12,
            borderPadding=12,
            borderRadius=5
        )
        
        # Parse markdown and convert
        lines = md_content.split('\n')
        for line in lines:
            if line.startswith('# '):
                text = line.replace('# ', '')
                elements.append(Paragraph(text, heading1_style))
                elements.append(Spacer(1, 0.2*inch))
            elif line.startswith('## '):
                text = line.replace('## ', '')
                elements.append(Paragraph(text, styles['Heading2']))
                elements.append(Spacer(1, 0.1*inch))
            elif line.strip() and not line.startswith('---'):
                elements.append(Paragraph(line, styles['Normal']))
                elements.append(Spacer(1, 0.05*inch))
            elif line.startswith('---'):
                elements.append(Spacer(1, 0.1*inch))
        
        doc.build(elements)
        print(f"✓ Successfully converted to PDF using reportlab: {pdf_file}")
        return True
        
    except ImportError as e:
        print(f"reportlab not available: {e}")
    
    print("✗ Could not convert markdown to PDF. Installing required packages...")
    return False

if __name__ == "__main__":
    convert_md_to_pdf()
