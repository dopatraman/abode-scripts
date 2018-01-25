## Abode scripts

A convenient place to store scripts. Doesn't have any structure yet.

### Zoning document parser
This is a one off for parsing a zoning document (spreadsheet) that has 2 columns:
    1. rule_name
    2. rule_value

once you've run
```
pip install -r requirements.txt
```

run the main script with arguments for the workbook name and sheet:
```
python main.py --workbookname ZoningSurvey.xlsm --sheetname "Zoning Analysis"
```
You should get a `dict` of key-value pairs.