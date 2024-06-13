import requests


def upload_ttl_to_graphdb(ttl_file_path, endpoint):
    headers = {
        "Content-Type": "text/turtle"
    }

    with open(ttl_file_path, 'rb') as file:
        ttl_data = file.read()

    response = requests.post(endpoint, headers=headers, data=ttl_data)

    return response



ontology = 'powerPlant.ttl'
mapped_instances = 'mapped_instances.ttl'
graphdb_url = 'http://localhost:7200'
repo_name = 'my_repo'

endpoint = f"{graphdb_url}/repositories/{repo_name}/statements"
feedback1 = upload_ttl_to_graphdb(ontology, endpoint)
feedback2 = upload_ttl_to_graphdb(mapped_instances, endpoint)

if feedback1:
    print(f"uploaded ontology successfully")
if feedback2:
    print(f"instances uploaded successfully")