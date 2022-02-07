"""add user table

Revision ID: 45b5d576aa75
Revises: f93240509e48
Create Date: 2022-02-07 22:37:31.376812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "45b5d576aa75"
down_revision = "f93240509e48"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
