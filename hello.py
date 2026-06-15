"""Your first program on the supercomputer. Edit the message, then run it."""
import socket
import os

# Try changing this line in nano, then run the script again.
message = "Hello from the supercomputer!"

print(message)
print("I am running on:", socket.gethostname())
print("My current folder is:", os.getcwd())
