
from datetime import datetime
import sqlite3
db_name = 'database.db'
def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result
def RegistrarVenta():
    # SE CREA UN ARCHIVO SI NO EXISTE Y SE ABRE, SI EXISTE SOLO SE ABRE. EN EL ARCHIVO SE VAN A REGISTRAR UNA VENTA
    print("Escogio registrar una venta")
    print("Seleccione el numero de productos a registrar")
    folv=0
    now = datetime.now()
    diaventa = now.day
    mesventa = now.month
    anioventa = now.year
    fecha = str(diaventa)+"/"+str(mesventa)+"/"+str(anioventa)
    print("Fecha: "+fecha)
    numart = int(input("Escriba la cantidad de productos: "))
    preciototal = 0
    descantpre = ""
    for i in range(numart):
        descart = input("Escriba la descripcion del producto "+str(i+1)+": ")
        cantidad = int(input("Escriba la cantidad de piezas: "))
        precioventa = float(input("Escriba el precio de venta de cada articulo: "))
        preciototal = precioventa * cantidad + preciototal
        descantpre = descart +" x"+str(cantidad)+" $"+str(precioventa)+"c/u\r\n"+descantpre
    print("El monto total es de $"+ str(preciototal))
    query = 'INSERT INTO Ventas VALUES(NULL, ?, ?, ?)'
    parameters = (descantpre, preciototal, fecha)
    run_query(query,parameters)
    query = 'SELECT * FROM Ventas'
    folios = run_query(query)
    mayor=[]
    for row in folios:
            mayor.append(row[0])
    print("El folio es: "+str(max(mayor)))
def ConsultarVenta():
    folenc = False
    print("Escogio consultar una venta")
    foliocon = int(input("Escriba el folio de la venta: "))
    query = 'SELECT * FROM Ventas'
    folios = run_query(query)
    for row in folios:
        if row[0] == foliocon:
            print("Folio: " + str(row[0]))
            print("Fecha: " + str(row[3]))
            print("Descripcion, cantidad y costo de cada producto: \n" + str(row[1]))
            print("Precio total: $" + str(row[2]))
            folenc = True
    if not folenc:
        print("Folio no encontrado")

    return 0

    return 0
def ObtenerReporte():
    fechano = False
    print("Escogio obtener un reporte de ventas")
    dia = input("Escriba el dia[dd]: ")
    mes = input("Escriba el mes[mm]: ")
    anio = input("Escriba el anio[aaaa]: ")
    fecharep = str(dia)+"/"+str(mes)+"/"+str(anio)
    query = 'SELECT * FROM Ventas ORDER BY folio ASC'
    reporte = run_query(query)
    for row in reporte:
        if row[3] == fecharep:
            print("Folio: " + str(row[0]))
            print("Descripcion, cantidad y costo de cada producto: \n" + str(row[1]))
            print("Precio total: $" + str(row[2]))
            print("----------------------------------------------------")
            fechano = True
    if not fechano:
        print("Fecha no encontrada")

    return 0

opc = 0
while (opc!=4):
    print("Seleccione:\n  1. Registrar Venta \n 2. Consultar \n 3. Obtener un reporte de ventas para una fecha específica\n4.Salir ")
    opc = int(input("Opcion: "))
    if opc == 1:
        RegistrarVenta()
    elif opc == 2:
        ConsultarVenta()
    elif opc == 3:
        ObtenerReporte()
    elif opc == 4:
        print("Gracias por usar el programa")
    else:
        print("Opcion incorrecta")