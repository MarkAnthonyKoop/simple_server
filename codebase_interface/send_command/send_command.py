from subprocess import run
from simple_server.mylog.mylog import mylog
import sys

def send_command(command):
    # Log the command being executed
    print("hello")
    print(f"Executing command: {command['commandString']}")
    
    # Execute the command
    #result = run(command["commandString"].strip(), shell=True, capture_output=True, text=True, 
    result = run(['c:/cygwin64/bin/bash.exe', '--login','-i','-c', command["commandString"].strip()], capture_output=True, text=True)
    print(f"result is:\n{result}")
    #result = run(['wsl', 'bash', '-c', command["commandString"].strip(),capture_output=True, text=True])
    #result = run(command["commandString"].strip(), shell=True, capture_output=True, text=True, executable='c:/windows/System32/WindowsPowerShell/v1.0/powershell.exe')
    
    # Prepare the result dictionary
    result_dict = {
        'args': result.args,
        'command': command['commandString'],
        'returncode': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr
    }
 
    mylog(result_dict)
    return result_dict


if __name__ == "__main__":
    command_string = " ".join(sys.argv[1:])
    command = {'commandString': command_string}
    send_command(command)
