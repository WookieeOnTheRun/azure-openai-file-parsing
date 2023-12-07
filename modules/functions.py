import openai, json, requests, tiktoken, pypdf

import docx, pptx, xlwings

from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter

import modules.config as cfg
import modules.prompts as pr

# generate completion from provided model deployment
def fnGenerateCompletions( pageDict ) :

    outputTracking = {}

    for key, item in pageDict.items() :

        for pageData in item :

            pageId = pageData[ 0 ]
            page = pageData[ 1 ]

            promptItem = pr.genericUserPrompt + ":" + str( page )
    
            response = openai.ChatCompletion.create(
                engine = cfg.aoaiModel ,
                messages =  [
                {
                    "role" : "system" ,
                    "content" : pr.genericSysPrompt
                },{
                    "role" : "user" ,
                    "content" : promptItem
                }],
                    temperature = cfg.temp,
                    max_tokens = cfg.maxTokens,
                    top_p = 0.95,
                    frequency_penalty = 0,
                    presence_penalty = 0,
                    stop = None
                )

            # print( response )
            # print( response[ "choices" ] )
            # print( "Response: ", response[ "choices"][ 0 ][ "message" ][ "content" ] )

            outputTracking[ pageId ] = ( response[ "choices"][ 0 ][ "message" ][ "content" ] )

    print( outputTracking )

    return outputTracking

# determine file type
def fnGetFileType( file ) :

    # regardless of location, assumption is final character(s) are ".xxx(x)"

    fileExt = ( file.split( "." ) )[ -1 ]

    return fileExt

# ingest file and pass content to LLM
def fnIngestFile( file ) :

    pageTracker = {}
    pageTracker[ file ] = []

    fileExt = fnGetFileType( file )

    if fileExt.upper() == "PDF" :

        fileLoader = PyPDFLoader( file )
        pageCollection = fileLoader.load_and_split()

        for page in pageCollection :

            # print( page.page_content )
            # print( page.metadata[ "page" ] )

            pageId = page.metadata[ "page" ]
            pageContent = page.page_content

            pageJson = {
                pageId : pageContent
            }

            pageTracker[ file ].append( pageJson )

    elif fileExt.upper() in [ "TXT", "CSV", "JSON", "XML" ] :

        idx = 1

        with open( file, "r" ) as rawFile :

            fileImport = rawFile.read()

            # print( fileImport )

            pageJson = {
                idx : fileImport
            }

            pageTracker[ file ].append( pageJson )

    elif fileExt.upper() in [ "DOC", "DOCX", "PPT", "PPTX", "XLS", "XLSX" ] :

        # do something with Office Docs

    if len( pageTracker.keys() ) > 0 :

        outputDict = fnGenerateCompletions( pageTracker )

    # connect to Vector Index in AI Search and write embeddings

    client = SearchClient( cfg.searchEndpoint, cfg.searchVectorIndex, AzureKeyCredential( cfg.searchKey ) )