import re
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

def Chatbot():
    print("*** Chatbot v1.0.0 Iniciando***")
    print("Hola soy el Chatbot v1.0.0, Puedo ayudarte a obtener informacion sobre Acciones y el clima")
    print("Que quieres saber hoy?")

    # Ciclo infinito para mantener el chatbot corriendo
    while True:
        try:
            user_input = input("---> ").strip()
            if not user_input:
                continue
            
            # Salida del bucle
            if user_input.lower() in ["salir", "exit", "quit", "adiós", "adios"]:
                print(">>> ¡Hasta luego!")
                break
            # Reglas para detectar intencion de preguntas por acciones
            stock_match = re.search(r"(?:precio|stock|acción|accion)\s+(?:de\s+)?(?:la\s+|el\s+)?(?:acción\s+|accion\s+)?(?:de\s+)?([\w\s]+)", user_input, re.IGNORECASE)
            # Reglas para detectar intencion de preguntas por clima    
            weather_match = re.search(r"(?:temperatura|clima|tiempo)\s+(?:(?:en|de)\s+)?([\w\s?]+)", user_input, re.IGNORECASE)

            #Caso 1: El usuario pregunta por acciones
            if stock_match:
                #Debemos esperar si el usuario indica alguna accion
                precio = obtener_precio_accion(None, user_input)
                if precio:
                    print(f">>> {precio}")
                else:
                    print("Chatbot: NO pude obtener el precio, Podrias intentar con otra accion? :)")
            #Caso 2: El usuario pregunta por clima
            elif weather_match:     
                temp = obtener_clima(None, user_input)  
                if temp:
                    print(f">>> {temp}")
                else:
                    print("Chatbot: NO pude obtener la temperatura. Podrias ntentar con  otra ciudad?")
            #Caso 3: El usuario no ejecuta alguna peticion
            else:    
                print("Chatbot: NO entendi tu peticion,podrias formularla de nuevo?")
                
        except KeyboardInterrupt:
            print("\n>>> ¡Hasta luego!")
            break
        except Exception as e:
            print(f">>> Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    Chatbot()
    