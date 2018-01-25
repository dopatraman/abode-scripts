from functools import partial
from openpyxl.reader.excel import load_workbook
from pprint import pprint
import argparse

COLUMNS = {
    "rule_name": "A",
    "rule_value": "C",
    "is_compliant": "D"
}
INTERIOR = (13, 16)
LOCATION = (18,19)
LOT = (21,38)
def get_zoning_data(worksheet, drange):
    get_column_ws = partial(_get_column, worksheet)
    rule_names = get_column_ws("rule_name", drange)
    rule_values = get_column_ws("rule_value", drange)
    return dict(zip(rule_names, rule_values))

def _get_column(worksheet, key, key_range):
    ci = COLUMNS.get(key, None)
    index_string = "{ci}{frm}:{ci}{to}".format(ci=ci,
                                               frm=key_range[0],
                                               to=key_range[1])
    if ci is not None:
        return [ row[0].value for row in worksheet[index_string]]
    raise KeyError('key not listed')

def _get_workbook(filename):
    return load_workbook(filename=filename, data_only=True)

def _get_worksheet(workbook, sheetname):
    return workbook.get_sheet_by_name(name=sheetname)

def _merge_dicts(dicts):
    all_dict = {}
    for d in dicts:
        all_dict.update(d.copy())
    return all_dict

def parse_workbook(filename, sheetname):
    wb = _get_workbook(filename=filename)
    ws = _get_worksheet(workbook=wb, sheetname=sheetname)
    return _merge_dicts([
            get_zoning_data(ws, INTERIOR),
            get_zoning_data(ws, LOCATION),
            get_zoning_data(ws, LOT)
            ])

def main():
    parser = argparse.ArgumentParser(prog="abode zoning parser")
    parser.add_argument('--workbookname', help='name of the workbook, use xlsx extention if possible')
    parser.add_argument('--sheetname', help='name of the worksheet, ie "ZONING ANALYSIS"')
    args = parser.parse_args()
    if (args.workbookname and args.sheetname):
        return parse_workbook(args.workbookname, args.sheetname)
    else:
        raise Exception("Invalid workbookname or sheetname")
    
if __name__ == '__main__':
    pprint(main())