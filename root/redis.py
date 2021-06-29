import picoredis as pr
#Connect and auth into redis database
r = pr.Redis(host='128.197.176.179')
r.auth('microfaas')
people = {"Johnny": {"age":0, "points":0}, "Jacky": {"age":0, "points":0}, "Jenny": {"age":0, "points":0}}
#Create entries
for name, desc in people.items():
	print(name, desc)
	r.hmset(name, desc)

