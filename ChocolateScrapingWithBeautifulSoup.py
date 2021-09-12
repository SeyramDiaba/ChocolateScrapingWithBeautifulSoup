import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cacao_html = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(cacao_html.content,'html.parser')

#Chocolate ratings distribution
ratings = []
chocolate_ratings = soup.find_all(attrs={'class':'Rating'})

for r in chocolate_ratings[1:]:
  ratings.append(float(r.get_text()))
print(ratings)
plt.hist(ratings)
plt.show()
plt.clf()

company_names = []
companies = soup.find_all(attrs = {'class':'Company'})
#loop through the tags containing company names
for c in companies[1:]:
  company_names.append(c.get_text())
#print(company_names)

cocoa_percentage = []
cocoa = soup.find_all(attrs= {'class':'CocoaPercent'})

for c in cocoa[1:]:
  cocoa_percentage.append(float(c.get_text().strip('%')))  
print(cocoa_percentage)

# dataframe of the best cocoa beans, beans with a rating >= 4


# dataframe with columns, company and ratings and their corresponding lists.
joint_columns = pd.DataFrame.from_dict({'Company Name':company_names,'Ratings':ratings,'CocoaPercentage':cocoa_percentage})
print(joint_columns)
grouped_df = joint_columns.groupby('Company Name').Ratings.mean()
ten_best = grouped_df.nlargest(10)
print(ten_best)

#Scatterplot of ratings vs percentage of cocoa
plt.scatter(joint_columns.CocoaPercentage, joint_columns.Ratings)
plt.show()

#draw a line of best fit
z = np.polyfit(joint_columns.CocoaPercentage, joint_columns.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(joint_columns.CocoaPercentage, line_function(joint_columns.CocoaPercentage), "r--")
plt.show()
plt.clf()

