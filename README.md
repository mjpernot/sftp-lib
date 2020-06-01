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
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install sftp-lib as a library module.

Create requirements-sftp-lib.txt file:
```
vim {Other_Python_Project}/requirements-sftp-lib.txt
```

Add the following lines to the requirements-sftp-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/sftp-lib.git#egg=sftp-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md

Add the following lines under the "Install supporting classes and libraries" section.
```
   pip install -r requirements-sftp-lib.txt --target sftp_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target sftp_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Sftp-Lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:
```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:
```
paramiko==1.8.0
```

### Git Installation:

Install general SFTP libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/sftp-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd sftp-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
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

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd sftp-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
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

