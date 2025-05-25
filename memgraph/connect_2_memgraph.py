from neo4j import GraphDatabase
 
# Define correct URI and AUTH arguments (no AUTH by default)
URI = "bolt://localhost:7687"
AUTH = ("", "")
 
with GraphDatabase.driver(URI, auth=AUTH) as client:
    # Check the connection
    client.verify_connectivity()
 
    # Create a user in the database
    records, summary, keys = client.execute_query(
        "CREATE (u:User {name: $name, password: $password}) RETURN u.name AS name;",
        name="John",
        password="pass",
        database_="memgraph",
    )
 
    # Get the result
    for record in records:
        print(record["name"])
 
    # Print the query counters
    print(summary.counters)
 
    # Find a user John in the database
    records, summary, keys = client.execute_query(
        "MATCH (u:User {name: $name}) RETURN u.name AS name",
        name="John",
        database_="memgraph",
    )
 
    # Get the result
    for record in records:
        print(record["name"])
 
    # Print the query
    print(summary.query)