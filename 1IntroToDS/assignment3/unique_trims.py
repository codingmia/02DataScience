import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0] 
	value = record[1]
	mr.emit_intermediate(value[:-10], 1)

def reducer(key, list_of_values):
	mr.emit(key)


if __name__ == '__main__':
	input_file = open(sys.argv[1])
	mr.execute(input_file, mapper, reducer)