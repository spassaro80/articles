import pandas as pd
import numpy as np
from django.conf import settings
import os, math
from datetime import date

def load_data_from_excel(file_name):

    #TODO when Django runs this line can be deleted and substitued by settins.BASE_DIR
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    xl = pd.ExcelFile(BASE_DIR + "\\" + file_name)

    sheets = []
    for sheet in xl.sheet_names:

        df = xl.parse(sheet)
        sheet_instance = {}
        table = {'table_name' : df.columns.values[2].replace(" ", "")}
        items = []

        date = df.columns.values[6].date()
        for i in df.index:
            if i > 0 and df.iat[i,2] is not np.nan:
                item_instance = {}
                item_instance['date'] = date
                item_instance['codes'] = df.iat[i,0]
                item_instance['bill_no'] = df.iat[i,1]
                item_instance['itemes'] = df.iat[i,2]
                item_instance['item_detail'] = df.iat[i,3]
                item_instance['detail'] = df.iat[i,4]
                item_instance['qty'] = df.iat[i,5]
                item_instance['U_PRS_USD'] = round(df.iat[i,6],2)
                item_instance['TOTAL_PRS_USD'] = round(df.iat[i,7],2)
                item_instance['U_PRS_DHS'] = round(df.iat[i,8],2)
                item_instance['S_PRS_dhs'] = round(df.iat[i,9],2)
                item_instance['LO_AND_PR'] = round(df.iat[i,10],2)
                items.append(item_instance)
        sheet_instance['table'] = table
        sheet_instance['items'] = items
        sheets.append(sheet_instance)

    return sheets

if __name__ == '__main__':
    sheets = load_data_from_excel("file_name")
    print(sheets)