# Python project that contains common libraries and classes for SFTP.
# Classification (U)

# Description:
  This project consists of a number of Python files that are common function libraries and classes to setup and use ssh and sftp connections.  These programs are not standalone programs, but are available for python programs to utilize.


###  This README file is broken down into the following sections:
 * Prerequisites
 * Installation
 * Testing
   - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_libs


# Installation:
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirement files for the supporting library in another program's project.

```
cd {Python_Project}
cat requirements-sftp-lib.txt --target sftp_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target sftp_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the system module requirements to the another program's requirements.txt file and remove any duplicates.

``
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general SFTP libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/sftp-lib.git
```

Install supporting classes and libraries

```
cd sftp-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Testing:

# Unit Testing:

### Installation:

Install general SFTP libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/sftp-lib.git
```

Install supporting classes and libraries

```
cd sftp-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Unit testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/sftp-lib
test/unit/sftp_class/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/sftp-lib
test/unit/sftp_class/code_coverage.sh
```

