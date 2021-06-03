"""tabla usuarios

Revision ID: da68b8967bc9
Revises: 
Create Date: 2021-06-02 21:21:47.987315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da68b8967bc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=120), nullable=True),
    sa.Column('apellido_materno', sa.String(length=120), nullable=True),
    sa.Column('matricula', sa.String(length=10), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_apellido_paterno'), 'user', ['apellido_paterno'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_matricula'), 'user', ['matricula'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_matricula'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_apellido_paterno'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###