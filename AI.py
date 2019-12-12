import pandas as pd
import os

def formatnom(path):
    path=str(path)
    nom=[]
    for i in range(len(path)-1,0,-1):
        if path[i]=="/" or path[i]==ascii(92):
            break
        elif path[i]==".":
            continue
        else:
            nom.append(path[i])
    return ''.join(nom)
        

class data():
    def __init__(self,path,option):
        ops=('direct','copy')
        self.chemin=path
        self.df=pd.read_csv(path,error_bad_lines=False)
        self.nom=formatnom(self.chemin)
        option=ops[option]
        if option=='copy':
            df2=self.df
            df2.to_csv()
            self.chemin=os.getcwd()
            self.df=df2
            
    def __repr__(self):
        return self.df
    
    def replace(self,string,rpl):
        self.df.replace(string,rpl,inplace="True")
        
        
    
        
    
            
        
        
    
            