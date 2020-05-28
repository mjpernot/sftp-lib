#!/usr/bin/python
# Classification (U)

"""Program:  sftp_get_pwd.py

    Description:  Unit testing of SFTP.get_pwd in sftp_class.py.

    Usage:
        test/unit/sftp_class/sftp_get_pwd.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import sftp_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class SSHClient(object):

    """Class:  SSHClient

    Description:  Class stub holder for paramiko.SSHClient class.

    Methods:
        __init__ -> Class initialization.
        open_sftp -> open_sftp method.
        getcwd -> getcwd method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def open_sftp(self):

        """Method:  open_sftp

        Description:  Class initialization.

        Arguments:

        """

        pass

    def getcwd(self):

        """Method:  chdir

        Description:  getcwd method.

        Arguments:

        """

        return True 


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_get_pwd_good -> Test with changing directory.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.username = "username"
                self.password = None
                self.host = "hostname"
                self.port = 22
                self.log_file = "./test/unit/sftp_class/tmp/paramiko.log"

        self.cfg = CfgTest()
        self.sshclient = SSHClient()
        self.cfg_file = "Config_File"
        self.cfg_dir = "Config_Dir"

    @mock.patch("sftp_class.paramiko.SSHClient.open_sftp")
    @mock.patch("sftp_class.gen_libs.load_module")
    def test_get_pwd_good(self, mock_cfg, mock_sftp):

        """Function:  test_get_pwd_good

        Description:  Test with changing directory.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        mock_sftp.return_value = True

        sftp = sftp_class.SFTP(self.cfg_file, self.cfg_dir)
        sftp.sftp = self.sshclient
        sftp.is_connected = True

        self.assertTrue(sftp.get_pwd())

        self.assertEqual((
            sftp.username, sftp.log_file, sftp.is_connected),
                         (self.cfg.username, self.cfg.log_file, True))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.cfg.log_file):
            os.remove(self.cfg.log_file)


if __name__ == "__main__":
    unittest.main()
