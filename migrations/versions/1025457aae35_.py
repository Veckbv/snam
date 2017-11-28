"""empty message

Revision ID: 1025457aae35
Revises: 
Create Date: 2017-11-28 03:35:16.047434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1025457aae35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('images', 'name')
    # ### end Alembic commands ###
