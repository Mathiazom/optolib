"""empty message

Revision ID: 4e0962d591ac
Revises: 146ccc7f5e51
Create Date: 2020-12-09 21:26:56.817233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e0962d591ac'
down_revision = '146ccc7f5e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cardinal', sa.Integer(), nullable=True),
    sa.Column('fulfilled', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('img_url', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('cardinal', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fulfilled', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('author', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('img_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='book_pkey')
    )
    op.drop_table('books')
    # ### end Alembic commands ###
