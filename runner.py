#!/usr/bin/python3

import os
import re
import subprocess

target = "choopiepups.superrealwebsite.fart"

def runwget(targetdir):
        global target
        thistarget = '--directory-prefix=' + targetdir
        proc = subprocess.Popen(['wget', thistarget, '-rkpN', '-e robots=off', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout)
        print(stderr)
        gettitlecmd = "cat " + targetdir + target "/index.html | grep -iPo '(?<=<title>)(.*)(?=</title>)'"
        proc2 = subprocess.Popen(gettitlecmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc2.communicate()
        thisstr = (stdout, stderr)
        print(thisstr)
        thistitle = str(thisstr).replace("(b'",'')
        cleantitle = thistitle[:24].replace(" ", '_')
        superclean = re.sub('[^A-Za-z0-9]+', '', cleantitle)
        copynewcmd = "cp -r " + targetdir + "* ./fakepages/" + superclean + "/"
        proc3 =  subprocess.Popen(copynewcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc3.communicate()
        thisstr = (stdout, stderr)
        print(thisstr)
        
for i in range(1,300):
        runwget('./fakepages/' + str(i) + '/')
