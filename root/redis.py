import picoredis as pr
import urandom as ur

#Connect to database
ur.seed(444)
r = pr.Redis(host='128.197.176.179')
r.auth('microfaas')
people = {"Johnny": {"spent":0, "balance":ur.getrandbits(8)}, "Jacky": {"spent":0, "balance":ur.getrandbits(8)}, "Jenny": {"spent":0, "balance":ur.getrandbits(8)}}
		
#Create entries
for name, desc in people.items():
	s = "{name} has {b} and spent {s}"
	s= s.format(name=name, b=desc['balance'], s=desc['spent'])
	print(s)
	print(r.hmset(name, 'balance', desc['balance'], 'spent', desc['spent']))

#Modify data
for i in range(10):
	r.multi()
	r.hincrby("Jenny", "spent", 1)
	r.hincrby("Jenny", "balance", -1 * 1)
	r.hincrby("Johnny", "spent", 1)
	r.hincrby("Johnny", "balance", -1 * 1)
	r.hincrby("Jacky", "spent", 1)
	r.hincrby("Jacky", "balance", -1 * 1)
	r.exec()
#Print data
for person in ["Jacky", "Jenny", "Johnny"]:
	print(person)
	print(r.hgetall(person))
#Delete all
r.flushall()
