import gmpy2
from Crypto.Util.number import *
import math

def algo1(p,q,e,gg):
	phi = ((p-1)*(q-1))//e
	while True:
		ge = pow(gg,phi,p*q)
		if ge != 1: return ge
		gg += 1
		

n = 169221770188000341507764005330769042705223611712308424479120192596136318818708135716157255550936563268500310852894489839470320516645317338473018150885997977008925839939560590924435380239519554475266121835753044660177349444503693993991253475530436734034224314165897550185719665717183285653938232013807360458249
e = 17
c = 100233131931360278332734341652304555814094487252151131735286074616555402795190797647001889669472290770925839013131356212574455274690422113278015571750653365512998669453161955302008599029919101244702933443124944274359143831492874463245444294673660944786888148517110942002726017336219552279179125115273728023902

tmp, ch = gmpy2.iroot(n,2)
#print(tmp) tmp = 13008526826201356667891590694678121516071641430494347349438757349219893000439927852950504383765791466428599814640460028507882213264934492728368742844734364
tmp = int(tmp)-1
cnt = 0
while True:
	if n%tmp == 0:
		p = tmp
		q = n//p
		print(p)
		print(q)
		assert n==p*q
		phi = ((p-1)*(q-1))//e
		d = inverse(17,phi)
		print("d:",d)
		m = pow(c,d,n)
		#long_to_bytes(m)
		l = 1
		fin = True
		while fin:
			print(l)
			"""
			for i in range(1,e+1):
				mm = m*i
				mes = long_to_bytes(mm%n)
				if b"ctf4b" in mes:
					print(mes)
					fin = False
					break
			"""
			mm = m*l
			mes = long_to_bytes(mm%n)
			if b"ctf4b" in mes:
				print(mes)
				fin = False
			l *= algo1(p,q,e,l)
			l %= n
		#print(math.gcd(17,phi))
		#print("d:",d)
		#print((e*d)%phi)
		#m = pow(c,d,n)
		#mm,ch = gmpy2.iroot(m,17)
		#print(ch)
		#print(long_to_bytes(m))
		#cc = c
		#while True:
		#	m,ch = gmpy2.iroot(cc,17)
		#	if ch:
		#		print(long_to_bytes(int(m)))
		#		break
		#	cc += n
		break
	tmp -= 2
	cnt += 1
	if cnt%100000 == 0: print(cnt)
