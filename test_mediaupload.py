import subprocess
import os

class Tests:
    def test_initialize(self):
        console_commands = ["git clone https://github.com/ITP2-Projekt/itp2-demonstration", 'cmd /c "cd ./itp2-demonstration && setup_linux.txt']
        for cmd in console_commands:
            # output = subprocess.check_output(cmd, shell=True)
            os.system(cmd)

if __name__ == "__main__":
    Tests().test_initialize()
