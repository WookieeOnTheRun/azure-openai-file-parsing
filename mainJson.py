# import modules
import openai, json, requests

from datetime import datetime as dt

import modules.config as cfg
import modules.functions as fn

# define important variables
reviewDoc = ""

openai.api_type = cfg.aoaiApiType
openai.api_base = cfg.aoaiEndpoint
openai.api_version = cfg.aoaiApiVersion
openai.api_key = cfg.aoaiApiKey

systemPrompt = """You are an expert on summarizing data in a JSON block, providing a count of the number of items in the JSON block as well as providing a 
list of categories of items such as names, geographic locations, any potential personally identifiable information and any other uncommon entities."""

userPrompt = """Analyze the following JSON, and then provide a count of the number of items in the JSON block as well as providing a list of categories of items such as names of people,
geographic locations, any potential personally identifiable information as well as any other uncommon entities : """

# Track Start and End Times
print( "Start Time: ", dt.now() )

# load document 
with open( reviewDoc, "r" ) as rawJson :

    fileImport = rawJson.read()

    # print( fileImport )

    promptItem = userPrompt + ":" + fileImport
    
    response = openai.ChatCompletion.create(
        engine = cfg.aoaiModel ,
        messages =  [
            {
                "role" : "system" ,
                "content" : systemPrompt
            },{
                "role" : "user" ,
                "content" : promptItem
            }
        ],
        temperature = 0.5,
        max_tokens = 1000,
        top_p = 0.95,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = None
    )

    print( response )
    # print( response[ "choices" ] )
    # print( "Response: ", response[ "choices"][ 0 ][ "message" ][ "content" ] )

print( "End Time: ", dt.now() )
