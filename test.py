# import sqlite3

# db = sqlite3.connect("School_stud.db")
# cusror = db.cursor()
# cusror.execute("create table if not exists student (id integer primary key, first_name text, last_name text, gender text, birth_date date, type_blood text, class text, perent_no integer, address text)")

# print("created ...")
# db.close()

import random

random1 = str(random.randint(100, 1000))
random2 = str(random.randint(100, 1000))
result = random1 + random2
print(len(result))

