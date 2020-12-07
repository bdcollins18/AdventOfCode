BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION_YEAR = "eyr"
HEIGHT = "hgt"
HAIR_COLOR = "hcl"
EYE_COLOR = "ecl"
PASSPORT_ID = "pid"
COUNTRY_ID = "cid"

f = open("input.txt")
record_string = f.read().replace(' ','\n')
record_strings = record_string.split('\n')
records = list()
record = dict()
for field in record_strings:
	if field != "":
		split_field = field.split(':')
		record[split_field[0]] = split_field[1]
	else:
		records.append(record)
		record = dict()

#records = [{"pid":"087499704", "hgt":"74in", "ecl":"grn", "iyr":"2012", "eyr":"2030", "byr":"1980", "hcl":"#623a2f"}]

valid = 0
for record in records:
	try:
		if len(record[BIRTH_YEAR]) != 4:
			continue
		birth_year = int(record[BIRTH_YEAR])
		if birth_year < 1920 or birth_year > 2002:
			continue
		if len(record[ISSUE_YEAR]) != 4:
			continue
		issue_year = int(record[ISSUE_YEAR])
		if issue_year < 2010 or issue_year > 2020:
			continue
		if len(record[EXPIRATION_YEAR]) != 4:
			continue
		expiration_year = int(record[EXPIRATION_YEAR])
		if expiration_year < 2020 or expiration_year > 2030:
			continue
		height_unit = record[HEIGHT][-2:]
		if height_unit == "in":
			height = int(record[HEIGHT][:-2])
			if height < 59 or height > 76:
				continue
		elif height_unit == 'cm':
			height = int(record[HEIGHT][:-2])
			if height < 150 or height > 193:
				continue
		else:
			continue
		hair_color = record[HAIR_COLOR]
		if len(hair_color) != 7:
			continue
		if hair_color[0] != '#':
			continue
		for c in hair_color[1:]:
			if c not in "0123456789abcdef":
				continue
		eye_color = record[EYE_COLOR]
		if eye_color not in ["amb","blu","brn","gry","grn","hzl","oth"]:
			continue
		passport_id = record[PASSPORT_ID]
		if len(passport_id) != 9:
			continue
		int(passport_id)
		valid += 1
	except:
		continue
print(valid)