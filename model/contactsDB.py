import sqlite3
import os.path

def create_tables(*tables):
    for table_name in tables:
        db_conn.execute("create table if not exists {} (name text  primary key, phone integer not null, email text)".format(table_name))


def query_by_name(name):
    query_result = []

    db_cursor = db_conn.cursor()
    for row in db_cursor.execute("select * from contacts where name like ?", (name,)):
        query_result.append(row)

    return query_result


def query_by_email(email):
    query_result = []

    db_cursor = db_conn.cursor()
    for row in db_cursor.execute("select * from contacts where email = ?", (email,)):
        query_result.append(row)

    return query_result


def add_contact(name, phone, email):
    db_conn.execute("insert into contacts(name, phone, email) values(?, ?, ?)", (name, phone, email))
    db_conn.commit()


def get_all_contacts():
    result = []

    for row in db_conn.execute("select * from contacts"):
        result.append(row)

    return result


db_conn = sqlite3.connect("managerDB.sqlite")
create_tables('contacts')
