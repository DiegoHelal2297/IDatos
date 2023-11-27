import psycopg2

# Se realiza un mapeo de los datos obtenidos por las APIs a un esquema de base de datos
def insert_busqueda(elem, peso_gr, costo_envio_UY, costo_envio_USA, ml, ebay):
    # Establece una conexión con la base de datos
    conn = psycopg2.connect(
        host="localhost",
        database="idatos",
        user="postgres",
        password="postgres"
    )

    # Crea un cursor
    cur = conn.cursor()

    # Inserta datos en la tabla busqueda
    cur.execute("""
        INSERT INTO busqueda (articulo, peso)
        VALUES (%s, %s) RETURNING id
    """, (elem, peso_gr))

    # Obtiene el ID de la última búsqueda insertada
    busqueda_id = cur.fetchone()[0]

    for clave, valor in ml.items():
        # Inserta datos en la tabla resultado
        cur.execute("""
            INSERT INTO resultado (titulo, precio, moneda, url_resultado, busqueda_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (clave, valor['price'], valor['currency_id'], valor['URL'], busqueda_id))

        # Inserta datos en la tabla ml
        cur.execute("""
            INSERT INTO ml (titulo, costoEnvio)
            VALUES (%s, %s)
        """, (clave, costo_envio_UY))

    for clave, valor in ebay.items():
        # Inserta datos en la tabla resultado
        cur.execute("""
            INSERT INTO resultado (titulo, precio, moneda, url_resultado, busqueda_id) 
            VALUES (%s, %s, %s, %s, %s)
        """, (clave, valor['price'], valor['currency_id'], valor['URL'], busqueda_id))
        
        # Inserta datos en la tabla ebay
        cur.execute("""
            INSERT INTO ebay (titulo, costoEnvioDesdeUSA, impuestosAduana) 
            VALUES (%s, %s, %s)
        """, (clave, costo_envio_USA, valor['taxes']))

    # Confirma los cambios
    conn.commit()

    # Cierra el cursor y la conexión
    cur.close()
    conn.close()