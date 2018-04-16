import getopt
from operator import itemgetter
import re
from urllib import request
import sys

def usage():
      print ("\nUSAGE: python firstWebScrpaer.py \"<site-name>\"\n")
      print ("[Prints the number of elements and the top five (or less) most-used ending tags (e.g. </html>) in a site]\n")
      print ("-h (--help) Display this usage")
      exit(1)

def main(argv):
    #usage case
    try:
        opts, args = getopt.getopt(argv, 'h', ['help'])
        if len(sys.argv) < 2:
            print ("Missing Site.")
            usage()
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    #using top five
    DEFAULT_MAPPING_COUNT_DISPLAY = 5

    #open site and decode
    r = request.urlopen(sys.argv[1])
    bytecode = r.read()
    htmlstr = bytecode.decode()

    #count elements and
    #map end tags to the number of appearances
    elemCount = 0
    tagDict = {}
    p = re.compile(r'</[^>]*>')
    iter = p.findall(htmlstr)
    for match in iter:
        elemCount = elemCount + 1
        if match not in tagDict:
            tagDict[match] = 0
        tagDict[match] = tagDict[match] + 1

    #print number of elements
    print(elemCount)

    #print top results
    topMappings = sorted(tagDict.items(), key=itemgetter(1), reverse=True)
    mapLength = min (DEFAULT_MAPPING_COUNT_DISPLAY, len(topMappings))

    i=0
    while i < mapLength:
        print(topMappings[i])
        i=i+1

    if mapLength < DEFAULT_MAPPING_COUNT_DISPLAY:
        print('No more.')

    exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
