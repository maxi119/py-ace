
Make all python script as c extentions
====

Config with a list with struct

Struct Project
----
	Projects
		work_dir		switch to the folder as working directory
		target			the target folder
		output			zip the target folder as gz file
		keep_source		keep .py inside
		exclude			remove the file inside  the folder.

Struct svn
----
	svn
		user
		password
		

Example
----
	from py-ace import *
	import collections
	SVN_INFO = collections.namedtuple( 'SVN_INFO', [ 'user', 'password', 'revision'] )

	class Struct(object):
		def __init__(self, **param ):
			self.__dict__.update(param)

	svn = SVN_INFO (  user = 'user', password = 'password', revision = -1 )

	Projects = [
		Struct( **dict (
			work_dir = '../MyProject',
			target = 'Game',
			output = 'output/game.zip',
			keep_source = [
					'Game/manage.py',
					'Game/Game/settings.py',
					'Game/Game/wsgi.py',
				],
			exclude = [
					'Game/Game/settings.py'
				],
			)) ,
		]        





	if __name__ == '__main__':


		for p in Projects:
			outfile = p.output
			p.output = os.path.join( os.getcwd(), outfile )
			if p.work_dir and p.work_dir != "": 
				os.chdir( p.work_dir )
			prepare_cleanup( p, svn )
			make_library( p )
			post_cleanup( p )
			pack_all( p )



