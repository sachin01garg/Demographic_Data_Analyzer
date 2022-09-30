import pandas as pd
from collections import Counter

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =df['race'].value_counts()

    # What is the average age of men?
    all_males=df['sex']=='Male'
    age_of_males=df['age'].where(all_males)
    average_age_men = round(float(age_of_males.mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors=df['education']=='Bachelors'
    total_bachelors=df['education'].where(bachelors).dropna().count()
    percentage_bachelors = round(total_bachelors/df['education'].count() * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    more_50k=df['salary'] == '>50K'
    with_adavance=(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    without_adavance=~(df['education']=='Bachelors') & ~(df['education']=='Masters') & ~ (df['education']=='Doctorate')
    
    high_education=df['education'].where(with_adavance).dropna().count()
    low_education=df['education'].where(without_adavance).dropna().count()

    # percentage with salary >50K
    higher_education_rich = round(df['education'].where(more_50k &         
                            with_adavance).count()/high_education * 100,1)
    lower_education_rich = round(df['education'].where(more_50k & 
                           without_adavance).count()/low_education * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    sal_50k=df['salary']=='>50K'
    min_hour_sal=df[(df['hours-per-week']==min_work_hours) & sal_50k] 
    total_hour= len(df[(df['hours-per-week'] == min_work_hours)].index)

    rich_percentage = len(min_hour_sal) / total_hour * 100

    # What country has the highest percentage of people that earn >50K?
    earn_50k= df[df['salary']=='>50K'].dropna()
    country_50k=Counter(list(earn_50k['native-country'].dropna()))
    country=Counter(list(df['native-country']))
    new_dict={}
    for key in country.keys():
      new_dict[key]=round(country_50k[key]/country[key] *100,1)
    MAX=max(new_dict.values())
    for key in new_dict.keys():
      if new_dict[key]== MAX:
           country_name=key  
    highest_earning_country = country_name
    highest_earning_country_percentage = MAX 

    # Identify the most popular occupation for those who earn >50K in India.
    india_50k= df[(df['native-country']=='India') & (df['salary']=='>50K')]
    top_IN_occupation=india_50k['occupation'].value_counts().idxmax()
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
