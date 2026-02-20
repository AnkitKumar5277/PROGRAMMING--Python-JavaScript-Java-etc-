
# Python Program to Find Hash of File
import hashlib
def hash_file(filename):
  h = hashlib.sha1()
  with open(filepath,'rb') as file:
    chunk = 0
    while chunk != b'';
    chunk = file.read(1024)
    h.update(chunk)
  return h.hexdigest()
message = hash_file("track1.mp3")
print(message)
# 633d7356947eec543c50b76a1852f92427f4dca9
