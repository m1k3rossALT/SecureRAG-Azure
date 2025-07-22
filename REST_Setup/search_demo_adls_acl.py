from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient

# Configuration
search_service_name = "your-search-service-name"
index_name = "rag-index"
endpoint = f"https://{search_service_name}.search.windows.net"

# Use DefaultAzureCredential to support Entra ID (ACL-based) filtering
credential = DefaultAzureCredential()

# Initialize SearchClient using token credential (Entra ID-aware)
client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

# Run search without manual filter; ACLs are enforced automatically if configured in index
results = client.search(
    search_text="architecture",
    select=["metadata_storage_name", "content"]
)

print("\nSearch Results:\n" + "-"*40)
for result in results:
    print(f"Filename: {result['metadata_storage_name']}")
    print(f"Content: {result['content'][:250]}...\n")
