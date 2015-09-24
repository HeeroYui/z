#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "MINIZIP : Small zip interface"


def create(target):
	my_module = module.Module(__file__, 'minizip', 'LIBRARY')
	my_module.add_src_file([
		"zlib/contrib/minizip/unzip.c",
		"zlib/contrib/minizip/zip.c",
		"zlib/contrib/minizip/miniunz.c",
		"zlib/contrib/minizip/ioapi.c"])
	
	my_module.add_export_path(tools.get_current_path(__file__) + "/zlib/contrib/")
	
	my_module.add_module_depend('z')
	
	my_module.compile_version_CC(1999)
	
	my_module.compile_flags('c', [
		"-DNOCRYPT",
		"-DIOAPI_NO_64"])
	
	if target.name=="IOs" or target.name=="MacOs":
		my_module.compile_flags('c', "-Wno-implicit-function-declaration")
	
	# add the currrent module at the 
	return my_module


