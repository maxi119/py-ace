
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
		

Example.py
----
	import collections
	from pyace import make_ace, SvnInfo, ProjectInfo

	svn = SvnInfo (  user = 'user', password = 'password' )

	Projects = [
		ProjectInfo( **dict (
			work_dir = '../Server',
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
			make_ace( p, svn )

		
Execute
----
	python Example.py build_ext --inplace
	
	Finally, get output/game.zip
	
