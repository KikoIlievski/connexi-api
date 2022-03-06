"""adding username column

Revision ID: c4de82978c82
Revises: fd4ca7195e91
Create Date: 2022-03-06 17:44:13.937690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c4de82978c82"
down_revision = "fd4ca7195e91"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users", sa.Column("username", sa.String, nullable=False, unique=True)
    )


def downgrade():
    op.drop_column("posts", "username")
