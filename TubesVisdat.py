#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bokeh')


# In[2]:


# import handling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import librari bokeh
import bokeh
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import HoverTool
import bokeh.sampledata


# In[3]:


fifa = pd.read_csv('fifa20.csv')
fifa.head()


# In[12]:


#menentukan figure
fig = figure()

#output file
output_file('fifa20.html', 
            title='top player')

#memasukkan data ke column
fifa_top = ColumnDataSource(fifa)

#memilih tools
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

#membuat figure
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']



# menambahkan representasi dari player
fig.square(x='Finishing',
           y='Hits',
           source=fifa_top,
           color='royalblue',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3)

# Format the tooltip
tooltips = [
            ('Player','@Name'),
            ('shoting', '@Finishing'),
            ('Total gol', '@Hits'),
           ]

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig)


# In[ ]:





# In[ ]:




