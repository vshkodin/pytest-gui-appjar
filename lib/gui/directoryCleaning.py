import os,shutil

def reports_cleaning():
        try:
            pathforscripttwo = os.path.realpath(__file__)
            pathforscripttwo = pathforscripttwo.replace('lib/tools/directoryCleaning.py', 'reports')
            shutil.rmtree(pathforscripttwo)
            return 'File removed'
        except:
            return 'Reports not found'