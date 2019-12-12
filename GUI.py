import pandas as pd
import PySimpleGUI as sg
import numpy as np
from GUI2 import GUI2
from AI import data
from func import returnarray


layoutfindfile =[[sg.Text('Emplacement du fichier')],    
        [sg.Text('csv file', size=(8, 1)), sg.Input(), sg.FileBrowse()],      
        [sg.Submit(), sg.Cancel()]]


window = sg.Window('File', layoutfindfile)  
event, values = window.Read()  
window.Close()
print(event, values)

if values[0][len(values[0])-4:len(values[0])]==".csv":
    d=data(values[0],1)
    df=d.df
    dst = [
    [sg.Table(values=df,
              display_row_numbers=True,
              auto_size_columns=False,
              num_rows=min(25, len(df)))]
    ]
    window2=sg.Window('dst',dst)
    #window2.read()
    col=returnarray(df.columns)
    print(col)
    layoutpreprocessing=[[sg.Text('Preprocessing')],
                    [sg.Checkbox(''),sg.Text('valeur:'),sg.Combo(values=col),sg.Input()],
                    [sg.Checkbox(''),sg.Text('type:'),sg.Combo(values=col),sg.Combo(values=('float','int'))],
                    [sg.Checkbox(''),sg.Text('remplacer nuls'),sg.Combo(values=col) ,sg.Input()],
                    [sg.Checkbox(''),sg.Text('drop nuls'), sg.Combo(values=col),sg.Combo(['0','1'])],      
                    [sg.Checkbox(''),sg.Text('binning'), sg.Combo(values=col),sg.Input(),sg.Input()],  
                    [sg.ReadButton('Appliquer'),sg.ReadButton('Fin'), sg.Cancel()]]
    window = sg.Window('preprocessing', layoutpreprocessing)
    event, values = window.Read()
    while True:
        event, values = window.Read()
        if event == "Appliquer":
                if values[0]==True and values[2]!=None:
                        df[values[1]]=exec(values[2])
                if values[3]==True:
                        df[values[4]]=df[values[4]].astype(values[5])
                if values[6]==True:
                        df[values[7]].replace(np.nan,values[8])
                if values[9]==True:
                        df.dropna(subset=[values[10]],axis=int(values[11]))
                if values[12]==True:
                        bins=np.linspace(min(df[values[13]]),max(df[values[13]]),int(values[14])+1)
                        group=returnarray(values[15])
                        df['new'+values[13]]=pd.cut(df[values[13]],bins,labels=group,include_lowest=True)
        if event == "Fin":
                window.Close()
                GUI2(df)
                break