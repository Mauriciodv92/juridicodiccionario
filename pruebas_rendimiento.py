
import time
import requests
import concurrent.futures

def prueba_1_home():
    inicio = time.time()
    response = requests.get("http://localhost:5000/")
    fin = time.time()
    print("🔹 Prueba 1 - Tiempo de respuesta del home (/):", fin - inicio, "segundos")

def prueba_2_carga_simultanea():
    def probar_home(_):
        try:
            response = requests.get("http://localhost:5000/")
            return response.status_code
        except Exception as e:
            return f"Error: {e}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        resultados = list(executor.map(probar_home, range(50)))

    exitosas = sum(1 for r in resultados if r == 200)
    print(f"🔹 Prueba 2 - Respuestas correctas (200): {exitosas}/50")

def prueba_3_busqueda():
    inicio = time.time()
    response = requests.get("http://localhost:5000/?q=acción")
    fin = time.time()
    print("🔹 Prueba 3 - Tiempo de búsqueda 'acción':", fin - inicio, "segundos")

def prueba_4_admin():
    try:
        inicio = time.time()
        response = requests.get("http://localhost:5000/admin")
        fin = time.time()
        print("🔹 Prueba 4 - Tiempo carga panel de administración:", fin - inicio, "segundos")
    except Exception as e:
        print("🔴 Prueba 4 - Error al acceder al panel:", e)

if __name__ == "__main__":
    prueba_1_home()
    prueba_2_carga_simultanea()
    prueba_3_busqueda()
    prueba_4_admin()
