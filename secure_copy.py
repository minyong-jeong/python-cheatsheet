import paramiko
from scp import SCPClient


class SSHManager:
    def __init__(self, hostname, username, password):
        self.ssh_client = self.create_ssh_client(hostname, username, password)

    def create_ssh_client(self, hostname, username, password):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname, username=username, password=password)

    def close_ssh_client(self):
        self.ssh_client.close()

    def send_file(self, local_path, remote_path):
        with SCPClient(self.ssh_client.get_transport()) as scp:
            scp.put(local_path, remote_path, preserve_times=True)

    def get_file(self, remote_path, local_path):
        with SCPClient(self.ssh_client.get_transport()) as scp:
            scp.get(remote_path, local_path)

    def send_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.readlines()

# ssh_manager = SSHManager("hostname", "username", "password")
# ssh_manager.send_file("local_path", "remote_path")
# ssh_manager.get_file('remote_path', 'local_path')
# ssh_manager.close_ssh_client()
