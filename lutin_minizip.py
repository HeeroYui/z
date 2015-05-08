#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "MINIZIP : Small zip interface"


def create(target):
	myModule = module.Module(__file__, 'minizip', 'LIBRARY')
	myModule.add_src_file([
		"zlib/contrib/minizip/unzip.c",
		"zlib/contrib/minizip/zip.c",
		"zlib/contrib/minizip/miniunz.c",
		"zlib/contrib/minizip/ioapi.c"])
	
	myModule.add_export_path(tools.get_current_path(__file__) + "/zlib/contrib/")
	
	myModule.add_module_depend('z')
	
	myModule.compile_version_CC(1999)
	
	myModule.compile_flags('c', [
		"-DNOCRYPT",
		"-DIOAPI_NO_64"])
	
	if target.name=="IOs" or target.name=="MacOs":
		myModule.compile_flags('c', "-Wno-implicit-function-declaration")
	
	# add the currrent module at the 
	return myModule


