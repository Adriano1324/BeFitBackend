"""Create user model

Revision ID: 3eb1607d948a
Revises:
Create Date: 2023-06-15 20:49:40.575298

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3eb1607d948a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("password_hash", sa.String(length=512), nullable=False),
        sa.Column("description", sa.String(length=512), nullable=True),
        sa.Column("avatar_img", sa.String(length=128), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_public", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(
        op.f("ix_user_password_hash"), "user", ["password_hash"], unique=False
    )
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_index(op.f("ix_user_password_hash"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
