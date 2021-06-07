from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "imaginary.quals.beginners.seccon.jp", 1337
#1337i': []の取得
s, f = sock(HOST, PORT)
for _ in range(6): read_until(f)
read_until(f,"> ")
s.send(b"1\n")
read_until(f,"part> ")
s.send(b"123\n")
read_until(f,"part> ")
s.send(b"123\n")

for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"1\n")
read_until(f,"part> ")
s.send(b"1\n")
read_until(f,"part> ")
s.send(b"1337\n")

for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"4\n")
print(read_until(f))
print(read_until(f))
c1 = read_until(f).strip()
s.close()
print(c1)
print("part 1 finish")

# 'の取得
s, f = sock(HOST, PORT)
for _ in range(6): read_until(f)
read_until(f,"> ")
s.send(b"1\n")
read_until(f,"part> ")
s.send(b"1234\n")
read_until(f,"part> ")
s.send(b"1234\n")
for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"1\n")
read_until(f,"part> ")
s.send(b"123\n")
read_until(f,"part> ")
s.send(b"123\n")
for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"4\n")
#read_until(f)
print(read_until(f))
print(read_until(f))
c2 = read_until(f).strip()
print("get c2")
for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"3\n")
read_until(f,"String> ")
print(str(c2[:64]+c1[64:]))
s.send(str(c2[:64]+c1[64:]).encode()+b"\n")

for _ in range(4): print(read_until(f))
for _ in range(5): read_until(f)
read_until(f,"> ")
s.send(b"5\n")

while True: print(read_until(f))

s.close()


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

