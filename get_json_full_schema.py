from cProfile import label
import pandas as pd
import json
import jsonschema
from jsonschema import validate
# Fields,Datatype,Label,Detailed Description,Analytic Category,Chart Suggestion
def get_col_props(col):
    col_dict = {
        col["Fields"]: {
            "Type": col["Datatype"],
            "Comment": col["Detailed Description"]
        }
    }   
    x = json.dumps(col_dict)
    return(x)

# Read the CSV file
df = pd.read_csv('performance_fields.csv')
cols = df.to_dict('records')


# Generate the schema
properties = [get_col_props(row) for row in cols]

schema_dict = {
    "title" : "PerformanceSchema", 
    "type" : "object", 
    "properties" :  ','.join(properties) 
}

print(schema_dict)
# Write the schema to a JSON file
with open('performance_schema.json', 'w') as f:
    json.dump(schema_dict, f)