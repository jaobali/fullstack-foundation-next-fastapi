import psycopg
from database.core.settings import settings

def get_connection():
    return psycopg.connect(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        dbname=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        sslmode=settings.PGSSLMODE,
        channel_binding=settings.PGCHANNELBINDING
    )


def execute_query(query: str, params: tuple | None = None) -> list[tuple]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall() if cur.description is not None else []


