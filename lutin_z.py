#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "z-lib library"


def create(target):
	if target.name=="Windows":
		my_module = module.Module(__file__, 'z', 'LIBRARY')
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
			"zlib/gzwrite.c"])
		
		my_module.add_export_path(tools.get_current_path(__file__))
		my_module.add_export_path(tools.get_current_path(__file__) + "/zlib")
		
		my_module.compile_flags('c', [
			"-D_LARGEFILE64_SOURCE=1",
			"-DHAVE_HIDDEN"])
		
		# add the currrent module at the 
		return my_module
	else:
		my_module = module.Module(__file__, 'z', 'PREBUILD')
		
		my_module.add_export_flag('link', '-lz')
		# add the currrent module at the 
		return my_module


