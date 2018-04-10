from eventregistry import *
import datetime
import json

er = EventRegistry(apiKey = "ab40eb06-3900-4689-a369-b4098f4e49ef")
#er = EventRegistry(apiKey = YOUR_API_KEY)

obamaConceptUri = er.getConceptUri("Microsoft")
q = QueryEventsIter(conceptUri = obamaConceptUri)
for event in q.execQuery(er, sortBy = "date",maxItems= 300):
    with open('microsoft.txt', 'w') as outfile:
        json.dump(event, outfile)
