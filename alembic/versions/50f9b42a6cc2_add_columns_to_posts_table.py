"""add columns to posts table

Revision ID: 50f9b42a6cc2
Revises: f6e52cc52917
Create Date: 2023-07-31 15:35:18.701034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f9b42a6cc2'
down_revision = 'f6e52cc52917'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="True"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
