"""empty message

Revision ID: 28e3b025335d
Revises: b90beda2d748
Create Date: 2018-07-05 01:25:03.177308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '28e3b025335d'
down_revision = 'b90beda2d748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', sa.String(length=50), nullable=False))
    op.drop_column('cms_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('password', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###