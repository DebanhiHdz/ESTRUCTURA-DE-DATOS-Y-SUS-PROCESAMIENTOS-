import sys
import sqlite3
from sqlite3 import Error
import datetime
import time
# SE CREA LA TABLA CON LA CUAL SE GUARDARAN LOS DATOS
try:
    with sqlite3.connect("Negocio_Cosmeticos.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE Tienda_deCosmeticos (Descripcion_Articulo TEXT NOT NULL, Cantidad_Vendidas NUMBER NOT NULL, Precio_Articulo NUMBER NOT NULL, Fecha_Venta DATE TEXT NOT NULL);")
        print("Tablas creadas exitosamente! \n")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
def registar_ventas (descripcion_art, cantidad_piezasVendidas, precio_deVenta, fecha_deVenta):
    try:
        with sqlite3.connect("Negocio_Cosmeticos.db") as conn:
            c = conn.cursor()
            valores = {"Descripcion_Articulo":descripcion_art, "Cantidad_Vendidas":cantidad_piezasVendidas, "Precio_Articulo":precio_deVenta, "Fecha_Venta":fecha_deVenta}
            c.execute("INSERT INTO Tienda_deCosmeticos VALUES(:Descripcion_Articulo,:Cantidad_Vendidas,:Precio_Articulo,:Fecha_Venta)", valores)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
# SE DEFINE EL MENU PRINCIPAL        
def menu_principal():
    print("\n- MENÚ DEL SISTEMA -")
    print("[1] Registrar una venta")
    print("[2] Consultar ventas de un día específico")
    print("[3] Salir")
    
ciclo = True
while ciclo:
    continuar = True
    menu_principal()
    opcion = int(input("Eliga el número de la opción que desee: "))
    
    if opcion == 1:
        
        while continuar:
#             SE DEFINE EL MENU DE LOS ARTICULOS DE LA TIENDA
            print("\n MENÚ ARTICULOS")
            print("-DESCRIPCION-         -PRECIO-")
            print("SOMBRAS                 $400")
            print("LABIAL MATE             $100")
            print("RIMEN                   $50")
            print("BASE LIQUIDA            $200")
            print("ILUMINADOR              $180")
            print("PRIMER                  $250")
            print("RUBOR                   $80")
            descripcion_art = input("Ingrese la descripcion del articulo: ").upper()
            cantidad_piezasVendidas = int(input("Ingrese la cantidad de piezas que se vendieron: "))
            while cantidad_piezasVendidas<0:
                print("No se admiten valores negativos")
                cantidad_piezasVendidas = int(input("Ingrese la cantidad de piezas que se vendieron: "))
            precio_deVenta = int(input("Ingrese el precio de venta por articulo: "))
            while precio_deVenta<0:
                print("No se admiten valores negativos")
                precio_deVenta = int(input("Ingrese el precio de venta por articulo: "))
            fecha_deVenta = datetime.date.today() 
            monto_total = (cantidad_piezasVendidas*precio_deVenta)
            registar_ventas = (descripcion_art, cantidad_piezasVendidas, precio_deVenta, fecha_deVenta)
            print(f"El monto total a pagar es de ${monto_total}")
            print("---VENTA AGREGADA---")
            registrar = int(input("Desea registrar una nueva venta? Seleccione '0' (cero) para regresa a menu principal: "))
            if registrar == 0:
                continuar = False
#  BUSCAR VENTAS POR LA FECHA               
    if opcion == 2:
        print ("Formato para buscar la fecha: [2020-12-30]")
        fecha = input("Ingrese la fecha de la venta que desea consultar: ")

        try:
            with sqlite3.connect("Negocio_Cosmeticos.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"Fecha_Venta":fecha}
                mi_cursor.execute("SELECT * FROM Tienda_Cosmeticos WHERE Fecha_Venta = :Fecha_Venta;",valores)
                registro = mi_cursor.fetchall()
                
                print("Fecha_Venta\tCantidad/Precio/Descripcion_Articulo")
                if registro:
                    for Descripcion_Articulo,Cantidad_Vendidas,precio_deVenta,Fecha_Venta in registro:
                        print(f"{Fecha_Venta} \t", end="")
                        print(f"{Cantidad_Vendidas}\t{precio_deVenta}\t{Descripcion_Articulo}")

        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
#   SE SALE DEL PROGRAMA  
    elif opcion == 3:
        ciclo = False
    else:
        print(f"La opción {opcion} no es valida, asegurese de capturar una opción numerica. \n")
        
print("GRACIAS POR UTILIZAR EL PROGRAMA")
