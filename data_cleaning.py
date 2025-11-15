# neha changes 

# Industry 
def clean_data(df):
  
  industry_groups = {
    'Industrials': 0,
    'Materials': 1, 
    'CommunicationServices': 2, 
    'Transport': 3,
    'InformationTechnology': 4,
    'Financials': 5,
    'Energy': 6,
    'Real Estate': 7,
    'Utilities': 8,
    'ConsumerDiscretionary': 9,
    'Education': 10,
    'ConsumerStaples': 11,
    'Healthcare': 12,
    'Research': 13
  }

  df["Industry_number"] = [industry_groups[x] for x in df["Industry"]]

  # Ethinicy 
  ethnicity_groups = {
      'White': 0,
      'Black': 1, 
      'Asian': 2, 
      'Latino': 3,
      'Other': 4
                      
  }
  
  df["Ethnicity_number"] = [ethnicity_groups[x] for x in df["Ethnicity"]]

  # Citizen
  citizen_groups = {
      'ByBirth': 0,
      'ByOtherMeans': 1,
      'Temporary': 2         
  }

  df["Citizen_number"] = [citizen_groups[x] for x in df["Citizen"]]

  return df

df_clean = clean_data(df_application)
df_clean.head()
