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

    