'''this program displays the number of covid cases per dates according to the country
in a scatter plot '''
#import the modules
import pandas 
file = pandas.read_csv('data.csv') #read the file as a dataframe
fig = px.scatter(file,x='date',y='cases',color='country')
fig.show()