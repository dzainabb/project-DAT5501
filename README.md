DAT5501 – Fertility Rates and Female Employment Analysis
Project Overview
This project investigates the relationship between female labour force participation and fertility rates across countries using international demographic and socioeconomic data. The analysis combines classical statistical techniques with machine learning methods to evaluate whether female employment is linearly associated with fertility, and to explore broader structural drivers of fertility outcomes.
The work was developed as part of the DAT5501: Analysis, Software and Career Practice module portfolio and is intended to demonstrate applied data analysis, validation, documentation, and professional repository curation.


Research Question
Is female labour force participation associated with lower fertility rates across countries, and to what extent does this relationship explain global fertility variation?

Data Sources
All data used in this project is publicly available and aggregated at country level:
Fertility rates:
Our World in Data – UN fertility estimates
https://ourworldindata.org/grapher/children-per-woman-un
Female labour force participation:
Our World in Data
https://ourworldindata.org/grapher/female-labor-force-participation-rates
GDP per capita (current US$):
World Bank
https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
Urban population share:
World Bank
https://data.worldbank.org/indicator/SP.URB.GROW

Methods
Data cleaning & validation using Python, unittest, and pytest
Linear regression to test the primary hypothesis
Polynomial time-series modelling (UK) with BIC for model selection
Decision tree classifier and regressor to capture non-linear relationships

Repository Structure
project-DAT5501/
├── data/
├── src/
├── tests/
├── data_cleaning.py
├── decision_tree.png
├── requirements.txt
└── README.md
Quality assurance
Data processing and analysis code are validated using unit tests implemented with pytest, and continuous integration is configured via CircleCI to automatically run tests on each commit, ensuring reproducibility and code reliability.
CIRCLECI - https://app.circleci.com/organization/github/dzainabb


