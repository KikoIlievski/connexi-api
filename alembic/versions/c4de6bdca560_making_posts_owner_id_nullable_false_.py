"""making posts.owner_id nullable = False (fixing typo made)

Revision ID: c4de6bdca560
Revises: e5a0082371a8
Create Date: 2022-02-07 23:00:33.968541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c4de6bdca560"
down_revision = "e5a0082371a8"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name="posts", column_name="owner_id", nullable=False)


def downgrade():
    op.alterColumn("posts", "owner_id", nullable=True)
