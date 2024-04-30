from cProfile import label
import pandas as pd
import json
import jsonschema
from jsonschema import validate
# Fields,Datatype,Label,Detailed Description,Analytic Category,Chart Suggestion
def get_col_props(col):
    return {
        "Name" : col['Fields'],
        "Type" : col['Datatype'],
        "Comment" : col['Detailed Description'],
    }
# Read the CSV file
df = pd.read_csv('performance_fields.csv')
cols = df.to_dict('records')


# Generate the schema
schema = [ get_col_props(row) for row in cols ]


# Write the schema to a JSON file
with open('performance_fields.json', 'w') as f:
    json.dump(schema, f)