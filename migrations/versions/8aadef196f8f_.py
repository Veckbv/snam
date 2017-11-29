"""empty message

Revision ID: 8aadef196f8f
Revises: 
Create Date: 2017-11-29 07:54:53.825532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aadef196f8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('chapter_name', sa.String(length=64), nullable=True))
    op.add_column('images', sa.Column('chapter_num', sa.Integer(), nullable=True))
    op.add_column('images', sa.Column('comics', sa.String(length=64), nullable=True))
    op.add_column('images', sa.Column('volume', sa.String(length=64), nullable=True))
    op.drop_column('images', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.drop_column('images', 'volume')
    op.drop_column('images', 'comics')
    op.drop_column('images', 'chapter_num')
    op.drop_column('images', 'chapter_name')
    # ### end Alembic commands ###
