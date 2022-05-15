"""Second Migration

Revision ID: 6e6b334067ab
Revises: 54af21e924cc
Create Date: 2022-05-15 16:27:18.973839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e6b334067ab'
down_revision = '54af21e924cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###
