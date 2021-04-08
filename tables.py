from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

data = [
    ['Kode Produk', 'Kode Warehouse', 'Nama Produk', 'Qty',],
    ['PRD-213', 'W001', 'Bantex', '120 Box',],
    ['PRD-219', 'W001', 'Spidol Snowman', '200 Box',],
    ['PRD-786', 'W002', 'Gunting', '200 Pcs',],
]


pdf = SimpleDocTemplate(
    'laporan_warehouse.pdf',
    pagesize=A4
)


table = Table(data)

style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.HexColor(0x23A455)),
    ('TEXTCOLOR',(0, 0), (3, 0), colors.HexColor(0xFFFFFF)),

    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,0), 12),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
])

table.setStyle(style)

rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.HexColor(0xD27DA9)
    else:
        bc = colors.HexColor(0x6EC1E4)
    
    ts = TableStyle(
        [('BACKGROUND', (0,i),(-1,i), bc)]
    )
    table.setStyle(ts)


ts = TableStyle(
    [
        ('BOX',(0,0),(-1,-1), 1.5,colors.HexColor(0xa9a9a9)),
        ('GRID',(0,1),(-1,-1),1,colors.HexColor(0xa9a9a9)),
    ]
)
table.setStyle(ts)


elems = []
elems.append(table)

pdf.build(elems)


# 2) Alternate backgroud color

# 3) Add borders




