"""add content column to posts table

Revision ID: f93240509e48
Revises: 8f220c824c70
Create Date: 2022-02-07 22:33:01.272437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f93240509e48"
down_revision = "8f220c824c70"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade():
    op.drop_column("posts", "content")
