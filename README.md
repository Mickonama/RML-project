# RML-project
Mapping instances in RML and uploading them to graphDB with automated python scripts

## Description of each file:

mapper.rml -> File containing the RML rules

powerPlant.ttl -> The ontology in turtle format

mapped_instances -> The output of the RML file

gdb_automation.py -> A script for connecting to a GraphDB repository and uploading the ontology and mapped instances .ttl files

rmlConverter.py -> Script for converting the RML rules to RDF triplets

sparql_queries.py -> Script for running SPARQL queries after connecting to a graphDB repository

complete_rml_pipeline.py -> The script that automates the whole process. Performs RML mapping, connects to graphDB repository and executes the SPARQL queries


## How to run

Simply run the complete_rml_pipeline.py script
