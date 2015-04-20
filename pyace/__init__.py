
from cython_setup import make_ace

__version__ = '0.0.4'

class SvnInfo():
	def __init__(self, user, password ):
		self.user = user
		self.password = password

class ProjectInfo():
    def __init__( self, work_dir, target, output, keep_source=[], exclude=[] ):
        self.work_dir = work_dir
        self.target = target
        self.output = output
        self.keep_source = keep_source
        self.exclude = exclude
        
