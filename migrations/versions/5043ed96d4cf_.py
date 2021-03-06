"""empty message

Revision ID: 5043ed96d4cf
Revises: 
Create Date: 2018-11-18 08:27:42.256118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5043ed96d4cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Foods',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('calories', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Intakes',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('image_name', sa.String(length=100), nullable=False),
    sa.Column('calories', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('age', sa.String(length=100), nullable=False),
    sa.Column('weight', sa.String(), nullable=True),
    sa.Column('height', sa.String(), nullable=True),
    sa.Column('gendar', sa.String(), nullable=True),
    sa.Column('activity', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=100), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('foodnutrient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('foodnutrient',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('calories', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('fat', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('carbs', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('protein', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.drop_table('user_tokens')
    op.drop_table('Users')
    op.drop_table('Intakes')
    op.drop_table('Foods')
    # ### end Alembic commands ###
