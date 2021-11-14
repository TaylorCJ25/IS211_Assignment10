import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
conn = create_connection("pets.db")


def select_all_person(conn, person_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM person where id =" + str(person_id))

    rows = cur.fetchall()
    if len(rows) >= 1:
        for row in rows:
            name = row[1] + " " + row[2]
            print(name + ", " + str(row[3]) + " year old")

        cur.execute(
            "SELECT * FROM pet where id =(SELECT pet_id FROM person_pet where person_id =" + str(person_id) + ")")
        pet_rows = cur.fetchall()

        for pet_row in pet_rows:
            print(name + " owns " + pet_row[1] + ",a " + pet_row[2] + " " + str(pet_row[3]) + " year old")
    else:
        print("Error: the person doesn't exist")


while True:
    person_id = input("Enter person's id or -1 to exit: ")
    if person_id != '-1':
        select_all_person(conn, person_id)
    else:
        break
    print()