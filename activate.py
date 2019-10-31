import os
import subprocess as sp


def activ():
	path = os.path.abspath('activate.bat')
	length = len(path)
	path = path[::-1]
	path = path[12:length]
	path = path[::-1]
	print(path)
	sp.call(f'cd {path} & start activate.bat', shell=True)


if __name__ == '__main__':
	activ()
else:
	activ()
