"""empty message

Revision ID: 9ad926a099f2
Revises: 546b87b24ed1
Create Date: 2020-05-25 11:34:42.198329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad926a099f2'
down_revision = '546b87b24ed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('company', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'company')
    # ### end Alembic commands ###