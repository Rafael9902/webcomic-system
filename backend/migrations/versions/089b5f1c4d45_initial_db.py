"""Initial_db

Revision ID: 089b5f1c4d45
Revises: 
Create Date: 2021-11-12 11:32:21.441695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '089b5f1c4d45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comic',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('month', sa.String(length=2), nullable=False),
    sa.Column('num', sa.String(length=50), nullable=False),
    sa.Column('link', sa.String(length=50), nullable=False),
    sa.Column('year', sa.String(length=50), nullable=False),
    sa.Column('news', sa.String(length=50), nullable=True),
    sa.Column('safe_title', sa.String(length=50), nullable=False),
    sa.Column('transcript', sa.String(length=100), nullable=False),
    sa.Column('alt', sa.String(length=50), nullable=False),
    sa.Column('img', sa.String(length=50), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('day', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('num'),
    sa.UniqueConstraint('num')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('comic')
    # ### end Alembic commands ###
