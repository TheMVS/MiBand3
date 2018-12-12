import crc16
crc = 0xFFFF
with open("Mili_wuhan.res") as f:
      while True:
        c = f.read(1) #takes 20 bytes :D
        if not c:
          print "Update Over"
          break
        cInt = int(c.encode('hex'), 16)
        crc = ((crc >> 8) | (crc << 8)) & 0xFFFF
        crc ^= (cInt & 0xff)
        crc ^= ((crc & 0xff) >> 4)
        crc ^= (crc << 12) & 0xffff
        crc ^= ((crc & 0xFF) << 5) & 0xffff
        # raw_input()
crc &= 0xffff
print(crc)
print(hex(crc & 0xff))
print(hex((crc >> 8) & 0xff))
