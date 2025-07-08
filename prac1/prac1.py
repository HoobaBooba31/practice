import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from math import sin


def xml_file_creation(data, url):
    main_data = ET.Element("data")
    xdata = ET.SubElement(main_data, "xdata")
    ydata = ET.SubElement(main_data, "ydata")

    for i in range(len(data)):
        x = ET.SubElement(xdata, "x")
        y = ET.SubElement(ydata, "y")
        x.text = data[i][0]
        y.text = data[i][1]

    rough_string = ET.tostring(main_data, "utf-8")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    with open(url, "w") as f:
        f.write(pretty_xml)


def main():
    if not os.path.exists("results"):
        os.mkdir("results")

    directory = os.path.join('results', 'prac1.xml')

    axes = [[], []]
    x = 0
    data = []

    while x <= 1:
        y = pow((6 * x - 2), 2) * sin(12 * x - 4)
        axes[0].append(x)
        axes[1].append(y)
        data.append([str(x), str(y)])
        x += 0.01

    xml_file_creation(data, directory)
    fix, ax = plt.subplots()
    ax.plot(axes[0], axes[1])
    plt.show()


if __name__ == "__main__":
    main()
