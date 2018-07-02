# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:46:24 2018

@author: jianya_liao
"""
#文件输出自动保存到输入文件夹
import pandas as pd
import os
import glob
path1=input("请输入要合档的文件地址：")
outsomedata=path1+"\\123.csv"
print(outsomedata)
firstfile=True
alldata=[]
for file in glob.glob(os.path.join(path1,"*.csv")):
    name=os.path.basename(file.upper().rstrip('.CSV'))
    print(name)
    if firstfile:  
      df=pd.read_csv(file,header=52)
      df.insert(0,"Wafer",name)
      columns=df.columns.values
      firstfile=False
      alldata.append(df)
    else:
      df=pd.read_csv(file,skiprows=53)
      df.insert(0,"Wafer",name)
      alldata.append(df)
alldata_concat=pd.concat(alldata,axis=0)
alldata_concat.to_csv(outsomedata,index=False,columns=columns)

