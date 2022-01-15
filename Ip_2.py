import socket  # ଏଠାରେ ଆମେ ଦୁଇଟି ମଡ୍ୟୁଲ୍, ସକେଟ୍ ଏବଂ ସମୟ ଆମଦାନୀ କରୁ
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ଏଠାରେ ଆମେ ଦୁଇଟି ମଡ୍ୟୁଲ୍, ସକେଟ୍ ଏବଂ ସମୟ ଆମଦାନୀ କରୁ
# କିମ୍ବା ହୋଷ୍ଟ

ଲକ୍ଷ୍ୟ = input('ଆପଣ କ’ଣ ସ୍କାନ୍ କରିବାକୁ ଚାହୁଁଛନ୍ତି?: ')

# ପରବର୍ତ୍ତୀ ରେଖା ଆମକୁ ip ଠିକଣା ଦେଇଥାଏ |
# ଲକ୍ଷ୍ୟସ୍ଥଳର
ଲକ୍ଷ୍ୟ_ip = socket.gethostbyname(ଲକ୍ଷ୍ୟ)
print('ହୋଷ୍ଟରେ ସ୍କାନ୍ ଆରମ୍ଭ କରିବା:', ଲକ୍ଷ୍ୟ_ip)


# function for scanning ports
def port_scan(port):
    try:
        s.connect((ଲକ୍ଷ୍ୟ_ip, port))
        return True
    except:
        return False

start = time.time()
# here we are scanning port 0 to 4

for port in range(5):
    if port_scan(port):
        print(f'ପୋର୍ଟ {port} ଖୋଲା ଅଛି')
    else:
        print(f'ପୋର୍ଟ {port} ବନ୍ଦ ଅଛି')

end = time.time()
print(f' ସମୟ ନିଆଯାଇଛି {end - start:.2f} seconds')

#
