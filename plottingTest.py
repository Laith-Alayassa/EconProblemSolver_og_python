import csv

import numpy as np
import pandas as pd
from matplotlib import  pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')
# plt.xkcd()
# print(plt.style.available)


data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,
         popularity,
        color = '#231359')

plt.title('Most popular languages')






# # Median Developer Salaries by Age
# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#
# x_indexes = np.arange(len(ages_x))
# width = 0.25
#
# # Median JavaScript Developer Salaries by Age
# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
#
# plt.bar(x_indexes - width,
#          js_dev_y,
#          label = 'JS-developers',
#          linewidth = 3,
#         width = width)
#
#
# # Median Python Developer Salaries by Age
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
#
# plt.bar(x_indexes, py_dev_y,
#          label = 'python devs',
#          linewidth = 3,
#         width = width)
#
#
#
#
# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
#
# plt.bar(x_indexes + width,
#          dev_y,
#          color = '#444444',
#          linestyle = '--' ,
#          label = 'all devs',
#         width = width)
#
# plt.xticks(ticks= x_indexes, labels=ages_x)
#
#
# plt.title('median salary (by age)')
# plt.xlabel('ages')
# plt.ylabel('median salary')
# plt.legend()
#
# plt.tight_layout()

plt.show()


