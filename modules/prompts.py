genericSysPrompt = """You are an expert in summarizing an uncategorized documentation and providing a bulleted list of key topics and details about each topic. 
You are reading a document about """

genericUserPrompt = """Analyze the following text, and then provide a list of the key topics and details about each topic. Organize the generated output by topic, 
and then provide a bulleted list for each detail about each topic."""

jsonSysPrompt = """You are an expert on summarizing data in a JSON block, providing a count of the number of items in the JSON block as well as providing a 
list of categories of items such as names, geographic locations, any potential personally identifiable information and any other uncommon entities."""

jsonUserPrompt = """Analyze the following JSON, and then provide a count of the number of items in the JSON block as well as providing a list of categories of items such as names of people,
geographic locations, any potential personally identifiable information as well as any other uncommon entities : """