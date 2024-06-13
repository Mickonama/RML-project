from pyrml import RMLConverter

converter = RMLConverter()
print("RML mapping initiated...")
rdf = converter.convert('mapper.rml')

rdf.serialize(destination="mapped_instances.ttl")
print("RML mapping completed!")
print("Mapped instances saved as mapped_instances.ttl")
