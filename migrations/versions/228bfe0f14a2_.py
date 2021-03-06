"""empty message

Revision ID: 228bfe0f14a2
Revises: d86207362afd
Create Date: 2018-05-03 19:19:48.405666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228bfe0f14a2'
down_revision = 'd86207362afd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection',
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['post.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collection')
    # ### end Alembic commands ###
