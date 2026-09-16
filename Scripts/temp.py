from databricks.connect import DatabricksSession

# Connect to your Databricks cluster
spark = DatabricksSession.builder.profile("DEFAULT").getOrCreate()
# spark = DatabricksSession.builder.remote(cluster_id="0901-204909-94tx7p97").getOrCreate()
spark.sql("SELECT 1").show()
