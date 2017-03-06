import requests
import carto
import json
import pandas as pd
from urllib.parse import urlencode
import io


account_name = 'stuartlynn'
def sql(query,format='csv'):

    url = 'https://stuartlynn.carto.com/api/v2/sql?'
    params = {'q':query, 'format' : format}
    response = requests.get(url + urlencode(params))
    if format=='geojson':
        response = response.json()
    else:
        print(response.text)
        output = io.StringIO(response.text)
        response = pd.read_csv(output)
    return response

def get_state_list():
    return sql('select distinct(state_name) from levi_districts_since_1948')

def get_state_data():
    pass



for state in get_state_list()['state_name']:
    print(state)

    state_data = sql('select * from levi_districts_since_1948 where state_name=\'{0}\''.format(state), format='geojson')
    with open('geojsons/full_res/{0}.geojson'.format(state),'w') as f:
        f.write(json.dumps(state_data))

    columns = ",".join(state_data['features'][0]['properties'].keys())
    state_data = sql('select ST_SimplifyPreserveTopology(the_geom, 0.001) as the_geom, {columns} from levi_districts_since_1948 where state_name=\'{state}\''.format(state=state, columns=columns), format='geojson')
    with open('geojsons/simplified_0.01/{0}.geojson'.format(state),'w') as f:
        f.write(json.dumps(state_data))

