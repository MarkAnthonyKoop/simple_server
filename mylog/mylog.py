import logging 

# Ensure the logging configuration is done outside the function to avoid reconfiguration on each call
logging.basicConfig(filename='command_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mylog(result):
    # Correctly accessing dictionary values
    log_string = f"""
\n\n-------------------------------send_command-----------------------------------
\n
    Command executed:\n{result['command']}\n\n\
    Command output:\n{result['stdout']}\n\n
"""
    if result['stderr']:
        log_string += f"    Command error: \n{result['stderr']}\n\n"
    log_string += "--------------------------------end_sendcmd-----------------------------------\n\n\n\n"
    logging.info(log_string) 


