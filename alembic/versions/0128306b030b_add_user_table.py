"""add user table

Revision ID: 0128306b030b
Revises: 20ed01910e0d
Create Date: 2023-07-31 15:19:00.838172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0128306b030b'
down_revision = '20ed01910e0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
