"""empty message

Revision ID: 4009fd5c8cd0
Revises: d2a335e592fa
Create Date: 2017-12-10 13:37:54.641327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4009fd5c8cd0'
down_revision = 'd2a335e592fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=140), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###
