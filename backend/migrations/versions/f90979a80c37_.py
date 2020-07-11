"""empty message

Revision ID: f90979a80c37
Revises: 9ad926a099f2
Create Date: 2020-05-25 14:55:55.356850

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f90979a80c37'
down_revision = '9ad926a099f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('applicant_id', sa.Integer(), nullable=True))
    op.drop_column('applications', 'applicatant_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('applicatant_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('applications', 'applicant_id')
    # ### end Alembic commands ###
