import os
from logger import Logger

class FileManager:
    """
    A class used to manage file operations.

    ...

    Attributes
    ----------
    file_path : str
        a formatted string to print out the file path
    binary : bool, optional
        a boolean indicating if file operations should be binary (default is False)
    file_dir : str
        a string representing the file directory
    file_type : str
        a string representing the file extension

    Methods
    -------
    read():
        Reads the content of the file.
    write(content):
        Writes the content to the file.
    rename(new_name):
        Renames the file.
    get_file_extension():
        Returns the file extension.
    check_dir_exist(dir_path):
        Checks if a directory exists.
    create_dir(dir_path, create_full_path=False):
        Creates a new directory.
    check_file_exist():
        Checks if the file exists.
    stat():
        Returns the status of the file.
        self.file_path
    """

    def __init__(self, file_path, binary=False, log_file=None):
        """
        Constructs all the necessary attributes for the FileManager object.

        Parameters
        ----------
            file_path : str
                The file path.
            binary : bool, optional
                If True, the file operations are handled in binary mode (default is False).
        """

        self.file_path = file_path
        self.file_name = self._extract_file_name()
        self.binary = binary
        self.logger = Logger("FileManager", level="INFO", log_file=log_file)
        self.file_dir = os.path.dirname(self.file_path)
        self.file_type = self.get_file_extension()

    def read(self):
        """
        Reads the content of the file.

        Returns
        -------
        str
            The content of the file.
        """

        try:
            mode = 'rb' if self.binary else 'r'
            with open(self.file_path, mode) as file:
                return file.read()
        except FileNotFoundError:
            self.logger.log(f"{self.file_path} not found.", 'error')
        except IOError as e:
            self.logger.log(f"IOError: {str(e)}", 'error')

    def write(self, content):
        """
        Writes the content to the file.

        Parameters
        ----------
        content : str
            The content to write to the file.
        """

        try:
            mode = 'wb' if self.binary else 'w'
            with open(self.file_path, mode) as file:
                file.write(content)
        except IOError as e:
            self.logger.log(f"IOError: {str(e)}", 'error')

    def _extract_file_name(self):
        """
        Extracts the file name from a file path.

        Parameters
        ----------
        file_path : str
            The file path.

        Returns
        -------
        str
            The file name.
        """
        return os.path.basename(self.file_path)
                      

    def _get_new_path(self, new_name):
        return os.path.join(self.file_dir, new_name)

    def rename(self, new_name):
        new_file_path = self._get_new_path(new_name)
        try:
            os.rename(self.file_path, new_file_path)
            self.file_path = new_file_path
            self.file_name = self._extract_file_name()   

        except FileNotFoundError:
            self.logger.log(f"{self.file_path} must exist before rename.", 'error')
        except IOError as e:
            self.logger.log(f"IOError: {str(e)}", 'error')

    def get_file_extension(self):
        _, extension = os.path.splitext(self.file_path)
        return extension

    def check_dir_exist(self, dir_path):
        return os.path.isdir(dir_path)

    def create_dir(self, dir_path, create_full_path=False):
        if not self.check_dir_exist(dir_path):
            if create_full_path:
                os.makedirs(dir_path)
            else:
                os.mkdir(dir_path)

    def check_file_exist(self):
        return os.path.isfile(self.file_path)

    def stat(self):
        return os.stat(self.file_path)