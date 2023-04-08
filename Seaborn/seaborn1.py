# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:59:25 2022

@author: HAMZA
"""
"""
# INTRODUCTION
1. Read datas
1. Poverty rate of each state
1. Most common 15 Name or Surname of killed people
1. High school graduation rate of the population that is older than 25 in states
1. Percentage of state's population according to races that are black,white,native american, asian and hispanic
1. High school graduation rate vs Poverty rate of each state
1. Kill properties
    * Manner of death
    * Kill weapon
    * Age of killed people
    * Race of killed people
    * Most dangerous cities
    * Most dangerous states
    * Having mental ilness or not for killed people
    * Threat types
    * Flee types
    * Having body cameras or not for police
1. Race rates according to states in kill data 
1. Kill numbers from states in kill data
1. Plotly Visualization Tutorial: https://www.kaggle.com/kanncaa1/plotly-tutorial-for-beginners
<br>
<br>
Plot Contents:
* [Bar Plot]
* [Point Plot]
* [Joint Plot]
* [Pie Chart]
* [Lm Plot]
* [Kde Plot]
* [Violin Plot]
* [Heatmap]
* [Box Plot]
* [Swarm Plot]
* [Pair Plot]
* [Count Plot]
"""    

    
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import warnings
warnings.filterwarnings('ignore') 

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))


# Read datas
median_house_hold_in_come = pd.read_csv('../../../../../Yeni klasör/MedianHouseholdIncome2015.csv', encoding="windows-1252")
percentage_people_below_poverty_level = pd.read_csv('../../../../../Yeni klasör/PercentagePeopleBelowPovertyLevel.csv', encoding="windows-1252")
percent_over_25_completed_highSchool = pd.read_csv('../../../../../Yeni klasör/PercentOver25CompletedHighSchool.csv', encoding="windows-1252")
share_race_city = pd.read_csv('../../../../../Yeni klasör/ShareRaceByCity.csv', encoding="windows-1252")
kill = pd.read_csv('../../../../../Yeni klasör/PoliceKillingsUS.csv', encoding="windows-1252")



a1= pd.DataFrame(median_house_hold_in_come)
a2= pd.DataFrame(percentage_people_below_poverty_level)
a3= pd.DataFrame(percent_over_25_completed_highSchool)
a4= pd.DataFrame(share_race_city)
a5= pd.DataFrame(kill)

#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob
#qw   qlıdıbd  wıucbewcdıuwcbpdıuwbcpbdwecob


























