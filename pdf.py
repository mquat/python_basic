import json
# from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, PageBreak

from reportlab.lib.units import mm, inch

hazop_data = json.dumps({'total_count':85, 'total_ratio': 92, 'total_average':33})

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 10)
    page_number_text = "%d" %(doc.page)
    canvas.drawCentredString(
        0.75 * inch,
        0.75 * inch,
        page_number_text
    )
    canvas.restoreState()    

def export_pdf(hazop_data):
    # pdf_buffer = BytesIO()
        
    req_hazop_data = json.loads(hazop_data)

    pagesize = (140 * mm, 216 * mm)

    my_doc = SimpleDocTemplate(
        "my_doc.pdf", 
        pagesize=pagesize,
        topMargin=1*inch,
        leftMargin=1*inch,
        rightMargin=1*inch,
        bottomMargin=1*inch
    )

    flowables = []

    sample_style_sheet = getSampleStyleSheet()
    custom_body_style = sample_style_sheet['BodyText']
    custom_body_style.fontName = 'Helvetica'
    custom_body_style.fontSize = 15



    paragraph_1 = Paragraph("A title", sample_style_sheet['Heading1'])
    paragraph_2 = Paragraph("VSFTY Count: Total %d cases" %(req_hazop_data['total_count']), sample_style_sheet['BodyText'])
    paragraph_3 = Paragraph("VSFTY Ratio: Total %d%%" %(req_hazop_data['total_ratio']), sample_style_sheet['BodyText'])
    paragraph_4 = Paragraph("VSFTY Average: %d on average" %(req_hazop_data['total_average']), sample_style_sheet['BodyText'])
    paragraph_5 = Paragraph("<b>Dingbat</b> paragraph - created this page to test 'pagebreak()'", custom_body_style)

    flowables.append(paragraph_1)
    flowables.append(paragraph_2)
    flowables.append(paragraph_3)
    flowables.append(paragraph_4)
    flowables.append(PageBreak())
    flowables.append(paragraph_5)

    my_doc.build(
        flowables,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

export_pdf(hazop_data)

def textobject_demo(hazop_data):
    req_hazop_data = json.loads(hazop_data)

    my_canvas = canvas.Canvas("txt_obj.pdf", pagesize=A4)

    text_object = my_canvas.beginText()
    text_object.setTextOrigin(10, 730)
    text_object.setFont('Times-Roman', 12)
    text_object.setFillColor(colors.darkgreen)
    text_object.textLines("""
        1. Total Count: %d
        2. Total Ratio: %d%% 
        3. Total Average: %d
    """ %(req_hazop_data['total_count'], req_hazop_data['total_ratio'], req_hazop_data['total_average']))

    my_canvas.drawText(text_object)

    my_canvas.save()

textobject_demo(hazop_data)    