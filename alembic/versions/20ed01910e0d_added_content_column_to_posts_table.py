"""added content column to posts table

Revision ID: 20ed01910e0d
Revises: 97defc581940
Create Date: 2023-07-31 15:11:24.572117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ed01910e0d'
down_revision = '97defc581940'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
