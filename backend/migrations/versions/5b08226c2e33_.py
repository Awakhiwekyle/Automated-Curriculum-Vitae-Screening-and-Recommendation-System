"""empty message

Revision ID: 5b08226c2e33
Revises: f6ee062b5935
Create Date: 2020-03-14 17:59:20.262527

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b08226c2e33'
down_revision = 'f6ee062b5935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fuel')
    op.drop_table('responses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('responses',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('requestId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('respondentId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('action', mysql.VARCHAR(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('fuel',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('fueltype', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('priority', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('origin', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('destination', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('volume', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('assessor', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('approver', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('plusvehicle', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('reason', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('requestedBy', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('daterequired', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###