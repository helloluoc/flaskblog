"""empty message

Revision ID: d86207362afd
Revises: f7ce02676c18
Create Date: 2018-05-03 18:51:09.312688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd86207362afd'
down_revision = 'f7ce02676c18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###