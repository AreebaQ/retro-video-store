"""empty message

Revision ID: 79c2865e5b6f
Revises: 4408873d4fe9
Create Date: 2021-11-05 18:06:16.147672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79c2865e5b6f'
down_revision = '4408873d4fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('register_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'register_at')
    # ### end Alembic commands ###
