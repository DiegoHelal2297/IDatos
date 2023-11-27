import os
import re
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def obtener_precio_por_peso(peso_gr):
    # Hay que tener instalado chrome y chromedriver en el sistema
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    
    s = Service(r'/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s, options=options)

    # Accedo a punto mio
    driver.get('https://www.puntomio.uy/calculadora')

    # Encontrar el campo de entrada del peso y enviar el nuevo valor
    peso_input = driver.find_element(By.NAME, 'weight')
    peso_input.clear()
    peso_input.send_keys(peso_gr)  # Peso en gramos

    # Calcular
    calcular = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].sc-jIZahH.fjGkwA.sc-ciZhAO.gvDXuO')
    calcular.click()

    try:
        # Obtengo el campo y luego me quedo solo con el valor numerico, descartando la moneda
        total_a_pagar_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-gicCDI.dkdsym'))).text
        total_a_pagar = re.findall(r'\d+\.?\d*', total_a_pagar_elem)
        
        # Chequeo si encontré un valor numerico
        if not total_a_pagar:
            print("No se encontró un valor numérico.")
            return 0

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return 0

    finally:
        # Cerrar el navegador
        driver.quit()

    return float(total_a_pagar[0])