"""add descuento and total to ordenes

Revision ID: c0a7737f0f41
Revises: 196ce72ddcdb
Create Date: 2026-01-09 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0a7737f0f41'
down_revision = '196ce72ddcdb'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('ordenes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descuento', sa.Numeric(precision=10, scale=2), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('total', sa.Numeric(precision=10, scale=2), nullable=False, server_default='0'))


def downgrade():
    with op.batch_alter_table('ordenes', schema=None) as batch_op:
        batch_op.drop_column('total')
        batch_op.drop_column('descuento')
