"""empty message

Revision ID: f4eeafc9d231
Revises: ec492bd18db6
Create Date: 2020-04-25 11:25:23.682277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4eeafc9d231'
down_revision = 'ec492bd18db6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(length=50), nullable=False),
    sa.Column('school', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('fieldOfStudy', sa.String(length=50), nullable=False),
    sa.Column('duration', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('created', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    # ### end Alembic commands ###
