"""empty message

Revision ID: f6ee062b5935
Revises: 19c280503028
Create Date: 2019-08-12 16:29:46.681840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6ee062b5935'
down_revision = '19c280503028'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('responses', sa.Column('action', sa.String(length=15), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('responses', 'action')
    # ### end Alembic commands ###