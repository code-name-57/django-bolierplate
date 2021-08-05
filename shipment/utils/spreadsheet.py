from openpyxl import load_workbook
from parse import *
from catalog.models import Size, Color, Collection, Carpet, DesignInColor, Design
from shipment.models import ShipmentItem


def parseColor(color):
    prs = parse("{} / {}", color)
    col, _ = Color.objects.get_or_create(primary_color=prs[0], texture_color=prs[1])
    return col


def parseSize(size):
    prs = parse("{:d} x {:d} {:w}", size, case_sensitive=False)
    if(prs is None):
        prs = parse("{:d}x{:d} {:w}", size, case_sensitive=False)

    siz, _ = Size.objects.get_or_create(width=prs[0]*1.0, length=prs[1]*1.0, shape=prs[2])
    return siz


def ProcessShipmentItem(shipment, qualityName, designName, color, size, ean, quantity):
    def _create():
        sizeInstance = parseSize(size)
        colorInstance = parseColor(color)
        quality, _ = Collection.objects.get_or_create(name=qualityName)
        design, _ = Design.objects.get_or_create(name=designName, collection=quality)
        designInColor, _ = DesignInColor.objects.get_or_create(design=design, color=colorInstance)
        cpt, _ = Carpet.objects.get_or_create(designColor=designInColor, size=sizeInstance)
        shipmentItem, _ = ShipmentItem.objects.get_or_create(
            shipment=shipment, carpet=cpt, barcode=ean, quantity=quantity, )

    if(ean):
        if(ean.isnumeric()):
            _create()


def process_packing_sheet(shipment):

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
            ProcessShipmentItem(shipment, row[col_names['QUALTY']].value,
                               row[col_names['DESIGN']].value,
                               row[col_names['COLOR']].value,
                               row[col_names['SIZE']].value,
                               row[col_names['EAN CODE']].value,
                               row[col_names['PCS']].value)

    pass
