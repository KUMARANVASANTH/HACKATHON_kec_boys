# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:25:56 2022

@author: DELL
"""
import pandas as pd
def waterspray(f1,f2,i):
    if(i>=len(f1)-1):
        print("finished")
    else:    
        if(f1[i]<24 or f2[i]>71):
            return(i)
        else:
            print("In water spary :",f1[i],f2[i],i)
            waterspray(f1,f2,i+1)

def heat(f1,f2,i):
    if(i>=len(f1)-1):
        print("finished")
    else:    
        if(f1[i]>26 or f2[i]<59):
            return(i)
        else:
            print("In heat :",f1[i],f2[i],i)
            heat(f1,f2,i+1)

def launch(f1,f2,i):
    if(i>=len(f1)-1):
        print("finished")
    else:    
        if(f1[i]>27 or f2[i]<58):
            i=waterspray(f1,f2,i)
            if(i):
                launch(f1,f2,i+1)
        elif(f1[i]<23 or f2[i]>72):
            i=heat(f1,f2,i)
            if(i):
                launch(f1,f2,i+1)
        else:
            launch(f1,f2,i+1)
            
df=pd.read_csv("feeds.csv")
f1=list(df['field1'])
f2=list(df['field2'])
launch(f1,f2,0)
