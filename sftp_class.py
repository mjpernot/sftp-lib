# Classification (U)

"""Program:  sftp_class.py

    Description:  Class definitions and methods for ssh and sftp connections.

    Classes:
        SFTP

"""

# Libraries and Global Variables

# Standard
import warnings

# Third-Party
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko

# Local
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class SFTP(object):

    """Class:  SFTP

    Description:  Class which is a representation of a SFTP connection.  A
        SFTP object is used as proxy to open up a SSH/SFTP connection to a
        server.

    Methods:
        __init__ -> Class instance initilization.
        open_conn -> Open a sftp connection to a server.
        close_conn -> Close the sftp connection.
        chg_dir -> Change to a new directory.
        get_pwd -> Return the current directory path.
        put_file -> Put file in destination location.
    """

    def __init__(self, cfg_file, cfg_dir, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the SSH class.

        Arguments:
            (input)  cfg_file -> Configuration file for the sftp connection.
            (input)  cfg_dir -> Directory path containing configuration file.

        """

        self.cfg_file = cfg_file
        self.cfg_dir = cfg_dir

        cfg = gen_libs.load_module(self.cfg_file, self.cfg_dir)

        self.username = cfg.username
        self.password = cfg.password
        self.host = cfg.host
        self.port = cfg.port
        self.log_file = cfg.log_file

        paramiko.util.log_to_file(self.log_file)

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.is_connected = False
        self.sftp = None

    def open_conn(self, **kwargs):

        """Method:  open_conn

        Description:  Open a sftp connection to a server via a ssh connection.

        Arguments:

        """

        self.is_connected = False

        try:
            self.ssh.connect(self.host, username=self.username,
                             password=self.password)
            self.is_connected = True
            self.sftp = self.ssh.open_sftp()

        except paramiko.AuthenticationException:
            print("ERROR:  Authentication failure.")

        except paramiko.SSHException:
            print("ERROR:  Connection error.")

        except:
            print("ERROR:  Unknown error.")

    def close_conn(self, **kwargs):

        """Method:  close_conn

        Description:  Close a sftp connection to a server.

        Arguments:

        """

        self.ssh.close()
        self.is_connected = False

    def chg_dir(self, chg_dir, **kwargs):

        """Method:  chg_dir

        Description:  Change to directory in the sftp connection.

        Arguments:
            (input)  chg_dir -> Directory to change to (relative or absolute).
            (output) status -> True|False - Change directory succeeded.

        """

        try:
            self.sftp.chdir(chg_dir)
            status = True

        except IOError:
            print("IOError: No such directory: %s" % chg_dir)
            status = False

        return status

    def get_pwd(self, **kwargs):

        """Method:  get_pwd

        Description:  Return the current path directory in the sftp connection.

        Arguments:
            (output) Current path directory.

        """

        return self.sftp.getcwd()

    def put_file(self, source_file, destination_file, **kwargs):

        """Method:  put_file

        Description:  Puts the source file at the destination location.

        Arguments:
            (input) source_file -> Source file name and directory path to put.
            (input) destination_file -> Destination file name & directory path"

        """

        self.sftp.put(source_file, destination_file)
