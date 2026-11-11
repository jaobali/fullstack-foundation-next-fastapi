from fastapi import APIRouter

from datetime import datetime, timezone
from database.core.connection import execute_query

router = APIRouter()

@router.get("/database_status")
def status():
    version, max_connections, used_connections = execute_query(
        """
        SELECT
            current_setting('server_version') AS version,
            current_setting('max_connections')::int AS max_connections,
            (SELECT count(*) FROM pg_stat_activity WHERE datname = current_database()) AS used_connections
        """
    )[0]

    return {
        "updated_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "database": {
            "server_version": version,
            "max_connections": max_connections,
            "used_connections": used_connections,
        },
    }
