# import modules
import openai, json, requests, tiktoken, pypdf

from datetime import datetime as dt

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter

import modules.config as cfg
import modules.functions as fn

# define important variables
# reviewDoc = "./docx/az104-trainer-handbook.pdf"
# promptTopic = "the Microsoft AZ-104 certification exam."
reviewDoc = "./docx/linux4pros.pdf"
promptTopic = "commands in the Linux Operating System used by Linux Professionals."

outputTracking = {}
outputTracking[ "Pages" ] = {}

openai.api_type = cfg.aoaiApiType
openai.api_base = cfg.aoaiEndpoint
openai.api_version = cfg.aoaiApiVersion
openai.api_key = cfg.aoaiApiKey

userPrompt = """Analyze the following text, and then provide a list of the key topics and details about each topic. Organize the generated output by topic, 
and then provide a bulleted list for each detail about each topic"""

systemPrompt = """You are an expert in summarizing technical documentation and providing a bulleted list of key topics and details about each topic. 
You are reading a technical document about """ + promptTopic

# Track Start and End Times
print( "Start Time: ", dt.now() )

# load document 
fileLoader = PyPDFLoader( reviewDoc )
pageCollection = fileLoader.load_and_split()

# for testing - limit x pages
'''
testCount = 1
counter = 0

while counter <= testCount :

    page = pageCollection[ counter ]

'''
# loop through page collection
for page in pageCollection :

    # print( page.page_content )
    # print( page.metadata[ "page" ] )

    pageId = page.metadata[ "page" ]

    promptItem = userPrompt + ":" + str( page.page_content )
    
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

    # print( response )
    # print( response[ "choices" ] )
    # print( "Response: ", response[ "choices"][ 0 ][ "message" ][ "content" ] )

    outputTracking[ pageId ] = ( response[ "choices"][ 0 ][ "message" ][ "content" ] )

    # used when testing loop is utilized
    # counter += 1

print( outputTracking )
print( "End Time: ", dt.now() )