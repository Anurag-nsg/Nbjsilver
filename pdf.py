from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def create_pdf(data_list):
    pdf_buffer = BytesIO()
    pdf_doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
    num_columns = len(data_list[0])
    col_width = A4[0] / num_columns 

    table_data = [list(data_list[0].keys())] + [list(d.values()) for d in data_list]
    table = Table(table_data, colWidths=[col_width] * num_columns, splitByRow=1)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    pdf_doc.build([table])

    return pdf_buffer.getvalue()

def send_email(pdf_content, recipient_email,mes):
    msg = MIMEMultipart()
    msg['From'] = 'silver.sender.n@gmail.com' 
    msg['To'] = recipient_email
    msg['Subject'] = f'{mes} PDF Report'
    pdf_attachment = MIMEApplication(pdf_content, _subtype='pdf')
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='report.pdf')
    message = f'<b>{mes} List pdf has been sent from Anurag</b>'
    msg.attach(MIMEText(message, 'html'))
    msg.attach(pdf_attachment)

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  
    smtp_server.starttls()
    smtp_server.login('silver.sender.n@gmail.com', 'oipt yiku ksjb yemc') 
    smtp_server.sendmail('silver.sender.n@gmail.com', recipient_email, msg.as_string())
    smtp_server.quit()

def pdf_and_send(data_list, recipient_email,mes):
    pdf_content = create_pdf(data_list)
    send_email(pdf_content, recipient_email,mes)

def pdf(data_list,mes):
    recipient_email = 'nbjsilver@gmail.com'
    pdf_and_send(data_list, recipient_email,mes)
