import asyncpg
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

class PostgresDB:
    """Clase para manejar la conexión a PostgreSQL con reintentos."""

    def __init__(self):
        self.DB_USER = os.getenv("POSTGRES_USER")
        self.DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        self.DB_NAME = os.getenv("POSTGRES_DB")
        self.DB_HOST = os.getenv("POSTGRES_HOST")
        self.DB_PORT = os.getenv("POSTGRES_PORT")
        self.pool = None

    async def connect(self, max_retries=5, retry_delay=3):
        """Intenta conectar con PostgreSQL con reintentos."""
        for attempt in range(max_retries):
            try:
                print(f"Intentando conectar a PostgreSQL (Intento {attempt + 1}/{max_retries})...")
                self.pool = await asyncpg.create_pool(
                    user=self.DB_USER,
                    password=self.DB_PASSWORD,
                    database=self.DB_NAME,
                    host=self.DB_HOST,
                    port=self.DB_PORT
                )
                print("Conexión a PostgreSQL establecida.")
                return
            except Exception as e:
                print(f"Error al conectar con PostgreSQL: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                else:
                    print("No se pudo conectar a PostgreSQL después de varios intentos.")
                    self.pool = None

    async def disconnect(self):
        """Cierra la conexión con PostgreSQL."""
        if self.pool:
            await self.pool.close()
            print("🔌 Conexión a PostgreSQL cerrada.")


# Crear una instancia global de la conexión
postgres_db = PostgresDB()

# Iniciar la conexión en el arranque de la aplicación
asyncio.run(postgres_db.connect())
