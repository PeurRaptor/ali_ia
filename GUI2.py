import pandas as pd
import PySimpleGUI as sg
import numpy as np
from AI import data
from func import returnarray

def GUI2(df):
    col=returnarray(df.columns)
    layout=[[sg.Text('Wrangling et description')],
                        [sg.Listbox(values=col),sg.ReadButton('+/-'),sg.Listbox(values=[])], 
                        [sg.Text('Correlation:'),sg.ReadButton('voir',key='corr')], 
                        [sg.Text('anova:'),sg.ReadButton('voir',key='anova')], 
                        [sg.Text('pearson:'),sg.ReadButton('voir',key='pearson')],
                        [sg.VerticalSeparator(pad=None)],
                        [sg.Text('description:'),sg.ReadButton('voir',key='desc')], 
                        [sg.Text('groupe-pivot:'),sg.Text('index:'),sg.Input(),sg.Text('colonne:'),sg.Input(),sg.ReadButton('voir',key='piv')],
                        #no more separator
                        [sg.Text('frame:'),sg.Combo(['plot','hist'])],#resultats et plotting  
                        [sg.Input(),sg.ReadButton('Executer'),sg.Input()]]
    window = sg.Window('preprocessing', layout)
    event, values = window.Read()
    while True:
        event, values = window.Read()
        if event == "Executer":
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
                break