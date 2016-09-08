#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "MINIZIP zip file interface"

def get_licence():
	return "zlib"

def get_compagny_type():
	return "edu"

def get_compagny_name():
	return "Caltech Alumni Association"

def get_maintainer():
	return ["Mark Adler <madler@alumni.caltech.edu>", ]

def get_version():
	return [1,2,8]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		"zlib/contrib/minizip/unzip.c",
		"zlib/contrib/minizip/zip.c",
		"zlib/contrib/minizip/miniunz.c",
		"zlib/contrib/minizip/ioapi.c"])
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "zlib/contrib/"))
	my_module.add_depend('z')
	my_module.compile_version("c", 1999)
	my_module.add_flag('c', [
		"-DNOCRYPT",
		"-DIOAPI_NO_64"])
	if "IOs" in target.get_type() \
	   or "MacOs" in target.get_type():
		my_module.add_flag('c', "-Wno-implicit-function-declaration")
	my_module.add_header_file([
		'zlib/contrib/minizip/crypt.h',
		'zlib/contrib/minizip/unzip.h',
		'zlib/contrib/minizip/ioapi.h',
		'zlib/contrib/minizip/mztools.h',
		'zlib/contrib/minizip/iowin32.h',
		'zlib/contrib/minizip/zip.h'
		],
		clip_path='zlib/contrib')
	return my_module


