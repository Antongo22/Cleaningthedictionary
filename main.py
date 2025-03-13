def gettext(file_name : str) -> (dict, int, int):
	f = open(file_name, 'r', encoding="utf-8")
	linearray = f.readlines()
	f.close()
	return setword(linearray)

def setword(linearray : list[str]) -> (dict, int, int):
	pairs = {}
	for line in linearray:
		line = line.replace("\n", "")

		if line:
			pair = line.split(" - ")
			if len(pair) != 2:
				continue
			
			for p in pair:	p.strip()

			if pair[0] not in pairs:
				pairs[pair[0]] = pair[1]

	return pairs, len(linearray), len(pairs)

def write(pairs: dict):
    with open("output.txt", 'w', encoding="utf-8") as f:
        for key, value in pairs.items():
            f.write(f"{key} - {value}\n")

def main():
	inp = input("Введите путь к файлу:").replace("\"", "") 
	pairs, ll, cl = gettext(inp)
	write(pairs)
	print(pairs)
	print('Было -', ll)
	print('Стало -', cl)




if __name__ == '__main__':
	main()