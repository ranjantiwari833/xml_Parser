import xml.etree.ElementTree as ET
import re
import sys

def parse_txt(txt_file):
    ## Parse the txt file and returns the formatted data as a list
    with open(txt_file) as coordinates:
        data = [point.strip() for point in coordinates.readlines()] # replaces the white spaces in each line at front and back
    
    ## Format the data in the txt file
    for point in range(len(data)):
        data[point] = re.sub(' ',',', data[point]) # converts the space separated data points to , separated
        data[point] = re.sub(';',',', data[point]) # removes the trailing ; and replaces with ,
    
    return data

def parse_xml(xml_file, txt_file):
    data = parse_txt(txt_file)

    ## Parse the xml file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ## find and replace the points
    counter = -1 # counter starts from -1 as the 1st tag read in root.iter is the blank tag

    for attributes in root.iter():
        # print(attributes.text)
        attributes.text = re.sub(r"Point1          [a-z0-9\.,\-]*,", f"Point1          {data[counter]}",attributes.text)
        attributes.text = re.sub(r"Point2          [a-z0-9\.,\-]*,", f"Point2          {data[counter]}",attributes.text)
        # print(attributes.text)
        counter += 1

    ## write the updated xml data into new xml file
    tree.write('updated_coordinates.xml')

def main ():
    if len(sys.argv) != 3:
        print("Not enough Arguments given.")
        print("Usage: python .\\xml_Parse.py .\\data.xml .\\data.txt")
    
    if len(sys.argv) == 3:
        parse_xml(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()