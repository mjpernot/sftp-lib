#!/usr/bin/python
# Classification (U)

"""Program:  sftp_chg_dir.py

    Description:  Unit testing of SFTP.chg_dir in sftp_class.py.

    Usage:
        test/unit/sftp_class/sftp_chg_dir.py

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
import version

__version__ = version.__version__


class SSHClient(object):

    """Class:  SSHClient

    Description:  Class stub holder for paramiko.SSHClient class.

    Methods:
        __init__ -> Class initialization.
        open_sftp -> open_sftp method.
        chdir -> chdir method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.chg_dir = None

    def open_sftp(self):

        """Method:  open_sftp

        Description:  open_sftp method.

        Arguments:

        """

        return self.chdir

    def chdir(self, chg_dir):

        """Method:  chdir

        Description:  chdir method.

        Arguments:

        """

        self.chg_dir = chg_dir


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_chg_dir_good -> Test with changing directory.
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
        self.chg_dir = "/dir/path"

    @mock.patch("sftp_class.paramiko.SSHClient.open_sftp")
    @mock.patch("sftp_class.gen_libs.load_module")
    def test_chg_dir_good(self, mock_cfg, mock_sftp):

        """Function:  test_chg_dir_good

        Description:  Test with changing directory.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        mock_sftp.return_value = True

        sftp = sftp_class.SFTP(self.cfg_file, self.cfg_dir)
        sftp.sftp = self.sshclient
        sftp.is_connected = True

        self.assertTrue(sftp.chg_dir(self.chg_dir))

        self.assertEqual(
            (sftp.username, sftp.log_file, sftp.is_connected),
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
