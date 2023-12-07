# import modules
import openai, json, requests, tiktoken, pypdf

from datetime import datetime as dt

import modules.config as cfg
import modules.functions as fn
import modules.prompts as pr

# define important variables
reviewDoc = ""
promptTopic = ""

outputTracking = {}
outputTracking[ "Pages" ] = {}

openai.api_type = cfg.aoaiApiType
openai.api_base = cfg.aoaiEndpoint
openai.api_version = cfg.aoaiApiVersion
openai.api_key = cfg.aoaiApiKey

# Track Start and End Times
print( "Start Time: ", dt.now() )

print( "End Time: ", dt.now() )