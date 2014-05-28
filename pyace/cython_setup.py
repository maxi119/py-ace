

from distutils.core import setup
from Cython.Build import cythonize
import Cython.Build.Dependencies as CB
from distutils.extension import Extension
import glob
import os, fnmatch
from os.path import basename

# import build_config

def _compile_py( filename ):
    import py_compile
    py_compile.compile( filename, )

def _make_extentions( target, ext ):
    ''' make each file as a module with hierarchy
        but keep __init__.py in folder..
    '''
    extensions = []
    t = target
    if True:
        for root, lstDir, lstFiles in os.walk(t):
            exfiles = []
            initFound = False if ext == 'py' else True
            for f in fnmatch.filter( lstFiles, "*.%s" %ext ):
                if f == "__init__.py":
                    initFound = True
                else:
                    exfiles.append( root + "/" + f )

            if initFound:
                pakname = '.'.join( x for x in root.split( os.path.sep ) if x != '' )
                if ext == 'py':
                    ## package root could not be use..
                    pakname_only = basename(root)
                    package_init = pakname + '._' + pakname_only  # => a.b ==> a.b._b
                    newName = root + "/_%s.py"%pakname_only
                    if os.path.isfile( newName ):
                    	os.remove( newName )
                    os.rename( root +"/__init__.py", newName )
                    eroot =  Extension( package_init, sources=[ root +"/_%s.py"%pakname_only] )
                    extensions.append( eroot )
                    # replace __init__.py
                    # os.system( "from %s import * >  %s /__init__.py"%( package_init, root ) )
                    with open( root+"/__init__.py", "w" ) as f:
                        f.write( "from _%s import *"%( pakname_only ) )
                    _compile_py( root + "/__init__.py" )
                    print pakname 

                for f in exfiles:
                    if f == '__init__.py':
                        print('')
                    modname = pakname+"."+ os.path.splitext( basename(f) )[0]
                    e =  Extension( name=modname , sources=[ f] )
                    extensions.append( e ) 
                    print "   %s"% modname 
                    
    return extensions
        
def _make_extentions_one( target, ext ):
    ''' Make all file into one package...
        if use .py ... the file couldn't be see as a module
    '''
    extensions = []
    for t in target:
        for root, lstDir, lstFiles in os.walk(t):
            exfiles = []
            initFound = False if ext == 'py' else True
            for f in fnmatch.filter( lstFiles, "*.%s" %ext ):
                if f == "__init__.py":
                    initFound = True
                else:
                    exfiles.append( root + "/" + f )

            if initFound:
                pakname = '.'.join( x for x in os.path.split( root ) if x != '' )
                flist = []
                if ext == 'py':
                    flist.append( root +"/__init__.py" )
                    print pakname 

                for f in exfiles:
                    modname = pakname+"."+ os.path.splitext( basename(f) )[0]
                    flist.append( f )
                    print "   %s"% modname 
                e =  Extension( name=pakname, sources=flist )
                extensions.append( e ) 
                    
    return extensions


def make_library( project ):

    
    extensions = _make_extentions( project.target, 'py' )

    #extensions += _make_extentions( ["utility"], 'pyx' )
    ex_module = cythonize( extensions )
    setup(
	    name = 'ace-package',
	    ext_modules = ex_module
	    #ext_modules = cythonize( 'utility/*.py', exclude=['__init__.*'] ),
	    )

def _remove_files( path, pattern ):
    import os, platform
    if (platform.system() == 'Windows') or (os.name == 'nt'):
        os.system( 'del %s\%s /s' %( path, pattern ) )
    else:
        os.system( 'rm -rf %s/%s' %( path, pattern ) ) 



def prepare_cleanup( project, svn ):
    # svn = build_config.svn
    # restore
    print('Restore all')
    os.system('svn update %s --username %s --password %s --no-auth-cache'%( project.target, svn.user, svn.password ) )
    # clear pyc
    print('Remove pyc, pyd')
    _remove_files( project.target, "*.pyc" )
    # clear pyd
    _remove_files( project.target, "*.pyd" )
    _remove_files( project.target, "*.so" )

    print('remove exclude files')
    # remove py that not in target..
    for e in project.exclude:
        try:
            os.remove( e )
        except Exception as e:
            pass

    for e in project.keep_source:
        try:
            os.remove( e )
        except Exception as e:
            pass
    

def post_cleanup( project ):
    print('clean up py.')
    _remove_files( project.target, "*.py" )
    _remove_files( project.target, "*.c" )
    _remove_files( project.target, "*.obj" )
    _remove_files( project.target, "*.lib" )
    _remove_files( project.target, "*.exp" )
    for f in project.keep_source:
        os.system( "svn revert %s" % f )

def zipdir( path, zfile ):
    for root, dirs, files, in os.walk(path):
        for file in files:
            zfile.write( os.path.join( root, file )) 


def pack_all( project ):
    import zipfile
    print( 'output tar file "%s"'%(project.output ) )

    outdir = os.path.dirname( project.output )
    if os.path.exists( outdir ) == False:
        os.makedirs( outdir )

    zfile = zipfile.ZipFile( project.output, "w", zipfile.ZIP_DEFLATED ) 
    zipdir( project.target, zfile )
    zfile.close()
    #os.system( 'tar zcf %s %s'%(project.output, project.target) )

def os_setup():
    import os, platform, nt
    if (platform.system() == 'Windows') or (os.name == 'nt'):
        vs2010 = os.environ.get('VS100COMNTOOLS')
        if vs2010:
            import distutils.msvc9compiler as dm9
            dm9.get_build_version = lambda : 10.0


def make_ace( project_info, svn ):
    outfile = project_info.output
    org_dir = None
    project_info.output = os.path.join( os.getcwd(), outfile )
    if project_info.work_dir and project_info.work_dir != "": 
        org_dir = os.getcwd()
        os.chdir( project_info.work_dir )
    prepare_cleanup( project_info, svn )
    make_library( project_info )
    post_cleanup( project_info )
    pack_all( project_info )

    if org_dir != None:
        os.chdir( org_dir )
            
            