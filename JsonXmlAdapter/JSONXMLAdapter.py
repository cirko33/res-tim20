import json, xmltodict

def ConvertToJSON(text):
    xmldict = xmltodict.parse(text)
    return json.dumps(xmldict)[13:-1]
    
def ConvertToXML(z):
    zahtev = json.loads(z)        
    ret = "<request>\n"
    for key,value in zahtev.items():
        ret += "\t<{kljuc}>{vrednost}</{kljuc}>\n".format(kljuc = key, vrednost = value)  
    ret += "</request>"     
    return ret 
