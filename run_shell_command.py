import subprocess


def run_shell_command(cmd):
    cmd_list = cmd.split(' ')
    sp = subprocess.run(cmd_list, stdout=subprocess.PIPE)
    print(sp.stdout.decode("utf-8"))
    print(sp.returncode)


if __name__ == "__main__":
    run_shell_command('echo shell cmd test!!')
