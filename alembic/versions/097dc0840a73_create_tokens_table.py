"""create tokens table

Revision ID: 097dc0840a73
Revises: e6c18ec0be85
Create Date: 2021-12-04 16:37:02.774051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097dc0840a73'
down_revision = 'e6c18ec0be85'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("tokens",
                    sa.Column("id", sa.Integer, nullable=False),
                    sa.Column("token", sa.String, nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("token"))


def downgrade():
    op.drop_table("tokens")
