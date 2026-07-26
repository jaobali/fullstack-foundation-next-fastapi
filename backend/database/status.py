from datetime import datetime, timezone

from fastapi import APIRouter
from database.core.connection import get_connection

router = APIRouter()

@router.get("/database_status")
def status():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    current_setting('server_version') AS version,
                    current_setting('max_connections')::int AS max_connections,
                    (SELECT count(*) FROM pg_stat_activity WHERE datname = %s) AS used_connections
                """,
                (conn.info.dbname,)
            )
            version, max_connections, used_connections = cur.fetchone()

    return {
        "updated_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "database": {
            "server_version": version,
            "max_connections": max_connections,
            "used_connections": used_connections,
        },
    }
