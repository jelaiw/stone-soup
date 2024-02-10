```sh
>>> s = "41 6c 6c 20 69 6e 70 75 74 20 69 73 20 62 69 74 73 0a"
>>> bytes.fromhex(s)
b'All input is bits\n'
>>> bin(0x41)
'0b1000001'
>>> chr(0x41)
'A'
>>> chr(0b01000011), chr(0b0011000), chr(0b10010000)
('C', '\x18', '\x90')
>>> 
```
