import MapReduce
import sys

mr = MapReduce.MapReduce()

# key has to be the joined property
def mapper(record):
	key = record[1] #order_id
	value = record
	mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
	orders = []
	line_items = []
	for value in list_of_values:
		if value[0] == 'line_item':
			line_items.append(value)
		else:
			orders.append(value)

	for order in orders:
		for line_item in line_items: #order_id equals
			if order[1] == line_item[1]:
				mr.emit((order + line_item)) 

if __name__ == '__main__':
	input_file = open(sys.argv[1])
	mr.execute(input_file, mapper, reducer)