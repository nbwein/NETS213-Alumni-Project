import csv
with open('part_4_data.csv', 'rb') as csv_file:
	reader = csv.reader(csv_file, delimiter=',', quotechar='|')

	# skip header line
	next(reader)

	name_to_yes = {}
	for row in reader:
		row[23] = row[23].replace(',', '')
		name = row[23]

		yes = 0

		if 'yes' in row[14]:
			yes = 1

		if not name in name_to_yes.keys():
			name_to_yes[name] = yes

		else:
			name_to_yes[name] += yes


	with open('name_to_yes.csv', 'wb') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='|')

		for name in name_to_yes.keys():
			writer.writerow([name, name_to_yes[name]])