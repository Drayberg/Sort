import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', action='store', dest='path', help='Enter the path to some shit')
parser.add_argument('-i', '--image', action='store_true', dest='image', help='Switch sorting images by size')
parser.add_argument('-v', '--video', action='store_true', dest='video', help='Switch sorting video by size')
parser.add_argument('-o', '--other', action='store_true', dest='other', help='Switch sorting other files by size')
parser.add_argument('-s', '--size', action='store', dest='size', default=1000000, help='Defines size of object')
args = parser.parse_args()