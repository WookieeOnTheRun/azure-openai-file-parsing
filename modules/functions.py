import json, openai, requests, pypdf

# take output dictionary of page numbers and summaries and create clean output
def fnGenerateOutput( dictOutput ) :

    for keys, values in dictOutput[ "Pages" ].items() :

        print( values )

# determine file type
def fnGetFileType( file ) :

    # regardless of location, assumption is final character(s) are ".xxx(x)"

    fileExt = ( file.split( "." ) )[ -1 ]

    return fileExt