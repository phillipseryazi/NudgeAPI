"""create businesses table

Revision ID: 16307c5cf253
Revises: 097dc0840a73
Create Date: 2021-12-17 12:47:11.738198

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import PrimaryKeyConstraint, UniqueConstraint


# revision identifiers, used by Alembic.
revision = '16307c5cf253'
down_revision = '097dc0840a73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("businesses",
                    sa.Column("id", sa.Integer, nullable=False),
                    sa.Column("name", sa.String, nullable=False),
                    sa.Column("description", sa.Text, nullable=False),
                    sa.Column("domain", sa.ARRAY(sa.String), nullable=False),
                    sa.Column("contacts", sa.ARRAY(sa.String), nullable=False),
                    sa.Column("email", sa.String, nullable=False),
                    sa.Column("created_at",
                              sa.TIMESTAMP(timezone=True),
                              nullable=False,
                              server_default=sa.text("now()")
                              ),
                    sa.Column("updated_at",
                              sa.TIMESTAMP(timezone=True),
                              nullable=False,
                              server_default=sa.text("now()")
                              ),
                    sa.Column("user_id", sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(
                        ["user_id"],
                        ["users.id"],
                        ondelete="CASCADE",
                        name="business_user_fk"),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )


def downgrade():
    op.drop_constraint("business_user_fk", table_name="businesses")
    op.drop_table("businesses")
