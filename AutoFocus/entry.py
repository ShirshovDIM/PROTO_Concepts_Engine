import subprocess
import sys
import os
import pathlib


if __name__ == "__main__":

    current_dir = pathlib.Path().resolve()

    install_libs = f"python -m pip install -r {current_dir}\\AutoFocus\\requirements.txt"
    run_debugged = f"{current_dir}\\AutoFocus\\ext\\Chrome\\Application\\chrome.exe --remote-debugging-port=9222 --user-data-dir={current_dir}\\temp\\"
    run_builder = f"python -s {current_dir}\\AutoFocus\\driver_setup.py"
    
    subprocess.run(install_libs)

    commands = [subprocess.Popen(command) for command in (run_builder, run_debugged)]
    

    for i, command in enumerate(commands):
        try:

            command.wait()

        except Exception as ex:
            print(ex)
            print(f"command {i} executed with status 0")

        else: 
             print(f"command {i} executed with status 1")


            