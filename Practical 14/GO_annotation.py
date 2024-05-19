### DOM way ###

import time                               # import necessary libraries
import xml.dom.minidom
import matplotlib.pylab as plt
import xml.sax
start_DOM= time.perf_counter()                   # Start to calculate time needed for DOM way
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')    # get 'term' by tag name
biological_process = 0
molecular_function = 0
cellular_component = 0
for term in terms:
    name = term.getElementsByTagName('namespace')[0].firstChild.nodeValue      # get the term names
    if name == 'biological_process':
        biological_process = biological_process + 1
    else:
        if name == 'molecular_function':
            molecular_function= molecular_function + 1
        if name == 'cellular_component':
            cellular_component= cellular_component + 1

print('The number of term biological_process is (by DOM way):',biological_process)  # DOM way
print('The number of term molecular_function is (by DOM way):',molecular_function)
print('The number of term cellular_component is (by DOM way):',cellular_component)
end_DOM = time.perf_counter()       # Finish to calculate time needed for DOM way
print(' The time for DOM method is:',end_DOM-start_DOM,'s')  # Calculate the time needed for DOM way


x=['biological_process','molecular_function','cellular_component']
y= [biological_process,molecular_function,cellular_component]
plt.figure()
plt.xlabel("GO terms") # create x label name
plt.ylabel("number of terms") # create y label name
plt.title("Frequency Data of GO Terms (DOM)") # add a title to the figure
plt.bar(x,y) # create the bar plot
plt.show()

### SAX way ###
start_SAX = time.perf_counter()    # Start to calculate time needed for SAX way


class TermCounter(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace_counts = {
            'biological_process': 0,
            'molecular_function': 0,
            'cellular_component': 0
        }

    def startElement(self, tag, attributes):
        self.current_element = tag
        if tag == "term":
            self.in_term = True

    def characters(self, content):
        if self.current_element == "namespace":
            if content in self.namespace_counts:
                self.namespace_counts[content] += 1

    def endElement(self, tag):
        self.current_element = ""

    def get_counts(self):
        return self.namespace_counts

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = TermCounter()
parser.setContentHandler(handler)
parser.parse('go_obo.xml')
namespace_counts = handler.get_counts()
print('The number of term biological_process is (by SAX way):', namespace_counts['biological_process'])
print("The number of term molecular_function is (by SAX way):", namespace_counts['molecular_function'])
print('The number of term cellular_component is (by SAX way):', namespace_counts['cellular_component'])

end_SAX = time.perf_counter()    # Finish to calculate time needed for SAX way
print(' The time for SAX method is:',end_SAX-start_SAX,'s')     # Calculate the time needed for SAX way
print("From my computer, it can be seen that SAX API is faster.")  

# From my computer, SAX API is faster than DOM.

x1=['biological_process','molecular_function','cellular_component']
y1= [namespace_counts['biological_process'],namespace_counts['molecular_function'],namespace_counts['cellular_component']]
plt.figure()
plt.xlabel("GO terms") # create x label name
plt.ylabel("number of terms") # create y label name
plt.title("Frequency Data of GO Terms (SAX)") # add a title to the figure
plt.bar(x1,y1) # create the bar plot
plt.show()

### From my computer, SAX API is faster than DOM. ###
