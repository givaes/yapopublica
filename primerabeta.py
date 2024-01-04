from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

# aqui donde se pone el titulo del modelo del vehiculo, en la terminal para publicar
titulo_personalizado = input("Ingrese el título personalizado: ")

# lista de titulos a publicar
titulos = [
   "Puerta",
"Parachoques delantero",
"Parachoques trasero",
"Parrilla delantera",
"Faros delanteros",
"Luces traseras",
"Espejos laterales",
"Capó",
"Puertas",
"Airbags",
"Parabrisas",
"Ventanas",
"Neumáticos",
"Ruedas",
"Suspensión delantera",
"Suspensión trasera",
"Dirección asistida",
"Sistema de escape completo",
"Tubo de escape",
"Convertidor catalítico",
"Frenos delanteros",
"Frenos traseros",
"Pastillas de freno",
"Discos de freno",
"Calipers de freno",
"Batería de automóvil",
"Alternador",
 "Motor de arranque",
"Radiador",
"Manguera del radiador",
"Termostato",
"Bomba de agua",
"Filtro de aire",
"Filtro de aceite",
"Filtro de combustible",
"Correa de transmisión",
"Tensor de correa",
"Correa de distribución",
"Embrague",
"Volante de inercia",
"Caja de cambios",
"Transmisión automática",
"Eje de transmisión",
"Amortiguadores",
"Muelles de suspensión",
"Bujes de suspensión",
"Bieletas de estabilizadora",
"Palieres",
"Junta homocinética",
"Soportes de motor",
"Soportes de transmisión",
"Tensor de cadena de distribución",
"Cadena de distribución",
"Válvula EGR",
"Sensor de oxígeno",
"Inyectores de combustible",
"Bomba de combustible",
"Bobinas de encendido",
"Bujías de encendido",
"Distribuidor de encendido",
"Árbol de levas",
"Culata",
"Bloque de motor",
"Radiador de calefacción",
"Compresor de aire acondicionado",
"Condensador de aire acondicionado",
"Filtro de aire acondicionado",
"Compresor de dirección asistida",
"Reservorio de dirección asistida",
"Bomba de dirección asistida",
"Correa de dirección asistida",
"Filtro de dirección asistida",
"Bomba de freno",
"Cilindro maestro de freno",
"Sonda lambda",
"Sensor de posición del cigüeñal",
"Sensor de posición del árbol de levas",
"Sistema de control de emisiones",
"Sistema de encendido electrónico",
"Fusibles",
"Relés",
"Interruptores eléctricos",
"Sistema de escape deportivo",
"Refrigerante de motor",
"Aceite de motor",
"Freno de mano",
"Pastillas de freno de estacionamiento",
"Tambores de freno",
"Sistema de luces auxiliares",
"Sensores de estacionamiento",
"Catalizador de alto flujo",
"Barra estabilizadora",
"Kit de distribución",
"Kit de embrague",
"Kit de frenos",
"Kit de correas de transmisión",
"Kit de cadena de distribución",
"Juego de juntas",
"Juego de anillos de pistón",
"Juego de cojinetes de biela",
"Juego de cojinetes de bancada",
"Juego de segmentos de pistón",
"Juego de válvulas",
"Aceite de caja de cambios",
"Líquido de frenos",
"Líquido de dirección asistida",
"Líquido de transmisión automática",
"Líquido de limpiaparabrisas",
"Silenciador de escape",
"Kit de rodamientos de rueda",
"Bomba de aceite",
"Caja de dirección",
"Sensores de ABS",
"Bomba de freno ABS",
"Sensor de velocidad de la rueda",
"Sensor de presión de neumáticos",
"Cerradura de puerta",
"Manija de puerta",
"Cinturón de seguridad",
"Asiento de automóvil",
"Panel de instrumentos",
"Computadora de a bordo",
"Sistema de audio para automóvil",
"Sistema de navegación GPS",
"Caja diferencial",
"Motor ensamblado",
"Catalizador",

]

# la url base para la publicacion
base_url = "https://www2.yapo.cl/ai/form/"

# obtiene la ruta del scrip
script_dir = os.path.dirname(os.path.abspath(__file__))

# inicia selenium para crome
driver = webdriver.Chrome()

try:
    # abre la pagina
    driver.get("https://www2.yapo.cl/login")

    # encuentra el campo del correo
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("desarmaduriaiparchile@gmail.com")  # aqui va el usuario

    # busca el campo de la contraseña
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("2agujas!")  # aqui las contraseñas

    # rpesionas enter
    password_input.send_keys(Keys.RETURN)

    # espera a que carge ña pagina
    driver.implicitly_wait(10)

    # Lista de regiones a recorrer
    regiones = [
        ("Biobío", 11),  # Región Biobío
        ("Araucanía", 12),  # Región Araucanía
        # se pueden agregar mas regiones
    ]

    for region_nombre, region_index in regiones:
        for i, titulo in enumerate(titulos):
            # construye la url completa 
            url = f"{base_url}{i}"

            # abre la url de anuncios
            driver.get(url)

            # espera al elemnto sea visible
            wait = WebDriverWait(driver, 10)
            categoria_selector = wait.until(EC.visibility_of_element_located((By.ID, "category_group")))

            # selecciona la seccion corecta que es accesorios de vehiculkos
            select = Select(categoria_selector)
            select.select_by_value("2100")

            # cobina los titulos
            titulo_completo = f"{titulo_personalizado} - {titulo}"

            # rellena el campo co el titulo
            titulo_input = driver.find_element(By.NAME, "subject")
            titulo_input.clear()  # Limpiar el campo de título antes de escribir
            titulo_input.send_keys(titulo_completo)

            # rellena el campo con la descripcion
            descripcion_texto = "🚗 Encuentra los mejores repuestos en Chile. CONTACTO:  WhatsApp: +569 74139654 .¡Tu destino confiable para piezas de calidad!"
            driver.execute_script(f'document.getElementsByName("body")[0].value = "{descripcion_texto}"')

           

            # pequeña pausa
            time.sleep(2)

            # agrega la imagen con js
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//p[contains(text(), 'Agregar imagen')]"))

            # espera al cuadro de dfialogo
            time.sleep(5)  # Espera adicional antes de buscar el cuadro de diálogo
            imagen_dialog = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

            # pequeña pausa
            time.sleep(2)

            # construye la ruta completa de la imagen relativa segun el script
            imagen_path = os.path.join(script_dir, "imagen.jpg")

            # envia la imagen de ruta
            imagen_dialog.send_keys(imagen_path)

            # elije la siguiente region
            region_selector = Select(driver.find_element(By.NAME, "region"))
            region_selector.select_by_index(region_index)

            time.sleep(2)  # pequeña pausa 
            comuna_selector = Select(driver.find_element(By.NAME, "communes"))
            comuna_selector.select_by_index(5)  # Seleccionar la opción en el puesto 5 (Cañete)

            # da click en los checkbox
            terms_checkbox = driver.find_element(By.ID, "accept_conditions")
            action = ActionChains(driver)
            action.move_to_element(terms_checkbox).click().perform()

            # da el click en publicar ahora
            publicar_button = driver.find_element(By.ID, "submit_create_now")
            publicar_button.click()

            # espera un tiempo
            time.sleep(5)

            # mensjae de finalizaciond e region
            print(f"Publicación completada para la región: {region_nombre}")

    # mantiene el programa funcionando
    input("Presiona Enter para finalizar el programa...")

finally:
    # Cerrar el navegador
    driver.quit()
