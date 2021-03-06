"""first commit

Revision ID: 01d6e48a580e
Revises: 
Create Date: 2020-12-19 17:41:18.306202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d6e48a580e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('title', sa.String(length=60), nullable=True, comment='标题'),
    sa.Column('year', sa.String(length=4), nullable=True, comment='电影年份'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('name', sa.String(length=20), nullable=True, comment='名字'),
    sa.Column('passwd', sa.String(length=50), nullable=True, comment='密码'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###
