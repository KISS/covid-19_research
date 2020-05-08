import pandas as pd
import requests
import json

acs5_base_api_url = "https://api.census.gov/data/2018/acs/acs5/profile?get="

acs5_request_params = {
  'pct_pop_over_65': "DP05_0024PE&for=county:*&in=state:*",
  'pct_pop_using_public_transit': 'DP03_0021PE&for=county:*&in=state:*',
  'pct_pop_uninsured': 'DP03_0099PE&for=county:*&in=state:*',
  'pct_households_below_poverty': 'DP03_0119PE&for=county:*&in=state:*',
  'median_household_income': 'DP03_0062E&for=county:*&in=state:*',
}

pop_est_base_api_url = "https://api.census.gov/data/2019/pep/population?get="

pop_est_request_params = {
  'pop_density': "POP,DENSITY&for=county:*&in=state:*",
}

def process_api_request(base_url, request_params):
  for k in request_params:
    # build API endpoint
    endpoint = base_url + request_params[k]

    # call the API and collect the response
    response = requests.get(endpoint)

    # load the response into a JSON, ignoring the first element which is just field labels
    formattedResponse = json.loads(response.text)[1:]

    # store the response in a dataframe
    if k == 'pop_density':
      df = pd.DataFrame(columns=['population', 'pop_density', 'state', 'county'], data=formattedResponse)
    else:
      df = pd.DataFrame(columns=[k, 'state', 'county'], data=formattedResponse)

    # save dataframe to a CSV spreadsheet
    df.to_csv('../census_data/' + k + '.csv', index=False)

# Request ACS5 data
process_api_request(acs5_base_api_url, acs5_request_params)
# Request Population Estimates data
process_api_request(pop_est_base_api_url, pop_est_request_params)