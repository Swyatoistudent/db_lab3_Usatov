import csv
import psycopg2

OUTPUT_FILE_T = 'Usatov{}.csv'

TABLES = [
    'car_list',
    'cars',
    'engine',
    'engine_copy',
    'lot',
]

config = psycopg2.connect(database="Usatov_Lab2", user="Usatov", password="123", host="localhost", port="5432")

with config:
    cur = config.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])