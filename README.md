🏙️ Toronto Airbnb Analysis

📌 Project Overview

This project is a revised and expanded analysis of Airbnb listings in Toronto, Ontario, Canada. It builds on my original work with:

* More complete datasets from multiple time periods
* Improved data cleaning and preprocessing
* Enhanced visualizations for deeper insights
* Interactive Tableau dashboards for exploration

Data was sourced from https://insideairbnb.com/toronto/ for November 2022, March 2023, June 2023, and September 2023.

🎯 Objective & Hypothesis

Objective: To explore trends in Toronto’s Airbnb market over time, identify factors influencing listing prices, and assess the potential impact of seasonality and neighbourhood characteristics.

Hypothesis:

* Location (proximity to downtown and tourist attractions) is a primary driver of nightly rates.
* Seasonality significantly affects both pricing and availability, with summer months showing higher demand and prices.
* Property type (entire home vs. private/shared room) has a measurable impact on occupancy rates and revenue potential.

🛠 Methods & Workflow
1. Data Collection

* Downloaded datasets from Inside Airbnb for four time points across 2022–2023.
* Included listings, calendar availability, and reviews data.

2. Data Cleaning & Preprocessing

Used airbnb_clean.py to:

* Remove duplicates and inactive listings
* Standardize column names and formats
* Handle missing values
* Convert date and price fields to usable formats

3. Exploratory Data Analysis (EDA)

Conducted in airbnb_TO_anal.ipynb using Python (Pandas, NumPy, Matplotlib, Seaborn).

Key steps:

* Summary statistics
* Price distribution analysis
* Geospatial mapping of listings
* Time-series trends in availability and pricing

4. Visualization

Created static plots in Python for quick insights.

Built interactive Tableau dashboards (airbnb_toronto.twb) for dynamic filtering by:

* Neighbourhood
* Property type
* Time period

5. Statistical Testing

* Correlation analysis between price and features (location, reviews, property type).
* Seasonal comparison using grouped means and variance analysis.

📊 Key Findings & Conclusion

* Location Matters Most Listings in downtown Toronto and near major attractions consistently command higher nightly rates.
* Seasonality is Real Summer months (June–September) show a clear spike in both prices and occupancy rates, supporting the seasonality hypothesis.
* Property Type Drives Revenue Potential Entire homes/apartments have higher average prices but also higher occupancy compared to private rooms.
* Market Growth & Saturation The number of active listings increased slightly over the year, but competition in certain neighbourhoods has started to stabilize prices.

Conclusion: 

Toronto’s Airbnb market is shaped by a combination of location, seasonality, and property type. Hosts can optimize revenue by adjusting pricing strategies seasonally and targeting high-demand neighbourhoods. Policymakers can use these insights to monitor short-term rental impacts on housing availability.

📂 Repository Structure
Code

├── cleaned_data/                # Processed datasets
├── data/                        # Raw datasets from Inside Airbnb
├── airbnb_TO_anal.ipynb          # Main analysis notebook
├── airbnb_clean.py               # Data cleaning script
├── airbnb_toronto.twb            # Tableau dashboard file
├── notes.txt                     # Project notes
└── README.md                     # Project documentation

📈 Tools & Technologies

Python: Pandas, NumPy, Matplotlib, Seaborn
Tableau: Interactive dashboards
Jupyter Notebook: EDA and statistical analysis
