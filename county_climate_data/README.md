# COVID-19 Research Project

The objective of this project was to uncover insights from COVID-19 case data and build machine learning models to help provide a clearer picture of what was happening in the United States at the start of 2020.

The data collected spans from January 21st 2020 to April 30th 2020. Four models were built, using supervised learning methods, each answering one of the questions posed below:

1. If a state imposes a stay-at-home or shelter-in-place intervention, can I predict whether a county in that state will see a less than 30% increase in week-on-week COVID-19 case counts within 3-weeks of intervention?
2. If a state imposes a stay-at-home or shelter-in-place intervention, can I predict whether a county in that state will see a 100% decrease in weekly case counts from week 2 to week 3, post-intervention?
3. Can I predict whether a state will implement stay-at-home or shelter-in-place intervention?
4. Can I predict whether there is a greater than 5% chance of dying in a U.S county if diagnosed COVID-19 positive?

County-level demographic, weather, and COVID-19 case data for the contiguous United States, Alaska, and Hawaii was used to build each model. This data was collected from several sources, including the Census Bureau API ([ACS 5-year](https://www.census.gov/data/developers/data-sets/acs-5year.html) and [County Population Totals](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html)), The National Conference of State Legislatures ([2020 State & Legislative Partisan Composition](https://www.ncsl.org/Portals/1/Documents/Elections/Legis_Control_2020_April%201.pdf)), National Centers for Environmental Information ([NOAA](https://www.ncei.noaa.gov/resources)), and the NYTimes ([Coronavirus (Covid-19) Data in the United States](https://github.com/nytimes/covid-19-data) and [State Closing/Reopening Schedules](https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html)).

Overall, all models showed some predictive capability and would likely improve if provided with more county-level demographic data. The best performing model was the one for predicting whether a state would impose a stay-at-home or shelter-in-place intervention, which identified the political party of a state governor as a key indicator (if the state governor is a Democrat, an intervention is highly likely to be imposed).

The models for Questions 1, 2, and 4 were built using k-Nearest Neighbors (kNN). kNN is a supervised learning algorithm where you assign a value for ​k​, which determines the number of neighbors the algorithm evaluates when calculating the classification of an unseen data point. The algorithm will assign the unseen data point the classification of the majority (the class assigned to the majority of its neighbors).

The model for Question 3 was built using a decision tree (aka CART), a supervised learning algorithm that selects features that will produce subsets of the original dataset (or data in the parent node) containing less noise or entropy (the number of observations that have different classifications). This process is done repeatedly until the subsets of data can’t be separated any further.

## How I built my models

I used SQL, Python, Excel, Postman, Azure Data Studio, and Visual Studio Code as tools for collecting, visualizing, pre-processing, and merging the different data sources I needed. I also used SQL to output the final datasets I used to build my models.

There was a lot of data wrangling involved since I was using data sources managed by different companies/organizations. An example of this is my having to create a mapping of NOAA climdiv state codes to corresponding FIPS codes ([viewable here](https://github.com/KISS/covid-19_research/blob/master/county_climate_data/climdiv_fips_mapping.csv)), in order to be able to join monthly temperature data with its corresponding state.

I used [Weka](https://www.cs.waikato.ac.nz/ml/weka/) to convert my datasets from CSV to the format supported by Weka (.arff) and to build my different models. Weka isn't my preferred tool but it was the tool required by my professor.

For model selection I analyzed each model's Confusion Matrix and ROC area.

## Full Report
https://github.com/KISS/covid-19_research/blob/master/CS619%20-%20COVID-19%20Research%20Report.pdf

## Decision Tree output by Model 3

Model 3 answered: "Can I predict whether a state will implement stay-at-home or shelter-in-place intervention?"

![Decision Tree showing that a governors political party is a good indicator of whether a state will impose a stay-at-home intervention to combat coronavirus or not](https://github.com/KISS/covid-19_research/blob/master/q3_model_decision_tree.png?raw=true)

The image is also viewable at https://github.com/KISS/covid-19_research/blob/master/q3_model_decision_tree.png?raw=true