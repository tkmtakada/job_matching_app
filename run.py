from app.app import app
import socket

if __name__ == "__main__":
    if 'ec2' in socket.gethostname():  # EC2
        app.run(host='0.0.0.0', port=80)
    else:  # LOCAL
        app.run()
