"""Change dimension of Vector from 1024 to 384 (for sentence-transformers/all-MiniLM-L6-v2)

Revision ID: 21961f36016e
Revises: 7b9fb2423c81
Create Date: 2024-06-10 01:49:09.898062

"""

from collections.abc import Sequence

import pgvector
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "21961f36016e"
down_revision: str | None = "7b9fb2423c81"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "embeddings",
        "embedding",
        existing_type=pgvector.sqlalchemy.Vector(dim=1024),
        type_=pgvector.sqlalchemy.Vector(dim=384),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "embeddings",
        "embedding",
        existing_type=pgvector.sqlalchemy.Vector(dim=384),
        type_=pgvector.sqlalchemy.Vector(dim=1024),
        existing_nullable=False,
    )
    # ### end Alembic commands ###