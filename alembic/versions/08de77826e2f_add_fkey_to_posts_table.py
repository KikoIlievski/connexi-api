"""add fkey to posts table

Revision ID: 08de77826e2f
Revises: 45b5d576aa75
Create Date: 2022-02-07 22:45:15.397029

"""
from decimal import localcontext
from threading import local
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "08de77826e2f"
down_revision = "45b5d576aa75"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("posts_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
