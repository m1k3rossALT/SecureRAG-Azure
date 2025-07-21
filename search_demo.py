from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Replace these with your values
search_service_name = "search_service_name"
index_name = "index_name"
api_key = "api_key"  # From Azure Search -> Keys

# Build endpoint
endpoint = f"https://{search_service_name}.search.windows.net"

# Initialize client
client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(api_key))

# Set group_id for filtering (e.g., Engineering or Finance)
user_group = "Engineering"

# Run search with filter
results = client.search(search_text="architecture",  # search keyword
                        filter=f"group_ids eq '{user_group}'",
                        select=["metadata_storage_name", "content"])

# Print results
print("\nSearch Results:\n" + "-"*40)
for result in results:
    print(f"Filename: {result['metadata_storage_name']}")
    print(f"Content: {result['content'][:250]}...\n")
