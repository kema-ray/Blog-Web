"""Third Migration

Revision ID: 648966f487e8
Revises: 6e6b334067ab
Create Date: 2022-05-15 16:30:31.121617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '648966f487e8'
down_revision = '6e6b334067ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('secure_password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'secure_password')
    # ### end Alembic commands ###