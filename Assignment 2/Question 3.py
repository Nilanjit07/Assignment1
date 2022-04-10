# Creating dictionary which contains lists
country = {
	"India": ["Delhi", "Maharastra", "Haryana",
			"Uttar Pradesh", "Himachal Pradesh"],
	"Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku"],
	"United States": ["New York", "Texas", "Indiana",
					"New Jersey", "Hawaii", "Alaska"]
}
for i in country['Japan']:
	print(i)
for i in country['India']:
	print(i)
for i in country['United States']:
	print(i)


# get list of values from dictionary
data = {'manoja': 'java', 'tripura': 'python',
		'manoj': 'statistics', 'manoji': 'cpp'}

[data[i] for i in data]
