Just a quick reference sheet for using the pandas library for Python, in both py and jupyter. With thanks to StackOverflow for their survey respondent data 2024, and to Companies House for the use of their UK companies dataset.

This repo uses:
- Python v3 (I am using 3.12.1)
    - jupyterlab (I am using v4.1.5)
    - pandas (I am using v2.2.0)

I recommend installing and running Jupyter Notebook to explore the data with pandas.

You can start Jupyter Notebook by installing Jupyter globally, and then running `jupyter notebook` to initiate in the browser. Then use the browser window to open the notebook or start a new one.

The first file is pandas_reference.py / .ipynb which contains a list of references to popular functions and basic useage of the pandas framework

The second file is pandas_example.py / .ipynb which uses the pandas framework to examine Companies House (UK Companies) data

You can download the data for this yourself using this link ([Companies House](https://download.companieshouse.gov.uk/en_output.html)) which I downloaded to this directory location `example-data/CompaniesHouse-BasicCompanyData.csv`

I exported the final subset data to `example-data/CompaniesHouses-target-companies.csv`
