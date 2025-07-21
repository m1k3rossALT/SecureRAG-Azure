# SecureRAG-Azure

A lightweight demo project that implements Retrieval-Augmented Generation (RAG) with document-level access control using Microsoft Azure services.

## 🔐 Key Features

- ✅ Secure document storage using Azure Blob Storage (ADLS Gen2)
- ✅ Document-level access via Entra ID group-based filtering
- ✅ Search powered by Azure AI Search
- ✅ Retrieval and filtering using Python SDK
- ✅ RAG-ready architecture (retrieval + LLM prompt-ready)

## 🧱 Tech Stack

- Microsoft Entra ID (formerly Azure AD)
- Azure Blob Storage (ADLS Gen2)
- Azure AI Search
- Azure OpenAI (optional for final generation)
- Python (azure-search-documents, azure-core)

## 📂 Project Structure

SecureRAG-Azure/
├── search_demo.py # Python script for filtered document search
├── doc1.txt # Sample document (Finance)
├── doc2.txt # Sample document (Engineering)
├── README.md # Project overview


## 🚀 How It Works

1. Upload documents to Azure Blob Storage with metadata:
   - e.g., `group_ids = Engineering`

2. Index documents in Azure AI Search with metadata extracted

3. In Python:
   - Authenticate with Azure AI Search
   - Apply a metadata filter based on user's group (e.g., `group_ids eq 'Engineering'`)
   - Retrieve matching document content

4. (Optional) Feed retrieved content to Azure OpenAI for LLM-based answers

## 🛡️ Access Control Strategy

Document-level access is enforced using `group_ids` metadata tags on blobs. Users are filtered into relevant content areas based on their Entra ID group membership.

## 📦 Requirements

```bash
pip install azure-core azure-search-documents


🧪 Sample Query Output
Search Results:
----------------------------------------
Filename: doc2.txt
Content: Title: Microservice Deployment Architecture - Engineering...

📄 License
This project is for personal and educational use only.

