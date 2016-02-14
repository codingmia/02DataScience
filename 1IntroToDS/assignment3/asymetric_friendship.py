import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0] #person
	value = record[1] # friend

	mr.emit_intermediate((key,value), 1)
	mr.emit_intermediate((value,key), 1)

def reducer(key, list_of_values):
	if len(list_of_values) == 1:
		mr.emit((key))


if __name__ == '__main__':
	input_file = open(sys.argv[1])
	mr.execute(input_file, mapper, reducer)