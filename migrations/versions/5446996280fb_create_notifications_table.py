"""Create notifications table

Revision ID: 5446996280fb
Revises: 69af956f9fdb
Create Date: 2024-11-17 01:16:35.938562

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5446996280fb'
down_revision = '69af956f9fdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_read', sa.Boolean(), nullable=True))
        batch_op.alter_column('content',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.drop_constraint('notifications_ibfk_1', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notifications', schema=None) as batch_op:
        batch_op.create_foreign_key('notifications_ibfk_1', 'users', ['user_id'], ['user_id'])
        batch_op.alter_column('content',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=False)
        batch_op.drop_column('is_read')

    # ### end Alembic commands ###
