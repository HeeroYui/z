#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "zip conpression and decompression library"

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
	    "zlib/adler32.c",
	    "zlib/crc32.c",
	    "zlib/deflate.c",
	    "zlib/infback.c",
	    "zlib/inffast.c",
	    "zlib/inflate.c",
	    "zlib/inftrees.c",
	    "zlib/trees.c",
	    "zlib/zutil.c",
	    "zlib/compress.c",
	    "zlib/uncompr.c",
	    "zlib/gzclose.c",
	    "zlib/gzlib.c",
	    "zlib/gzread.c",
	    "zlib/gzwrite.c"
	    ])
	# build in C mode
	my_module.compile_version("c", 1999)
	my_module.add_path(tools.get_current_path(__file__))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "zlib"))
	my_module.compile_flags('c', [
	    "-D_LARGEFILE64_SOURCE=1",
	    "-DHAVE_HIDDEN"
	    ])
	my_module.add_header_file([
	    'zlib/zlib.h',
	    'zlib/inflate.h',
	    'zlib/deflate.h',
	    'zlib/inffast.h',
	    'zlib/zutil.h',
	    'zlib/inftrees.h',
	    'zlib/trees.h',
	    'zlib/crc32.h',
	    'zlib/gzguts.h',
	    'zlib/inffixed.h',
	    'zlib/zconf.h'
	    ], destination_path="")
	my_module.add_module_depend(['c'])
	return my_module


