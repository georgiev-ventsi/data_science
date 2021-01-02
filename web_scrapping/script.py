from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, 'html.parser')
# print(soup)

rating_data = soup.find_all(attrs={"class": "Rating"})
ratings = []
for rating in rating_data[1:]:
  ratings.append(float(rating.string))
# print(ratings)

plt.hist(ratings)
plt.show()

company_data = soup.select('.Company')
companies = []
for company in company_data[1:]:
  companies.append(company.string)
# print(companies)

dict = {"Company": companies, "Ratings": ratings}
cacao_df = pd.DataFrame.from_dict(dict)
# print(cacao_df.head())

mean_vals = cacao_df.groupby("Company").Ratings.mean()
ten_best = mean_vals.nlargest(10)
# print(ten_best)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
 
for td in cocoa_percent_tags[1:]:
  percent = int(float(td.get_text().strip('%')))
  cocoa_percents.append(percent)
# print(cocoa_percents)

cacao_df['CocoaPercentage'] = cocoa_percents
cacao_df.head()
plt.scatter(cacao_df.CocoaPercentage, cacao_df.Ratings)
plt.show()
plt.clf()

z = np.polyfit(cacao_df.CocoaPercentage, cacao_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cacao_df.CocoaPercentage, line_function(cacao_df.CocoaPercentage), 'r--')
plt.show()
