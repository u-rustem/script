import re
import plotly.express as px

import matplotlib.image as mpimg
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import scipy
from scipy import stats
import os
import sqlite3
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import datetime
import pymysql.cursors
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import json
from plotly.subplots import make_subplots

import matplotlib.image as mpimg

time = datetime.datetime.now()

connection = pymysql.connect(host="192.168.1.31",
                             user="admin",
                             password="Password10!",
                             db="Utilization",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
print("connection successful!!")

#Varible hostname SGT
name = input('Пожалуйста, введите имя SGT:')
#Connection Database

fig = make_subplots(rows=10, cols=2, subplot_titles=("CC Timers: from 1 to 3", "CC Timers: from 4 to 6", "CC Timers: from 9 to 11", "CC Timers: from 12 to 14",
                                                    "CC Cer Drops: from 1 to 3", "CC Cer Drops: from 4 to 6", "CC Cer Drops: from 9 to 11", "CC Cer Drops: from 12 to 14",
                                                    "CC Ses Drops: from 1 to 3", "CC Ses Drops: from 4 to 6", "CC Ses Drops: from 9 to 11", "CC Ses Drops: from 12 to 14",
                                                    "Inbound SB7s", "Outbound SB7s", "Inbound SB8s", "Outbound SB8s",
                                                    "Inbound LAGs", "Outbound LAGs", "Total Inbound", "Total Outbound"))
#Percent Timer CCs
timer = "SELECT * FROM Utilization.timer where hostname = '%s'" % name
df = pd.read_sql(timer, connection)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['1_xlp_0'],  name='Timer: Slot 1 Xlp 0'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['1_xlp_1'],  name='Timer: Slot 1 Xlp 1'), row=1, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['2_xlp_0'],  name='Timer: Slot 2 Xlp 0'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['2_xlp_1'],  name='Timer: Slot 2 Xlp 1'), row=1, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['3_xlp_0'],  name='Timer: Slot 3 Xlp 0'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['3_xlp_1'],  name='Timer: Slot 3 Xlp 1'), row=1, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['4_xlp_0'],  name='Timer: Slot 4 Xlp 0'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['4_xlp_1'],  name='Timer: Slot 4 Xlp 1'), row=1, col=2)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['5_xlp_0'],  name='Timer: Slot 5 Xlp 0'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['5_xlp_1'],  name='Timer: Slot 5 Xlp 1'), row=1, col=2)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['6_xlp_0'],  name='Timer: Slot 6 Xlp 0'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['6_xlp_1'],  name='Timer: Slot 6 Xlp 1'), row=1, col=2)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['9_xlp_0'],  name='Timer: Slot 9 Xlp 0'), row=2, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['9_xlp_1'],  name='Timer: Slot 9 Xlp 1'), row=2, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['10_xlp_0'],  name='Timer: Slot 10 Xlp 0'), row=2, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['10_xlp_1'],  name='Timer: Slot 10 Xlp 1'), row=2, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['11_xlp_0'],  name='Timer: Slot 11 Xlp 0'), row=2, col=1)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['11_xlp_1'],  name='Timer: Slot 11 Xlp 1'), row=2, col=1)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['12_xlp_0'],  name='Timer: Slot 12 Xlp 0'), row=2, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['12_xlp_1'],  name='Timer: Slot 12 Xlp 1'), row=2, col=2)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['13_xlp_0'],  name='Timer: Slot 13 Xlp 0'), row=2, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['13_xlp_1'],  name='Timer: Slot 13 Xlp 1'), row=2, col=2)

fig.add_trace(go.Scatter(x=df['timedate'], y=df['14_xlp_0'],  name='Timer: Slot 14 Xlp 0'), row=2, col=2)
fig.add_trace(go.Scatter(x=df['timedate'], y=df['14_xlp_1'],  name='Timer: Slot 14 Xlp 1'), row=2, col=2)

#Cer Drops CCs
CerDrops = "SELECT * FROM Utilization.cer_drops where hostname = '%s'" % name
df1 = pd.read_sql(CerDrops, connection)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['1_xlp_0'],  name='CerDrop: Slot 1 Xlp 0'), row=3, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['1_xlp_1'],  name='CerDrop: Slot 1 Xlp 1'), row=3, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['2_xlp_0'],  name='CerDrop: Slot 2 Xlp 0'), row=3, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['2_xlp_1'],  name='CerDrop: Slot 2 Xlp 1'), row=3, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['3_xlp_0'],  name='CerDrop: Slot 3 Xlp 0'), row=3, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['3_xlp_1'],  name='CerDrop: Slot 3 Xlp 1'), row=3, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['4_xlp_0'],  name='CerDrop: Slot 4 Xlp 0'), row=3, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['4_xlp_1'],  name='CerDrop: Slot 4 Xlp 1'), row=3, col=2)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['5_xlp_0'],  name='CerDrop: Slot 5 Xlp 0'), row=3, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['5_xlp_1'],  name='CerDrop: Slot 5 Xlp 1'), row=3, col=2)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['6_xlp_0'],  name='CerDrop: Slot 6 Xlp 0'), row=3, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['6_xlp_1'],  name='CerDrop: Slot 6 Xlp 1'), row=3, col=2)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['9_xlp_0'],  name='CerDrop: Slot 9 Xlp 0'), row=4, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['9_xlp_1'],  name='CerDrop: Slot 9 Xlp 1'), row=4, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['10_xlp_0'],  name='CerDrop: Slot 10 Xlp 0'), row=4, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['10_xlp_1'],  name='CerDrop: Slot 10 Xlp 1'), row=4, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['11_xlp_0'],  name='CerDrop: Slot 11 Xlp 0'), row=4, col=1)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['11_xlp_1'],  name='CerDrop: Slot 11 Xlp 1'), row=4, col=1)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['12_xlp_0'],  name='CerDrop: Slot 12 Xlp 0'), row=4, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['12_xlp_1'],  name='CerDrop: Slot 12 Xlp 1'), row=4, col=2)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['13_xlp_0'],  name='CerDrop: Slot 13 Xlp 0'), row=4, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['13_xlp_1'],  name='CerDrop: Slot 13 Xlp 1'), row=4, col=2)

fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['14_xlp_0'],  name='CerDrop: Slot 14 Xlp 0'), row=4, col=2)
fig.add_trace(go.Scatter(x=df1['timedate'], y=df1['14_xlp_1'],  name='CerDrop: Slot 14 Xlp 1'), row=4, col=2)

#Ses Drops CCs
SesDrops = "SELECT * FROM Utilization.ses_drops where hostname = '%s'" % name
df2 = pd.read_sql(SesDrops, connection)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['1_xlp_0'],  name='SesDrop: Slot 1 Xlp 0'), row=5, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['1_xlp_1'],  name='SesDrop: Slot 1 Xlp 1'), row=5, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['2_xlp_0'],  name='SesDrop: Slot 2 Xlp 0'), row=5, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['2_xlp_1'],  name='SesDrop: Slot 2 Xlp 1'), row=5, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['3_xlp_0'],  name='SesDrop: lot 3 Xlp 0'), row=5, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['3_xlp_1'],  name='SesDrop: Slot 3 Xlp 1'), row=5, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['4_xlp_0'],  name='SesDrop: Slot 4 Xlp 0'), row=5, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['4_xlp_1'],  name='SesDrop: lot 4 Xlp 1'), row=5, col=2)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['5_xlp_0'],  name='SesDrop: Slot 5 Xlp 0'), row=5, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['5_xlp_1'],  name='SesDrop: Slot 5 Xlp 1'), row=5, col=2)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['6_xlp_0'],  name='SesDrop: Slot 6 Xlp 0'), row=5, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['6_xlp_1'],  name='SesDrop: Slot 6 Xlp 1'), row=5, col=2)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['9_xlp_0'],  name='SesDrop: Slot 9 Xlp 0'), row=6, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['9_xlp_1'],  name='SesDrop: Slot 9 Xlp 1'), row=6, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['10_xlp_0'],  name='SesDrop: Slot 10 Xlp 0'), row=6, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['10_xlp_1'],  name='SesDrop: Slot 10 Xlp 1'), row=6, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['11_xlp_0'],  name='SesDrop: Slot 11 Xlp 0'), row=6, col=1)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['11_xlp_1'],  name='SesDrop: Slot 11 Xlp 1'), row=6, col=1)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['12_xlp_0'],  name='SesDrop: Slot 12 Xlp 0'), row=6, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['12_xlp_1'],  name='SesDrop: Slot 12 Xlp 1'), row=6, col=2)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['13_xlp_0'],  name='SesDrop: Slot 13 Xlp 0'), row=6, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['13_xlp_1'],  name='SesDrop: Slot 13 Xlp 1'), row=6, col=2)

fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['14_xlp_0'],  name='SesDrop: Slot 14 Xlp 0'), row=6, col=2)
fig.add_trace(go.Scatter(x=df2['timedate'], y=df2['14_xlp_1'],  name='SesDrop: Slot 14 Xlp 1'), row=6, col=2)

#Inbound/Outbound SB_7_Ls and SB8s
Inbound = "SELECT * FROM Utilization.Inbound where hostname = '%s'" % name
df3 = pd.read_sql(Inbound, connection)

#Inbound/Outbound SB_7_Ls
Outbound = "SELECT * FROM Utilization.Inbound where hostname = '%s'" % name
df4 = pd.read_sql(Outbound, connection)

#SB7s
#Inbound
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L1'],  name='In: SB_7_L1'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L3'],  name='In: SB_7_L3'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L5'],  name='In: SB_7_L5'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L7'],  name='In: B_7_L7'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L9'],  name='In: SB_7_L9'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L11'],  name='In: SB_7_L11'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L13'],  name='In: SB_7_L13'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L15'],  name='In: SB_7_L15'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L17'],  name='In: SB_7_L17'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L19'],  name='In: SB_7_L19'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L21'],  name='In: SB_7_L21'), row=7, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_7_L23'],  name='In: SB_7_L23'), row=7, col=1)
#Outbound
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L1'],  name='Out: SB_7_L1', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L3'],  name='Out: SB_7_L3', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L5'],  name='Out: SB_7_L5', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L7'],  name='Out: SB_7_L7', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L9'],  name='Out: SB_7_L9', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L11'],  name='Out: SB_7_L11', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L13'],  name='Out: SB_7_L13', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L15'],  name='Out: SB_7_L15', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L17'],  name='Out: SB_7_L17', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L19'],  name='Out: SB_7_L19', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L21'],  name='Out: SB_7_L21', line=dict(width=4, dash='dot')), row=7, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_7_L23'],  name='Out: SB_7_L23', line=dict(width=4, dash='dot')), row=7, col=2)


#SB8s
#Inbound
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L1'],  name='In: SB_8_L1'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L3'],  name='In: SB_8_L3'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L5'],  name='In: SB_8_L5'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L7'],  name='In: SB_8_L7'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L9'],  name='In: SB_8_L9'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L11'],  name='In: SB_8_L11'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L13'],  name='In: SB_8_L13'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L15'],  name='In: SB_8_L15'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L17'],  name='In: SB_8_L17'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L19'],  name='In: SB_8_L19'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L21'],  name='In: SB_8_L21'), row=8, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['SB_8_L23'],  name='In: SB_8_L23'), row=8, col=1)
#Outbound
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L1'],  name='Out: SB_8_L1', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L3'],  name='Out: SB_8_L3', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L5'],  name='Out: SB_8_L5', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L7'],  name='Out: SB_8_L7', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L9'],  name='Out: SB_8_L9', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L11'],  name='Out: SB_8_L11', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L13'],  name='Out: SB_8_L13', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L15'],  name='Out: SB_8_L15', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L17'],  name='Out: SB_8_L17', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L19'],  name='Out: SB_8_L19', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L21'],  name='Out: SB_8_L21', line=dict(width=4, dash='dot')), row=8, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['SB_8_L23'],  name='Out: SB_8_L23', line=dict(width=4, dash='dot')), row=8, col=2)

#LAGs
#Inbound
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG1'],  name='In: LAG1'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG2'],  name='In: LAG2'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG3'],  name='In: LAG3'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG4'],  name='In: LAG4'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG5'],  name='In: LAG5'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG6'],  name='In: LAG6'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG7'],  name='In: LAG7'), row=9, col=1)
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['LAG8'],  name='In: LAG8'), row=9, col=1)
#Outbound
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG1'],  name='Out: LAG1', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG2'],  name='Out: LAG2', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG3'],  name='Out: LAG3', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG4'],  name='Out: LAG4', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG5'],  name='Out: LAG5', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG6'],  name='Out: LAG6', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG7'],  name='Out: LAG7', line=dict(width=4, dash='dot')), row=9, col=2)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['LAG8'],  name='Out: LAG8', line=dict(width=4, dash='dot')), row=9, col=2)

#Total
fig.add_trace(go.Scatter(x=df3['timedate'], y=df3['total'],  name='TotalInbound', line=dict(color='firebrick', width=4, dash='dot')), row=10, col=1)
fig.add_trace(go.Scatter(x=df4['timedate'], y=df4['total'],  name='TotalOutbound', line=dict(color='royalblue', width=4, dash='dot')), row=10, col=2)

img = mpimg.imread("Allot-logo-new.jpg")
mpimg.imsave("out.png", img)


fig.update_layout(template="ggplot2", height=3000, width=1500, title="Utilization Traffic SGT: %s" % name, title_font_size=30)

fig['layout']['yaxis']['title']='Timer Max 100%'
fig['layout']['yaxis2']['title']='Timer Max 100%'
fig['layout']['yaxis3']['title']='Timer Max 100%'
fig['layout']['yaxis4']['title']='Timer Max 100%'

fig['layout']['yaxis5']['title']='Cer Drops >'
fig['layout']['yaxis6']['title']='Cer Drops >'
fig['layout']['yaxis7']['title']='Cer Drops >'
fig['layout']['yaxis8']['title']='Cer Drops >'

fig['layout']['yaxis9']['title']='Ses Drops >'
fig['layout']['yaxis10']['title']='Ses Drops >'
fig['layout']['yaxis11']['title']='Ses Drops >'
fig['layout']['yaxis12']['title']='Ses Drops >'

fig['layout']['yaxis13']['title']='Traffics'
fig['layout']['yaxis14']['title']='Traffics'
fig['layout']['yaxis15']['title']='Traffics'
fig['layout']['yaxis16']['title']='Traffics'

fig['layout']['yaxis17']['title']='Traffics'
fig['layout']['yaxis18']['title']='Traffics'
fig['layout']['yaxis19']['title']='Total Traffics'
fig['layout']['yaxis20']['title']='Total Traffics'

fig.show()