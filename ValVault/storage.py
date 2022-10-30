import platform
import json
from pathlib import Path
from os import getenv

def save_to_drive(data, file):
	f = open(file, "w")
	f.write(data)
	f.close()

def read_from_drive(file):
	f = open(file, "r")
	data = f.read()
	f.close()
	return data

def json_write(data, file):
	jsonData = json.dumps(data,indent=4)
	save_to_drive(jsonData, file)

def json_read(file):
	rawData = read_from_drive(file)
	data = json.loads(rawData)
	return data

def create_path(path: Path):
	if(path.is_dir()):
		return
	path.mkdir()

def linux_path():
	xdg = getenv("XDG_CONFIG_HOME")
	if (xdg):
		return Path(xdg) / "ValUtils"
	home = Path(getenv('HOME'))
	return home / ".ValUtils"

def utils_path():
	global utilsPath
	if (platform.system() == "Windows"):
		appdata = Path(getenv('APPDATA'))
		utilsPath = appdata / "ValUtils"
		create_path(utilsPath)
	elif (platform.system() == "Linux"):
		utilsPath = linux_path()
		create_path(utilsPath)
	return utilsPath

def set_path():
	global settingsPath
	utilsPath = utils_path()
	settingsPath = utilsPath / "vault"
	create_path(settingsPath)

set_path()