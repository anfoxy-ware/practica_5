import redis
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de Redis
redis_host = os.getenv('REDIS_HOST')
redis_port = int(os.getenv('REDIS_PORT'))
redis_password = os.getenv('REDIS_PASSWORD')

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
