import psycopg2
from pprint import pprint
import re
from collections import Counter


def most_freq_keyword():

    conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
    cursor = conn.cursor()
    cursor.execute("""select keywords from keywords""")

    data_rows = []


    for row in cursor:
        temp = re.sub(r'\W+', '', row[0])
        data_rows.append(temp)
    cursor.close()
    return data_rows


counts = Counter(most_freq_keyword())
pprint(counts)


