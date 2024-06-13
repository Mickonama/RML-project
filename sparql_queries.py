import pandas as pd
import requests


def run_sparql_query(endpoint, query):
    headers = {
        "Accept": "application/sparql-results+json, application/json"
    }

    params = {
        "query": query
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        results = data['results']['bindings']
        df = pd.DataFrame(
            [{var: binding[var]['value'] if var in binding else None for var in data['head']['vars']} for binding in
             results])
        return df
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return pd.DataFrame()



graphdb_url = 'http://localhost:7200'
repo_name = 'my_repo'
endpoint = f"{graphdb_url}/repositories/{repo_name}"
query1 = """
PREFIX ppl:  <http://powerplant.example.com/schema/>

select DISTINCT ?country ?gdp where {
    ?country ppl:hasPlant ?plant.
    ?country ppl:GDP ?gdp.
    ?plant ppl:primary_fuel "Solar".
} 
"""

results1 = run_sparql_query(endpoint, query1)
print(results1)
results1.to_csv('sparql_results/query1_results.csv')

query2 = """
PREFIX ppl:  <http://powerplant.example.com/schema/>

select ?continent (sum(?gdp) as ?continent_GDP) (sum(?pop) as ?continent_population) (?continent_GDP/?continent_population as ?per_capita_GDP) where {
	?continent ppl:contains ?country.
    ?continent a ppl:Continent.
    ?country a ppl:Country.
	?country ppl:GDP ?gdp.
	?country ppl:population ?pop.
    
} GROUP BY ?continent ORDER BY DESC(?per_capita_GDP)
"""

results2 = run_sparql_query(endpoint, query2)
print(results2)
results2.to_csv('sparql_results/query2_results.csv')

query3 = """
PREFIX ppl:  <http://powerplant.example.com/schema/>

select ?country (count(?plant) as ?total_power_plants) (sum(?cap) as ?total_capacity_MW)where {
    ?country ppl:hasPlant ?plant.
    ?plant ppl:capacity ?cap.
    
} GROUP BY ?country ORDER BY DESC(?total_power_plants)
"""

results3 = run_sparql_query(endpoint, query3)
print(results3)
results3.to_csv('sparql_results/query3_results.csv')