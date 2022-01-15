# Python Program to Get IP Address
import socket      # Importing socket library
hostname = socket.gethostname()
def କମ୍ପ୍ୟୁଟର_ନାମ():
    print("ତୁମର କମ୍ପ୍ୟୁଟର ନାମ ହେଉଛି: " + hostname)
def କମ୍ପ୍ୟୁଟର_ଠିକଣା():
    IPAddr = socket.gethostbyname(hostname)
    print("ତୁମର କମ୍ପ୍ୟୁଟର ଠିକଣା ହେଉଛି: " + IPAddr)

