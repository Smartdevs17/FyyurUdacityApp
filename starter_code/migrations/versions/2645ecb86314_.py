"""empty message

Revision ID: 2645ecb86314
Revises: 368de07258c1
Create Date: 2022-08-18 19:30:07.998067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2645ecb86314'
down_revision = '368de07258c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'website')
    # ### end Alembic commands ###
