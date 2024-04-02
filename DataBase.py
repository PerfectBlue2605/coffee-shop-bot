import sqlite3 as sq
from datetime import date

with sq.connect('coffee_art') as con:
    cur = con.cursor()  # Cursor

    cur.execute("""SELECT name FROM milk""")
    names = cur.fetchall()

    cur.execute("""SELECT count FROM milk""")
    count = cur.fetchall()

def milk_output(names,count):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute("""SELECT name FROM milk""")
        names = cur.fetchall()

        cur.execute("""SELECT count FROM milk""")
        count = cur.fetchall()
    result = ''
    x = 0
    for line in names:
        result+=(str(line).strip("'(),'")+' '+str(count[x]).strip("(,)")+'\n')
        x+=1
    return(result)

def coffee_output():
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute("""SELECT name FROM coffee""")
        names = cur.fetchall()

        cur.execute("""SELECT count FROM coffee""")
        count = cur.fetchall()
    result = ''
    x = 0
    for line in names:
        result+=(str(line).strip("'(),'")+' '+str(count[x]).strip("(,)")+'г'+'\n')
        x+=1
    return(result)

def bank_output():
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute("""SELECT bank FROM bank""")
        names = cur.fetchall()

    result = ''
    for line in names:
        result+=(str(line).strip("'(),'"))
    return(result)

def stuff_output():
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute("""SELECT name FROM stuff""")
        names = cur.fetchall()

        cur.execute("""SELECT count FROM stuff""")
        count = cur.fetchall()
    result = ''
    x = 0
    for line in names:
        result+=(str(line).strip("'(),'")+' | '+str(count[x]).strip("(',')")+'\n')
        x+=1
    return(result)

def get_id(name):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        if name != '+1' or '+5' or '-1' or '-5':
            cur.execute(f"""SELECT name_id FROM milk WHERE name == "{name}" """)
            item_id = cur.fetchone()
    return (item_id)

def clear_temp():
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''DELETE FROM temp''')

def set_var(name):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        if type(name) == str:
            cur.execute(f'''INSERT INTO temp (var) VALUES ('{name}')''')

def get_var(id):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''SELECT var FROM temp WHERE id == {id}''')
        var = cur.fetchone()
    return str(var).strip("'(),'")

def add_one(table,choosen_milk):
    print(table,choosen_milk)
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''UPDATE {table} SET count = count + 1 WHERE name == "{choosen_milk}"''')

def add_five(table,choosen_milk):
    print(table,choosen_milk)
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''UPDATE {table} SET count = count + 5 WHERE name == "{choosen_milk}"''')

def reduce_one(table,choosen_milk):
    print(table,choosen_milk)
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''UPDATE {table} SET count = count - 1 WHERE name == "{choosen_milk}"''')

def reduce_five(table,choosen_milk):
    print(table,choosen_milk)
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''UPDATE {table} SET count = count -5 WHERE name == "{choosen_milk}"''')

def change_value_coffee(table, choosen_coffee, value):
    print(table, choosen_coffee)
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        cur.execute(f'''UPDATE {table} SET count = {value} WHERE name == "{choosen_coffee}"''')

def bank_change(value):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        try:
            cur.execute(f'''UPDATE bank SET bank = {value} ''')
        except Exception:
            return(False)


def stuff_change(name,value):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor
        if value == 'Нет':
            cur.execute(f'''UPDATE stuff SET count = 'Нет' WHERE name == "{name}" ''')
        elif value == 'Есть':
            cur.execute(f'''UPDATE stuff SET count = 'Есть' WHERE name == "{name}"  ''')

def get_stat():
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute("""SELECT bank FROM bank""")
        bank = str(cur.fetchone())

        cur.execute("""SELECT name FROM milk""")
        names = cur.fetchall()

        cur.execute("""SELECT count FROM milk""")
        count = cur.fetchall()

        cur.execute("""SELECT count FROM coffee WHERE name = 'Кофе'""")
        coffee_count = str(cur.fetchone())

        cur.execute("""SELECT name FROM coffee WHERE name = 'Кофе'""")
        coffee_name = str(cur.fetchone())
    result = ''
    x = 0
    for line in names:
        result += (str(line).strip("'(),'") + ' ' + str(count[x]).strip("(,)") + '\n')
        x += 1
    return (f"""{date.today()}\n\nКасса\n{bank.strip("'(),'")}₽\n\n{result}\n{coffee_name.strip("'(),'")}\n{coffee_count.strip("'(),'")}г""")

def stock_check(table,name):
    with sq.connect('coffee_art') as con:
        cur = con.cursor()  # Cursor

        cur.execute(f"""SELECT count FROM {table} WHERE name == '{name}'""")
        stock = cur.fetchall()
        for x in stock:
            for i in x:
                stock = i
    return(stock)










milk_output(names,count)

