import argparse
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import os 

parser = argparse.ArgumentParser(prog="prac2")
parser.add_argument("filename")
parser.add_argument("-l", "--largex", help="Max large X")
parser.add_argument("-s", "--smallx", help="Max small X")

args = parser.parse_args()


def plot_prac(largex=0, smallx=1):

    directory = os.path.join("examples", args.filename)
    data = [[], []]
    try:
        tree = ET.ElementTree(file=directory)
        root = tree.getroot()
        for x in root.iter("x"):
            data[0].append(float(x.text))
        for y in root.iter("y"):
            data[1].append(float(y.text))
        fix, ax = plt.subplots()
        ax.plot(data[0], data[1])
        ax.set_xbound(lower=smallx, upper=largex)
        plt.show()
    except:
        return print("Ошибка при чтении файла или генерации графика")


if __name__ == "__main__":
    try:
        plot_prac(
            float(args.largex) if args.largex is not None else 0,
            float(args.smallx) if args.smallx is not None else 1,
        )
    except Exception as e:
        print(f"Ошибка: {str(e)}")
