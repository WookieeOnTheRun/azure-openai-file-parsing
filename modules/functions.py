import json, openai, requests, pypdf

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter

import modules.config as cfg
import modules.prompts as pr

# generate completion from provided model deployment
def fnGenerateMultiPageCompletions( pageId, page ) :

    outputTracking = {}

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

def fnIngestFile( file ) :

    fileExt = fnGetFileType( file )

    if fileExt.upper() == "PDF" :

        pageTracker = {}

        fileLoader = PyPDFLoader( file )
        pageCollection = fileLoader.load_and_split()

        for page in pageCollection :

            # print( page.page_content )
            # print( page.metadata[ "page" ] )

            pageId = page.metadata[ "page" ]
            pageContent = page.page_content

    elif fileExt.upper() in [ "TXT", "CSV", "JSON" ] :

        with open( file, "r" ) as rawJson :

            fileImport = rawJson.read()

            # print( fileImport )

    elif fileExt.upper() in [ "DOC", "DOCX", "PPT", "PPTX" ] :

        # blah blah blah