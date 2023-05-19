from setup import src

filen = src["html_filename"]
eevee_social = src["eevee_social"]

with open(filen,'r') as f:
    reader = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(reader,'html.parser')

class_fetch = []
for i in soup.find_all():
    if i.has_attr('class'):
        for j in i['class']:
            if "eevee" in j:
                class_fetch.append(j)

unify = set(class_fetch)
classes = list(unify)

with open(eevee_social,'r') as f:
    reader2 = f.read()

with open("eevee-social-extract.js",'w') as n:
    n.write("""document.addEventListener("DOMContentLoaded", () => {\n\t\tlet svg_tag = document.getElementsByTagName("svg");\n\t\tfor (let tag = 0; tag < svg_tag.length; tag++) {\n\t\t\tsvg_tag[tag].setAttribute("xmlns", "http://www.w3.org/2000/svg");}""")

pure = []
for class_ in classes:
    import re
    filtering = re.sub("eevee-","",class_)
    pure.append(filtering)

    try:
        #Fetching Classes
        start = reader2.index(f"//{filtering}")
        end = reader2.index(f"//!{filtering}")
        result = reader2[start:end]
        with open("eevee-social-extract.js",'a') as n:
            n.write(result)
    except:
        pass

#Fetching Array of icons
iconfetch = "icons-names"
icons = reader2.index(f"//{iconfetch}")
icone = reader2.index(f"//!{iconfetch}")
iconr = reader2[icons:icone]
with open("eevee-social-extract.js",'a') as n:
    n.write(iconr)

for class_ in pure:
    try:
        #Fetching Classes
        start = reader2.index(f"//loop-{class_}")
        end = reader2.index(f"//!loop-{class_}")
        result = reader2[start:end]
        with open("eevee-social-extract.js",'a') as n:
            n.write(result)
    except:
        pass

with open("eevee-social-extract.js",'a') as n:
    n.write("""});""")