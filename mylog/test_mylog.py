from subprocess import run
from mylog import mylog

# Configure logging

def test_mylog():
    # Log the command being executed
    #logging.info(f"Executing command: {command['commandString']}")
    
    # Execute the command

    
    # Prepare the result dictionary
    result_dict = {
        'args': "the args",
        'returncode': "a rturncode",
        'stdout': "\n\nstdout\n\n",
        'stderr': "\n\nstde\n\n",
    }
 
    print("resultdict is ",result_dict)
    mylog(result_dict)
       
    return result_dict

test_mylog()

