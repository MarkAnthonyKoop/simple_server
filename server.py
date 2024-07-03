# server.py

import os
from flask import Flask, jsonify, request
import ssl
from base64 import b64encode, b64decode

from simple_server.codebase_interface.send_command.send_command import send_command

localhost_only = False
app = Flask(__name__)

def check_auth(header_value):
    # Expected format: Basic base64_encoded_credentials
    try:
        #print("entering check_auth")
        method, encoded_credentials = header_value.split()
        #print(f"method {method} encoded_cred {encoded_credentials}")
        if method.lower() != 'basic':
            #print(f"method lower is '{method.lower()}'")
            return False
        envpw = os.environ.get('CODE_PLANNER_API_KEY')
        #print(f"envpw {envpw}  enc creds {encoded_credentials}")
        return encoded_credentials == envpw
    except Exception as e:
        print(f"error is {e}")
        return False

def fails_auth():
    if localhost_only:
        return False
    auth_header = request.headers.get('Authorization')
    #print(f"auth header is ",auth_header)
    if auth_header and check_auth(auth_header):
        return False
    print("failed auth")
    return True

@app.route('/qpe1was4fsd/code_baseinterface/send_command', methods=['POST'])
def route_send_command():
    if fails_auth():
        return "Not Found", 404
    command = request.json
    return jsonify(send_command(command))

if __name__ == "__main__":
    # Manually create an SSL context
    if not localhost_only:  #skip if localhost
        print("starting host...")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('cert.pem', 'key.pem')
        context.load_verify_locations('cabundle.pem')
        print("started host--changing working directory to ~/sandbox")
        # Change the HOME environment variable for the current Python process
        #os.environ['HOME'] = '/home/x/sandbox'
        os.environ['SIMPLE_SERVER'] = 'TRUE'
        #os.chdir("C:/Users/x/sandbox")
        #os.chdir("/home/x/sandbox")
        #os.chdir("c:/cygwin64/home/x/sandbox")
        #os.chdir("c:/Users/x/sandbox")
        
    if localhost_only:  
        app.run(host='localhost', port=8000) #for testing
    else:
        print("app.run...")
        app.run(host='0.0.0.0', port=443, ssl_context=context) #current
        print("DONE!!!!")
    #app.run(host='0.0.0.0', port=443, ssl_context=context, debug=True)
    
