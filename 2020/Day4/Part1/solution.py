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

valid = 0
for record in records:
	if BIRTH_YEAR in record and ISSUE_YEAR in record and EXPIRATION_YEAR in record and HEIGHT in record and HAIR_COLOR in record and EYE_COLOR in record and PASSPORT_ID in record:
		valid += 1

print(valid)