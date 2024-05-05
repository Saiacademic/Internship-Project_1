import sys
import os
import glob
import shutil
import time
import logging
from datetime import timedelta, date


# start editable vars #
days_old = 10	
original_folder = r"E:\Testing 1"	# folder to move files from
new_folder = r"E:\Testing 2"		# folder to move files to
logfile = r"C:\Users\Sai Patil\Documents\Source\log.log"

logging.basicConfig(filename="log.log",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
	
# start function definitions #
def log(level,msg,tofile=True):
	print (msg)
	
	if tofile == True:
		if level == 0:
			logger.info(msg)
		else:
			logger.error(msg)
			
def end(code):
	log(0,"End.")
	log(0,"-------------------------")

	sys.exit(code)


# start process #

move_date = date.today() - timedelta(days=days_old)
move_date = time.mktime(move_date.timetuple())
logger = logging.getLogger("cuarch")
hdlr = logging.FileHandler(logfile)
hdlr.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s'))      #log file format#
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)       

log(0,"Initialising...")

count = 0
size = 0.0

for filename in glob.glob1(original_folder, "*.*"):
    srcfile = os.path.join(original_folder, filename)
    destfile = os.path.join(new_folder, filename)
    if os.stat(srcfile).st_mtime < move_date:
        if not os.path.isfile(destfile):
            size = size + (os.path.getsize(srcfile) / (1024*1024.0))
            shutil.move(srcfile, destfile)
        
            log(0,"Archived '" + filename + "'.")      #log file statement
            count = count + 1
log(0,"Archived " + str(count) + " files, totalling " + str(round(size,2)) + "MB.")   #no. of files and size
end(0)
