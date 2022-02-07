"""add last few columns to posts table

Revision ID: e5a0082371a8
Revises: 08de77826e2f
Create Date: 2022-02-07 22:54:27.026751

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e5a0082371a8"
down_revision = "08de77826e2f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", column_name="published")
    op.drop_column("posts", column_name="created_at")
