from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from parse import *
from catalog.models import Size, Color

def parseColor(color):
    prs = parse("{} / {}", color)
    col = Color.objects.get_or_create(primary_color = prs[0], texture_color = prs[1])
    return prs

def parseSize(size):
    # print(size)
    prs = parse("{:d} x {:d} {:w}", size, case_sensitive=False)
    if(prs is None):
        prs = parse("{:d}x{:d} {:w}", size, case_sensitive=False)
    print(prs)
    siz = Size.objects.get_or_create(width = prs[0]*1.0, length = prs[1]*1.0)
    return prs

def ReallyCreateShipmentItem(qualityName, designName, color, size, quantity, ean):
    print("Quality : "+qualityName+
        " Design name : "+designName+
        " Color 1: "+parseColor(color)[0]+"Color 2 : "+parseColor(color)[1]+
        " Size w : "+str(parseSize(size)[0])+
        " Size h : "+str(parseSize(size)[1])+
        " Size s : "+str(parseSize(size)[2])+
        " Quantity :"+str(quantity))

def CreateShipmentItem(qualityName, designName, color, size, ean, quantity):
    if(ean):
        if(ean.isnumeric()):
            ReallyCreateShipmentItem(qualityName, designName, color, size, quantity, ean)

def shipment_created(shipment):

    print("Shipment Created with packing sheet " + str(shipment.packing_sheet.url))
    workbook = load_workbook(shipment.packing_sheet)
    packing_sheet = workbook.active

    col_names = {}
    column_index = 0 
    REQ_NAMES = set(['QUALTY', 'DESIGN', 'COLOR', 'SIZE', 'EAN CODE', 'PCS'])
    for column in packing_sheet.iter_cols(0, packing_sheet.max_column):
        if column[0].value in REQ_NAMES:
            col_names[column[0].value] = column_index
        column_index += 1



    from collections import defaultdict
    data = defaultdict(list)
    for row in packing_sheet.iter_rows(2, packing_sheet.max_row):
        for key, index in col_names.items():
            data[key].append(row[index].value)
            CreateShipmentItem(row[col_names['QUALTY']].value,
                            row[col_names['DESIGN']].value,
                            row[col_names['COLOR']].value,
                            row[col_names['SIZE']].value,
                            row[col_names['EAN CODE']].value,
                            row[col_names['PCS']].value)

    pass
