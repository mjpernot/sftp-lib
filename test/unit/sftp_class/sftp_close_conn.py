#!/usr/bin/python
# Classification (U)

"""Program:  sftp_close_conn.py

    Description:  Unit testing of SFTP.close_conn in sftp_class.py.

    Usage:
        test/unit/sftp_class/sftp_close_conn.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_close_conn_good -> Test with close connection.
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
        self.cfg_file = "Config_File"
        self.cfg_dir = "Config_Dir"

    @mock.patch("sftp_class.gen_libs.load_module")
    def test_close_conn_good(self, mock_cfg):

        """Function:  test_close_conn_good

        Description:  Test with close connection.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        sftp = sftp_class.SFTP(self.cfg_file, self.cfg_dir)

        sftp.close_conn()

        self.assertEqual((
            sftp.username, sftp.log_file, sftp.is_connected, sftp.sftp),
                         (self.cfg.username, self.cfg.log_file, False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.cfg.log_file):
            os.remove(self.cfg.log_file)


if __name__ == "__main__":
    unittest.main()
