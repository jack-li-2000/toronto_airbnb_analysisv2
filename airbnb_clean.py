import pandas as pd
import swifter

cal1 = pd.read_csv('data/calendar_11_2022.csv')
lis1 = pd.read_csv('data/listings_11_2022.csv')

cal2 = pd.read_csv('data/calendar_03_2023.csv')
lis2 = pd.read_csv('data/listings_03_2023.csv')

cal3 = pd.read_csv('data/calendar_06_2023.csv')
lis3 = pd.read_csv('data/listings_06_2023.csv')

cal4 = pd.read_csv('data/calendar_09_2023.csv')
lis4 = pd.read_csv('data/listings_09_2023.csv')

clean_cal1 = cal1.drop('maximum_nights',axis=1)
clean_cal1['date'] = cal1.date.swifter.apply(pd.to_datetime)

clean_cal2 = cal2.drop('maximum_nights',axis=1)
clean_cal2['date'] = cal2.date.swifter.apply(pd.to_datetime)

clean_cal3 = cal3.drop('maximum_nights',axis=1)
clean_cal3['date'] = cal3.date.swifter.apply(pd.to_datetime)

clean_cal4 = cal4.drop('maximum_nights',axis=1)
clean_cal4['date'] = cal4.date.swifter.apply(pd.to_datetime)

splice_date_1 = clean_cal2.date[0]
splice_date_2 = clean_cal3.date[0]
splice_date_3 = clean_cal4.date[0]

clean_cal1 = clean_cal1[clean_cal1['date'] < splice_date_1]
clean_cal2 = clean_cal2[clean_cal2['date'] < splice_date_2]
clean_cal3 = clean_cal3[clean_cal3['date'] < splice_date_3]
clean_cal4 = clean_cal4[clean_cal4['date'] < pd.to_datetime('2023-11-01')]

clean_cal = pd.concat([clean_cal1, clean_cal2, clean_cal3, clean_cal4], ignore_index=True)

lis = pd.concat([lis1, lis2, lis3, lis4], ignore_index=True)
lis = lis.drop_duplicates(subset=['id'],keep='last')

lis = lis[['id','room_type','accommodates','beds','bedrooms','price','number_of_reviews',
           'review_scores_rating','review_scores_accuracy','review_scores_cleanliness',
           'review_scores_location','review_scores_checkin','review_scores_location','neighbourhood_cleansed']]

clean_cal.to_csv('cleaned_data/clean_cal.csv')
lis.to_csv('cleaned_data/clean_lis.csv')

