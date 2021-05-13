# First we will use some open source libraries
from datetime import datetime
import requests
import pandas as pd
import pypyodbc 
import numpy as np
import xlsxwriter

# Get start and end period for API query using the datetime library
now = datetime.now()
end = str(now.year) + "-" + str(now.month).zfill(2)
start = str(now.year - 3) + "-" + str('01')

# Using the URL from the ABS website to make the request. Note that parameters are fed into the URL.
url = 'http://stat.data.abs.gov.au/sdmx-json/data/RT/0.2.01.10.M/all?detail=Full&dimensionAtObservation=AllDimensions&startPeriod=' + start + '&endPeriod=' + end
data = requests.get(url).json()

# This picks up the data
ds = data['dataSets'][0]['observations']
df = pd.DataFrame.from_dict(ds, orient = 'index').reset_index()

# This picks up the month periods
ds1 = data['structure']['dimensions']['observation'][5]['values']
df1 = pd.DataFrame(ds1).reset_index()

combined = pd.concat([df, df1.reindex(df1.index)], axis=1).drop(['index',1,2],axis=1)

print(combined)

