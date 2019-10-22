from json import load, dump
from datetime import datetime
try:
	with open("dumpp.json", "r", encoding="utf-8") as f:
		s = load(f)
except Exception as e:
	t = open("error_dump.log", "a+", encoding="utf-8")
	print(datetime.now(), file=t)
dump(s, open("copydump.json", "w+", encoding="utf-8"), ensure_ascii=False, indent=4)
