# Does what it says on the tin.
# Note that it takes a while to read all the mdb thingies.
# To run pandas_access successfully, install mdbtools through whatever you need.
# -Matt

import pandas
import numpy as np
import pandas_access

DATASET = "./FDOC_January_2017.mdb"

if __name__ == "__main__":
	table_list = []
	for tablename in pandas_access.list_tables(DATASET):
		print(tablename)
		table_list.append(tablename)

	tables_dict = {}
		
	for table in table_list[0:2]: #doing more makes it take forever.
		tables_dict[table] = pandas_access.read_table(DATASET, table)

