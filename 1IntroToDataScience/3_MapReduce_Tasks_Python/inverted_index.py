import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0] #document id
	value = record[1] # document content
	words = value.split()
	for w in words:
		mr.emit_intermediate(w, record[0]) # [word, docId]

def reducer(key, list_of_values):
	values=[]
	for value in list_of_values:
		if value not in values:
			values.append(value)
	mr.emit((key, values)) # [word, list of docIds]


if __name__ == '__main__':
	input_file = open(sys.argv[1])
	mr.execute(input_file, mapper, reducer)