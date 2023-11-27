import os
import sys
import pandas as pd
import LlamadasAPI
import PuntoMio
import BaseDeDatosConnect

from decouple import config
from textwrap import wrap

def main(elem, costo_envio_UY, peso_gr):
    costo_envio = 0
    if (peso_gr != 0):
        costo_envio = PuntoMio.obtener_precio_por_peso(peso_gr)

    # Credentials
    API_KEY = config('API_KEY_Ebay', default='None')

    # Hago el llamado a las APIs
    mercado_libre = LlamadasAPI.find_ML(elem)
    ebay = LlamadasAPI.find_ebay(elem, API_KEY)

    BaseDeDatosConnect.insert_busqueda(elem, peso_gr, costo_envio_UY, costo_envio, mercado_libre, ebay)

if __name__ == "__main__":
    # Elemento a buscar
    arg1 = sys.argv[1]
    # Costo envio UY
    arg2 = sys.argv[2]

    # Peso opcional
    if len(sys.argv) > 3:
        arg3 = sys.argv[3]
    else:
        arg3 = 0

    main(arg1, arg2, arg3)