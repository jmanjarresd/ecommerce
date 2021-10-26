from db import obtener_conexion

def get_Users():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    """ with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall() """
    conexion.close()
    return data

def agg_user(name, username, password, email, phone, country, date):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO users (name, username, password, email, phone, country, datetime) VALUES (?,?,?,?,?,?,?)",
                                        (name, username, password,email, phone, country, date))
    """ with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, username, password, email, phone, country, datetime) VALUES (?,?,?,?,?,?,?)",
                                        (name, username, password,email, phone, country, date)) """
    conexion.commit()
    conexion.close()

def edit_users(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users WHERE id_user = ?", (id))    
    data = cursor.fetchall()
    """ with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE id_user = ?", (id))    
        data = cursor.fetchall() """
    conexion.close()
    return data[0]

def update_users(name, username, password, email, phone, country, date, id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
            UPDATE users
            SET name = ?,
                username = ?,
                password = ?,
                email = ?,
                phone = ?,
                country = ?,
                datetime = ?
            WHERE id_user = ?
         """, (name, username, password, email, phone, country, date, id))
    #with conexion.cursor() as cursor:
    #    cursor.execute("""
    #        UPDATE products
    #        SET name = ?,
    #            category = ?,
    #            code = ?,
    #            price = ?,
    #            description = ?
    #        WHERE id_product = ?
    #     """, (product_name, category, code, price, product_description, id))
    conexion.commit()
    conexion.close()

def delete_users(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM users WHERE id_user = {0}".format(id))
    """ with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id_user = {0}".format(id)) """
    conexion.commit()
    conexion.close()

def agg_product(product_name, category, code, price, product_description, img):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO products (name, category, code, price, description, img) VALUES (?, ?, ?, ?, ?, ?)",
                                        (product_name, category, code, price, product_description, img))
    """ with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO products (name, category, code, price, description) VALUES (?, ?, ?, ?, ?)",
                                        (product_name, category, code, price, product_description)) """
    conexion.commit()
    conexion.close()

def get_Products():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    """ with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall() """
    conexion.close()
    return data

def edit_Products(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM products WHERE id_product = ?", (id))    
    data = cursor.fetchall()
    """ with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE id_product = ?", (id))    
        data = cursor.fetchall() """
    conexion.close()
    return data[0]

def update_products(product_name, category, code, price, product_description, id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
            UPDATE products
            SET name = ?,
                category = ?,
                code = ?,
                price = ?,
                description = ?
            WHERE id_product = ?
         """, (product_name, category, code, price, product_description, id))
    #with conexion.cursor() as cursor:
    #    cursor.execute("""
    #        UPDATE products
    #        SET name = ?,
    #            category = ?,
    #            code = ?,
    #            price = ?,
    #            description = ?
    #        WHERE id_product = ?
    #     """, (product_name, category, code, price, product_description, id))
    conexion.commit()
    conexion.close()

def delete_products(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM products WHERE id_product = {0}".format(id))
    """ with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE id_product = {0}".format(id)) """
    conexion.commit()
    conexion.close()

def login_users(username):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conexion.close()
    return user

def login_admins(username):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM admins WHERE username = ?", (username,))
    admin = cursor.fetchone()
    conexion.close()
    return admin