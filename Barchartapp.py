#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:09:10 2017

@author: Nimra
"""
from __future__ import division #used 2.7 python
import plotly.graph_objs as go
import pandas as pd



def BarChart():
    csv = pd.read_csv('bevgeburtenjahrgeschlquartstz.csv') #rreading the data
    csv_d = csv.loc[csv['StichtagDatJahr']== 2015] #make a smaller data set whcih only contains stuff from 2015
    newframe = csv_d[["QuarLang","SexKurz","AnzGebuWir"]] #only relevant columns
    
    dataset = {   #this set contains all relevant info under each other for given zone
            "Zone":[],
            "GeburtenM":[],
            "GeburtenF":[]
    }
    areas= (set(newframe["QuarLang"])) #all posssible areas we have
    for area in areas:
        dataset["Zone"].append(area) #adding it to the dataset
        
        
    for area in areas: #need to get births for every area
        w_counter = 0 #each area has it is own counter
        m_counter = 0
        for index, row in newframe.iterrows(): #going through the values
            if row["QuarLang"]== area and row["SexKurz"] == "M":
                m_counter += row["AnzGebuWir"]
                                                        #if it matches area then add it to the sex
            if row["QuarLang"]== area and row["SexKurz"] == "W":
                w_counter += row["AnzGebuWir"]
        dataset["GeburtenM"].append(m_counter)
        dataset["GeburtenF"].append(w_counter)
    return dataset

def DonutChart():
    csv = pd.read_csv('bevgeburtenjahrgeschlquartstz.csv')
    csv_d = csv.loc[csv['StichtagDatJahr']== 2015] #make a smaller data set whcih only contains stuff from 2015
    newframe = csv_d[["SexKurz","AnzGebuWir"]]
    w_counter = 0
    m_counter = 0 #total count of female or males
    for index, row in newframe.iterrows():
        if row["SexKurz"] == "M":
            m_counter += row["AnzGebuWir"]
            
        if row["SexKurz"] == "W":
            w_counter += row["AnzGebuWir"] #same as before, we check if it is male or female and add
    
    dataframe = {
            "Male" : round(float(m_counter/ (m_counter + w_counter)*100), 3),
            "Female": round(float(w_counter/ (m_counter + w_counter)*100), 3) #turning it into precents
            
            }
    return dataframe

def LineChart():
    csv = pd.read_csv('bevgeburtenjahrgeschlquartstz.csv')
    csv_new = csv[["StichtagDatJahr","SexKurz","AnzGebuWir"]] #again only the needed stuff
    
    dataset = {
            "Year": [],
            "Male":[],
            "Female": [],
            "Summe":[]
    }
    
    
    dyears= (set(csv_new["StichtagDatJahr"]))
    for year in dyears:
        dataset["Year"].append(year) #need it in a list so we can fill it up later and use as axis
        
      
        
    for year in dyears:
        w_counter = 0
        m_counter = 0
        for index, row in csv_new.iterrows():
            if row["StichtagDatJahr"]== year and row["SexKurz"] == "M": #couting m for every year
                m_counter += row["AnzGebuWir"]
            if row["StichtagDatJahr"]== year and row["SexKurz"] == "W": #counting w for every year
                w_counter += row["AnzGebuWir"]
            
        dataset["Male"].append(m_counter)
        dataset["Female"].append(w_counter)
        dataset["Summe"].append(w_counter+m_counter)    #add it in list, all pairs underneath each other
    
    return dataset


