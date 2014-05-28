
from cython_setup import make_ace


class SvnInfo():
	def __init__(self, user, password ):
		self.user = user
		self.password = password

class ProjectInfo():
    def __init__( self, work_dir, target, output, keep_source=[], exclude=[] ):
        self.work_dir = work_dir
        self.target = 'Game'
        self.output = 'output/game.zip'
        self.keep_source = keep_source
        self.exclude = exclude
        
