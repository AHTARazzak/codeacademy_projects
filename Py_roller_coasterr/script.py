import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np

# load rankings data here:
wdb = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
sdb = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#print(wdb.head(5))

# write function to plot rankings over time for 1 roller coaster here:

def coastername(name,dataframe):
  thecoaster=dataframe[dataframe["Name"].str.contains(name)]
  ax = plt.gca()
  thecoaster.plot(kind='line',x='Year of Rank',y='Rank',ax=ax)
  ax.legend([name])
  plt.show()
  plt.clf()

#coastername("El Toro",wdb)

# write function to plot rankings over time for 2 roller coasters here:

def coaster2name(coaster1,coaster2,dataframe):
  thecoaster1=dataframe[dataframe["Name"].str.contains(coaster1)]
  thecoaster2=dataframe[dataframe["Name"].str.contains(coaster2)]
  ax = plt.gca()
  thecoaster1.plot(kind='line',x='Year of Rank',y='Rank',ax=ax)
  thecoaster2.plot(kind='line',x='Year of Rank',y='Rank',color='red',ax=ax)
  ax.legend([coaster1,coaster2])
  plt.show()
  plt.clf()

#coaster2name("El Toro","Boulder Dash", wdb)

# write function to plot top n rankings over time here:

def topncoasters(n,dataframe):
  coasterselect=dataframe[dataframe["Rank"]<=n]
  coasternames=(coasterselect['Name'].unique())
  arraypandas=[]
  for name in coasternames:
    arraypandas.append(dataframe[dataframe["Name"].str.contains(name)])
  ax = plt.gca()
  for coaster in arraypandas:
    coaster.plot.scatter(x='Year of Rank',y='Rank', marker='o', ax=ax)
  ax.legend(coasternames)
  plt.show()
  plt.clf()

#topncoasters(5, wdb)

plt.clf()

# load roller coaster data here:
ccdb = pd.read_csv('roller_coasters.csv')

#print(ccdb.describe())
#print(ccdb.head())
# write function to plot histogram of column values here:
def plot_histogram(dataframe,column):
  plt.hist(dataframe[column].dropna())
  plt.title('Histogram of Roller Coaster {}'.format(column))
  plt.xlabel(column)
  plt.ylabel('Count')
  plt.show()

#plot_histogram(ccdb, 'speed')
#plt.clf()
#plot_histogram(ccdb, 'length')
#plt.clf()
#plot_histogram(ccdb, 'num_inversions')
#plt.clf()

# write function to plot inversions by coaster at a park here:

def plotinversion(dataframe,name):
  coasters=dataframe[dataframe['park']==name]
  coasters=coasters.sort_values('num_inversions',ascending=False)
  coaster_names=coasters['name']
  number_inversions = coasters['num_inversions']
  plt.bar(range(len(number_inversions)),number_inversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names,rotation=90)
  plt.title('Number of Inversions Per Coaster at {}'.format(name))
  plt.xlabel('Roller Coaster')
  plt.ylabel('# of Inversions')
  plt.show()

plotinversion(ccdb, 'Six Flags Great Adventure')
plt.clf()

# write function to plot pie chart of operating status here:

def pie_chart_status(coaster_df):
  operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
  closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
  num_operating_coasters = len(operating_coasters)
  num_closed_coasters = len(closed_coasters)
  status_counts = [num_operating_coasters,num_closed_coasters,10]
  plt.pie(status_counts,autopct='%0.1f%%',labels=['Operating','Closed','nice'])
  plt.axis('equal')
  plt.show()

pie_chart_status(ccdb)
plt.clf()
# write function to create scatter plot of any two numeric columns here:

def plot_scatter(coaster_df, column_x, column_y):
  plt.scatter(coaster_df[column_x],coaster_df[column_y])
  plt.title('Scatter Plot of {} vs. {}'.format(column_y,column_x))
  plt.xlabel(column_x)
  plt.ylabel(column_y)
  plt.show()

# function to plot scatter of speed vs height
def plot_scatter_height_speed(coaster_df):
  coaster_df = coaster_df[coaster_df['height'] < 140]
  plt.scatter(coaster_df['height'],coaster_df['speed'])
  plt.title('Scatter Plot of Speed vs. Height')
  plt.xlabel('Height')
  plt.ylabel('Speed')
  plt.show()

plot_scatter_height_speed(ccdb)

