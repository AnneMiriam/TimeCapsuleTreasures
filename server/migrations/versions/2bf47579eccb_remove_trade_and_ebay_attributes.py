"""remove trade and ebay attributes

Revision ID: 2bf47579eccb
Revises: 88561fcdfadf
Create Date: 2024-02-12 19:00:01.271785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bf47579eccb'
down_revision = '88561fcdfadf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('trade_status')
        batch_op.drop_column('ebay_link')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ebay_link', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('trade_status', sa.VARCHAR(), nullable=False))

    # ### end Alembic commands ###
