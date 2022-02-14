import os
import paramiko
from dotenv import load_dotenv

load_dotenv()

'''
This script uses the paramiko module to make a connection to an sftp server. 

You need to set the path for the id_rsa file and the keypass for that file.

If you want to upload any files in the server you must define the local and remote paths.

'''


def create_client(host, port, username, keypath, keypass):
    """

    host: The server address
    port: The port
    username: Specify the name of the user
    keypath: Specify the location of the id_rsa file in your machine
    keypass: Specify the password for the id_rsa key

    """
    transport = paramiko.Transport((host, port))
    mykey = paramiko.RSAKey.from_private_key_file(keypath, keypass)
    print("Connecting...")
    transport.connect(username=username, pkey=mykey)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected.")
    return sftp


host = os.getenv("host")
port = int(os.getenv("port"))
username = os.getenv("username")
keypath = os.getenv("keypath")
keypass = os.getenv("keypass")

sftpclient = create_client(host=host, port=port, username=username, keypath=keypath, keypass=keypass)

# Uncomment of you want to upload files
# localPath = ""
# remotePath = ""

# sftp.put(localpath=localPath, remotepath=remotePath)

dirlist = sftpclient.listdir('.')
for row in dirlist:
    print(row)

sftpclient.close()

productsList = ["S02P02", "S06P01", "S06P04"]