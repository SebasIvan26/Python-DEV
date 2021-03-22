import pandas as pd
import numpy as np
import matplotlib
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

def writeStatsToFile(nbStat, lbStat, ocfStat, destination):
    writer = pd.ExcelWriter(destination, engine='openpyxl', mode='a')
    writer.book = load_workbook(destination)
    writer.sheets = {ws.title:ws for ws in writer.book.worksheets}
    nbStat.to_excel(writer, sheet_name='NB', freeze_panes=(1,0))
    lbStat.to_excel(writer, sheet_name='LB', freeze_panes=(1,0))
    ocfStat.to_excel(writer, sheet_name='OCF', freeze_panes=(1,0))
    writer.save()
    writer.close()
    #except Exception:
     #   print("Statistic Performance Tabs are not properly saved")

def getDataStat(filepath, memoTName):
    
    memo_data_df = pd.read_excel(filepath, sheet_name=memoTName, usecols=['Account Name', 'NB', 'LB', 'OCF'])
    memo_data_df = memo_data_df.dropna()
    df_source = memo_data_df

    df1 = df_source.groupby(['Account Name'])['NB'].sum().sort_values(ascending=False)
    df1.loc['Total'] = df1.sum()

    df2 = df_source.groupby(['Account Name'])['LB'].sum().sort_values(ascending=True)
    df2.loc['Total'] = df2.sum()

    df3 = df_source.groupby(['Account Name'])['OCF'].sum().sort_values(ascending=True)
    df3.loc['Total'] = df3.sum()

    return [df1, df2, df3]

def main():

    source = r'/Users/sebastienstvil/Documents/Python/Python-DEV/Beta Project - Velocity/Base-Lab/Testing/wtc_cash_flows/WTC Cash Flow testingRes.xlsx'
    destination = r'/Users/sebastienstvil/Documents/Python/Python-DEV/Beta Project - Velocity/Base-Lab/Testing/wtc_cash_flows/Book1.xlsx'
    dataTab = 'Memo'

    ##Read and Analyze file with Pandas
    stats_pivot_tables = getDataStat(source, dataTab)

    nbStat = stats_pivot_tables[0]
    lbStat = stats_pivot_tables[1]
    ocfStat = stats_pivot_tables[2]

    print(nbStat)
    print(lbStat)
    print(ocfStat)

    writeStatsToFile(nbStat, lbStat, ocfStat, destination)

    


    


   


if __name__ == "__main__":
    main()