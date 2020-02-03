from json import load, dump
t = "1017041764"
with open("dumpp.json", "r") as f:
	s = load(f)
	s.pop(t)
	for i in s:
		if i.isdigit():
			if "bot_list" in s[i] and t in s[i]["bot_list"]:
				print(s[i])
				s[i]["bot_list"].pop(s[i]["bot_list"].index(t))
				print(i)
	dump(s, open("dumpp.json", "w+", encoding="utf-8"), ensure_ascii=False, indent=4)
