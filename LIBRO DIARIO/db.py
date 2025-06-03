import sqlite3

def crear_db():
    conn = sqlite3.connect('libro_diario.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS asientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            glosa TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS detalles_asiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asiento_id INTEGER,
            cuenta TEXT,
            descripcion TEXT,
            debe REAL,
            haber REAL,
            FOREIGN KEY(asiento_id) REFERENCES asientos(id)
        )
    ''')
    conn.commit()
    conn.close()

def insertar_asiento(fecha, glosa, detalles):
    conn = sqlite3.connect('libro_diario.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO asientos (fecha, glosa) VALUES (?, ?)', (fecha, glosa))
    asiento_id = cur.lastrowid

    for item in detalles:
        cur.execute('''
            INSERT INTO detalles_asiento (asiento_id, cuenta, descripcion, debe, haber)
            VALUES (?, ?, ?, ?, ?)
        ''', (asiento_id, item["cuenta"], item["descripcion"], item["debe"], item["haber"]))

    conn.commit()
    conn.close()

def obtener_asientos():
    conn = sqlite3.connect('libro_diario.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM asientos')
    asientos = cur.fetchall()

    resultados = []
    for a in asientos:
        cur.execute('SELECT cuenta, descripcion, debe, haber FROM detalles_asiento WHERE asiento_id = ?', (a[0],))
        detalles = cur.fetchall()
        resultados.append({
            "id": a[0],
            "fecha": a[1],
            "glosa": a[2],
            "detalles": detalles
        })
    conn.close()
    return resultados
