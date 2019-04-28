#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#*http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles K Barcza*
#*************************************************************************************(c)2002-2019********

import os
import glob
import shutil
import sys

from distutils.core import setup
from distutils.cmd import Command
from distutils.command.build import build
from distutils.command.install import install
from setuptools import setup
import subprocess
    
with open("README.md", "r") as fh:
    long_description = fh.read()

DEPENDENCIES = [
    'PyQt5',
    'gettext',
]

def check_modules():
    for d in DEPENDENCIES:
        try:
            if type(d)==str:
                __import__(d)
            elif type(d)==list:
                if d[1].find('/')==-1:
                    exec(f"from {d[0]} import {d[1]}")
                else:
                    if not os.path.exists(d[1]+d[0]):
                        print(f"{d[0]} command is not available, please install before build!")
                        exit(1)
        except Exception as e:
            print("Please install the {} module before build! \n{}".format(d,e))
            exit(1)

def have_gettext():
    return subprocess.getoutput("pyuic5 --help").find("--gettext") > -1

def update_messages():
    # Create empty directory
    pkgname="parallx"
    os.system("rm -rf .tmp")
    os.makedirs(".tmp")
    # Collect UI files
    for filename in glob.glob1("modules_uic", "*.ui"):
        if have_gettext():
            os.system("pyuic5 -g -o .tmp/ui_%s.py modules_uic/%s" % (filename.split(".")[0], filename))
        else:
            os.system("pyuic5 -o .tmp/ui_%s.py modules_uic/%s" % (filename.split(".")[0], filename))
    # Collect Python files
    for filename in glob.glob1("modules_uic", "*.py"):
        shutil.copy("modules_uic/%s" % filename, ".tmp")
    # Generate POT file
    os.system("mkdir -p po")
    os.system("""xgettext --default-domain=%s --keyword=_ --keyword=i18n --keyword=ki18n \
              --package-name='parallx' \
              --package-version=1.0.1 \
              --copyright-holder='blackPanther Europe' \
              --msgid-bugs-address=info@blackpantheros.eu \
              -o po/%s.pot .tmp/* src/*.py *.py""" % (pkgname,pkgname))
    # Update PO files
    for item in os.listdir("po"):
        if item.endswith(".po"):
            os.system("msgmerge -q -o .tmp/temp.po po/%s po/%s.pot" % (item,pkgname))
            os.system("cp .tmp/temp.po po/%s" % item)
    # Remove temporary directory
    os.system("rm -rf .tmp")
    
class Build(build):
    def run(self):
        check_modules()
        pkgname="parallx"
        locale_dir = "build/share/locale"
        os.system("rm -rf build")
        os.system("mkdir -p build/lib/parallx")
        os.system("mkdir -p build/scripts-3.7")

        print ("Copying PYs Src...")
        os.system("cp src/*.py build/lib/parallx")
        print ("Generating UIs...")
        for filename in glob.glob1("modules_uic", "*.ui"):
            if have_gettext():
                os.system("pyuic5 -g -o build/lib/parallx/ui_%s.py modules_uic/%s" 
                          % (filename.split(".")[0], filename))
            else:
                os.system("pyuic5 -o build/lib/parallx/ui_%s.py modules_uic/%s" 
                          % (filename.split(".")[0], filename))

        for filename in glob.glob1("./", "*.py"):
            if filename not in ["setup.py"]:
                os.system("cat %s > build/scripts-3.7/%s" % (filename, filename[:-3]))

        print ("Build locales...")
        for filename in glob.glob1("po", "*.po"):
            lang = filename.rsplit(".", 1)[0]
            os.system("msgfmt po/%s.po -o po/%s.mo" % (lang, lang))
            try:
                os.makedirs(os.path.join(locale_dir, "%s/LC_MESSAGES" % lang))
            except OSError:
                pass
            shutil.copy("po/%s.mo" % lang, os.path.join(locale_dir, "%s/LC_MESSAGES" 
                                                        % lang, "%s.mo" % pkgname))


class Install(install):
    def run(self):
        install.run(self)

if "update_messages" in sys.argv:
    update_messages()
    sys.exit(0)

setup(
    name="parallx",

    version="0.0.1",

    description="Easy gui for parallel actions on intranet computers",
    long_description = """
    The ParallX is an administration tool. You can execute commands on 
    several computers in the same time with this tool.
    
    Project idea and design: Charles K. Barcza
    Maintainer: Miklos Horvath 
    """,
    
    url="https://github.com/blackPantherOS/parallx",

    author="Charles Barcza, Miklos Horvath",
    maintainer="Miklos Horvath <hmiki@blackpantheros.eu>",
    
    license="GPLv3+",

    classifiers=[
        "Development Status :: 3 - Alpha",

       "Intended Audience :: System Administrators",

        "Topic :: Desktop Environment",
        "Topic :: Desktop Environment :: K Desktop Environment (KDE)",
        "Topic :: System :: Software Distribution",
        "Environment :: X11 Applications :: Qt",
        
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: BSD :: OpenBSD",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],

    package_dir={"parallx":"build/lib/parallx"},
    packages=["parallx"],
    scripts=["build/scripts-3.7/parallx"],
    data_files  = [('/'.join(e.split('/')[1:-1]), [e]) for e in subprocess.getoutput("find build/share/locale").split() if ".mo" in e],
    install_requires = [],

    cmdclass = {
        'build': Build,
        'install': Install,
    }
)
