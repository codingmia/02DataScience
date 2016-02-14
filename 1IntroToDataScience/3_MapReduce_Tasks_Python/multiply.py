import MapReduce
import sys

mr = MapReduce.MapReduce()
#[matrix, i, j, value]
def mapper(record):
	key = record[0] 
	# i, j, value
	value = (record[1], record[2], record[3])
	if key == 'a':
		for k in range(5):
			mr.emit_intermediate((value[0], k), ('a', value[1], value[2]))
	if key == 'b':
		for k in range(5):
			mr.emit_intermediate((k, value[1]), ('b', value[0], value[2]))	


def reducer(key, list_of_values):
	a_values = []
	b_values = []
	sum = 0

	for value in list_of_values:
		if value[0] == 'a':
			a_values.append(value)
		if value[0] == 'b':
			b_values.append(value)

	sum = 0
	for p in a_values:
		for q in b_values:
			product = 0
			if(p[1] == q[1]):
				product = p[2] * q[2]
				sum += product

	mr.emit((key[0], key[1], sum))

if __name__ == '__main__':
	input_file = open(sys.argv[1])
	mr.execute(input_file, mapper, reducer)