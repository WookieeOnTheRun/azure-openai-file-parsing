import json, openai, requests, pypdf

# take output dictionary of page numbers and summaries and create clean output
def fnGenerateOutput( dictOutput ) :

    for keys, values in dictOutput[ "Pages" ].items() :

        print( values )