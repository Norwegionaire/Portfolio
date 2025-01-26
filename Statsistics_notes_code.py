# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:57:13 2024

@author: engeb
"""

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# =============================================================================
# def task():
#     fertilizer = np.array([1]*5 + [2]*5 + [3]*5 )
#     
#     height = np.array([10.5, 50.6, 20, 30.9, 40] + [50.9, 40, 35, 12, 19] + [80, 90, 60.1, 80.1, 90])
#     
#     dataframe = pd.DataFrame({"Fertilizer": fertilizer, "Height": height})
#     
#     anova = smf.ols("Height ~ C(Fertilizer)", data = dataframe).fit()
#     
#     anova_table = sm.stats.anova_lm(anova, typ=2)
#     print(anova_table)
#     turkey = pairwise_tukeyhsd(endog = dataframe["Height"], groups = dataframe["Fertilizer"])
#     print("\nTukey's HSD Test Results")
#     print(turkey.summary())
# 
# =============================================================================
#task()

def task_2():
    region = np.array(["NorthEast"]*5 + ["Midwest"]*6 + ["South"]*4 + ["West"]*5)
    NorthEast = [15, 10, 13, 14, 13]
    Midwest = [17, 12, 18, 13, 15, 12]
    South = [11, 7, 9, 13]
    West = [10, 12, 8, 7, 9]
    dataregion = np.array(NorthEast + Midwest + South + West)
    
    dataFrame = pd.DataFrame({"Region" : region, "Data" : dataregion})

    anovaregion = smf.ols("Data ~ C(Region)", data = dataFrame).fit()
    
    anovaregion_table = sm.stats.anova_lm(anovaregion, typ = 2)
    print(anovaregion_table)
    turkey2 = pairwise_tukeyhsd(endog = dataFrame["Data"], groups = dataFrame["Region"], alpha = 0.05)
    print(turkey2.summary())

def task_2d():
    dataRegion = {"Northeast" : [15, 10, 13, 14, 13, None],
            "Midwest" : [17, 12, 18, 13, 15, 12],
            "South" : [11, 7, 9, 13, None, None],
            "West" : [10, 12, 8, 7, 9, None]}
    df = pd.DataFrame(dataRegion)
    
    df_long = df.melt(var_name = "Region", value_name = "Value")
    df_long.dropna(inplace = True)
    
    #print(df_long)
    
    fanovaregion = smf.ols("Region ~ C(Value)", data = df).fit()
    
    fanovaregion_table = sm.stats.anova_lm(fanovaregion, typ = 2)
    print(fanovaregion_table)
    fturkey2 = pairwise_tukeyhsd(endog = df["Value"], groups = df["Region"], alpha = 0.05)
    print(fturkey2.summary())

task_2()
print()
#task_2d()