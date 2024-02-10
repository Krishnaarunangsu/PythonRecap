from pyspark.sql import Row
assert(Row(name="Alice", age=11).asDict() == {'name': 'Alice', 'age': 11})

row = Row(key=1, value=Row(name='a', age=2))
assert (row.asDict() == {'key': 1, 'value': Row(name='a', age=2)})

assert(row.asDict(True) == {'key': 1, 'value': {'name': 'a', 'age': 2}})
