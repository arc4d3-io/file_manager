import unittest
import os
from logger import Logger
from file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.logger = Logger("TestFileManager")
        self.test_file_path = "test_file.txt"
        self.new_file_name = "renamed_file.txt"      
        self.test_content = "This is a test file."
        self.file_manager = FileManager(self.test_file_path, log_file="test_file_manager_delete.log")

    def tearDown(self):
        # Remove o arquivo de teste após cada teste
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.new_file_name):
            os.remove(self.new_file_name)            

    def test_read_and_write_file(self):
        # Escreve conteúdo no arquivo de teste
        self.file_manager.write(self.test_content)

        # Lê o conteúdo do arquivo de teste
        content = self.file_manager.read()

        # Verifica se o conteúdo lido é igual ao conteúdo escrito
        self.assertEqual(content, self.test_content)

    def test_rename_file(self):
        """precisa escrever o arquivo antes de renomeá-lo"""
        self.file_manager.write(self.test_content)
        new_file_name = "renamed_file.txt"

        # Renomeia o arquivo de teste
        self.file_manager.rename(new_file_name)

        # Verifica se o novo nome de arquivo foi atribuído corretamente
        self.assertEqual(self.file_manager.file_name, new_file_name)

        # Verifica se o arquivo antigo não existe mais
        self.assertFalse(os.path.exists(self.test_file_path))

        # Verifica se o novo arquivo existe
        self.assertTrue(os.path.exists(new_file_name))

    def test_get_file_extension(self):
        # Obtém a extensão do arquivo de teste
        file_extension = self.file_manager.get_file_extension()

        # Verifica se a extensão obtida é igual à extensão esperada
        self.assertEqual(file_extension, ".txt")

    def test_check_dir_exist(self):
        # Verifica se um diretório existente é detectado corretamente
        self.assertTrue(self.file_manager.check_dir_exist("."))

        # Verifica se um diretório inexistente é detectado corretamente
        self.assertFalse(self.file_manager.check_dir_exist("nonexistent_directory"))

    def test_create_dir(self):
        new_directory = "new_directory"

        # Cria um novo diretório
        self.file_manager.create_dir(new_directory)

        # Verifica se o diretório foi criado corretamente
        self.assertTrue(os.path.isdir(new_directory))

        # Remove o diretório após o teste
        os.rmdir(new_directory)

    def test_check_file_exist(self):
        # Verifica se um arquivo existente é detectado corretamente
        self.file_manager.write(self.test_content)
        self.assertTrue(self.file_manager.check_file_exist())

    def test_stat(self):
        # Escreve conteúdo no arquivo de teste
        self.file_manager.write(self.test_content)

        # Obtém as informações estatísticas do arquivo
        file_stat = self.file_manager.stat()

        # Verifica se o tamanho do arquivo é igual ao tamanho do conteúdo escrito
        self.assertEqual(file_stat.st_size, len(self.test_content))

        # Verifica se o arquivo existe
        self.assertTrue(os.path.exists(self.test_file_path))

if __name__ == '__main__':
    unittest.main()
