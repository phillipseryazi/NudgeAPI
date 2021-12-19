"""alter business table

Revision ID: 0213ab07dbce
Revises: 16307c5cf253
Create Date: 2021-12-19 13:14:49.411952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0213ab07dbce'
down_revision = '16307c5cf253'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name="businesses",
        column_name="domain",
        type_=sa.JSON,
        postgresql_using="domain::json")


def downgrade():
    op.alter_column(table_name="businesses",
                    column_name="domain",
                    type_=sa.String)
