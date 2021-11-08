"""empty message

Revision ID: 0f3b8fbbb125
Revises: 79c2865e5b6f
Create Date: 2021-11-08 14:36:34.322493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f3b8fbbb125'
down_revision = '79c2865e5b6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('inventory_checked_out', sa.Integer(), nullable=True))
    op.add_column('videos_customers', sa.Column('due_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('videos_customers', 'due_date')
    op.drop_column('video', 'inventory_checked_out')
    # ### end Alembic commands ###
