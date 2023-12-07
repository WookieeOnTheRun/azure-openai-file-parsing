# import modules
import openai, json, requests, tiktoken, pypdf

from datetime import datetime as dt

import modules.config as cfg
import modules.functions as fn
import modules.prompts as pr

# define important variables
reviewDocs = [ "" ]
promptTopic = ""

openai.api_type = cfg.aoaiApiType
openai.api_base = cfg.aoaiEndpoint
openai.api_version = cfg.aoaiApiVersion
openai.api_key = cfg.aoaiApiKey

# Track Start and End Times
print( "Start Time: ", dt.now() )

for file in reviewDocs :

    docOutput = fn.fnIngestFile( file )

print( "End Time: ", dt.now() )