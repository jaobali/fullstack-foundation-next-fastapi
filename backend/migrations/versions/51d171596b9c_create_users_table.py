"""create users table

Revision ID: 51d171596b9c
Revises: b7dbd8f46107
Create Date: 2026-07-31 13:00:10.217903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51d171596b9c'
down_revision: Union[str, Sequence[str], None] = 'b7dbd8f46107'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
