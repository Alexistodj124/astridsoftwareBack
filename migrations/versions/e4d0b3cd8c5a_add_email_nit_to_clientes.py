"""add email and nit to clientes

Revision ID: e4d0b3cd8c5a
Revises: c0a7737f0f41
Create Date: 2026-02-20 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4d0b3cd8c5a'
down_revision = 'c0a7737f0f41'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('nit', sa.String(length=50), nullable=True))


def downgrade():
    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.drop_column('nit')
        batch_op.drop_column('email')

