import bcrypt

# server
HOST = '127.0.0.1'
PORT = 8222
HOST_KEY_FILE = 'ssh_host_key'

# ssh server, server
USERNAME = 'user'
PASSWORD = 'user' 
PASSWORDS = {
    USERNAME: bcrypt.hashpw(PASSWORD.encode(), bcrypt.gensalt())
}

# sftp server, server
SFTP_ROOT = "sftp_files" 