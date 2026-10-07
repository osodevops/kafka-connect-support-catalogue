"""Build the public OSO Kafka Connect service overview from structured content."""
from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/OSO_Kafka_Connect_Support_and_Services.pdf'
W,H=612,792
NAVY=HexColor('#08034E'); BODY=HexColor('#4D5079'); MUTED=HexColor('#9496AF'); RULE=HexColor('#D9DBE8'); TINT=HexColor('#F2F3F9')
for name,f in [('Lexend','Lexend-Regular.ttf'),('LexendBold','Lexend-Bold.ttf'),('Space','SpaceGrotesk-Regular.ttf'),('SpaceBold','SpaceGrotesk-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(ROOT/'assets/fonts'/f)))
data=json.loads((ROOT/'docs/service-overview.json').read_text())
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('OSO Kafka Connect Support and Services')
c.setAuthor('OSO'); c.setSubject('Public overview of Kafka Connect support and engineering services')
def paragraph(text,x,top,width,size=11,leading=16,font='Space',colour=BODY):
 p=Paragraph(escape(text).replace('\n','<br/>'),ParagraphStyle('text',fontName=font,fontSize=size,leading=leading,textColor=colour))
 _,height=p.wrap(width,1000)
 p.drawOn(c,x,top-height)
 return top-height

# Cover uses the OSO house artwork and mark.
c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
c.drawImage(str(ROOT/'assets/cover-background.png'),0,0,width=W,height=H,mask='auto')
c.drawImage(str(ROOT/'assets/oso-logo.png'),62,642,width=106,height=70,preserveAspectRatio=True,anchor='nw',mask='auto')
paragraph('KAFKA CONNECT',62,550,485,11,15,'SpaceBold',MUTED)
paragraph(data['title'],62,508,485,34,43,'LexendBold',white)
paragraph(data['subtitle'],62,350,465,15,23,'Space',white)
c.setStrokeColor(Color(1,1,1,.35));c.line(62,182,550,182)
paragraph('SERVICE OVERVIEW',62,161,400,10,14,'SpaceBold',MUTED)
paragraph('oso.sh',62,130,450,12,17,'Space',white)
paragraph(data['date']+'  |  Version '+data['version'],62,91,450,9,13,'Space',MUTED)
c.showPage()
for index,page in enumerate(data['pages'],start=2):
 c.setFillColor(NAVY);c.rect(0,H-9,W,9,fill=1,stroke=0)
 paragraph('OSO  /  KAFKA CONNECT SUPPORT AND SERVICES',48,H-32,520,8,12,'SpaceBold',MUTED)
 paragraph(page['eyebrow'],48,720,515,9,13,'SpaceBold',MUTED)
 y=paragraph(page['title'],48,693,515,25,32,'LexendBold',NAVY)-15
 y=paragraph(page['intro'],48,y,515,11,16)-24
 for title,text in page['sections']:
  y=paragraph(title,48,y,515,13,18,'LexendBold',NAVY)-7
  y=paragraph(text,48,y,515,10.4,14.5)-15
 if y<110:
  raise ValueError(f'Page {index} overflows: final y={y:.1f}. Shorten its content.')
 c.setStrokeColor(RULE);c.line(48,97,564,97)
 paragraph(page['note'],48,84,515,8.3,11,'Space',BODY)
 paragraph('oso.sh',48,37,480,8,11,'Space',MUTED)
 c.setFillColor(MUTED);c.setFont('Space',8);c.drawRightString(564,26,f'{index} / {len(data["pages"])+1}')
 c.showPage()
c.save()
print(OUT)
