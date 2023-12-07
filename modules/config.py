# Assumption : Azure OpenAI is being used
aoaiEndpoint = ""
aoaiApiKey = ""
aoaiModel = "" # GPT-4 model, ideally 32K for larger JSON documents
aoaiEmbeddingModel = ""
aoaiApiType = "azure"
aoaiApiVersion = "2023-08-01-preview"

# Provides capability to write document embeddings to Azure AI Search 'Vector' Index
searchEndpoint = ""
searchKey = ""
searchVectorIndex = ""

# optional configuration options
maxTokens = 1000
temp = 0.5
