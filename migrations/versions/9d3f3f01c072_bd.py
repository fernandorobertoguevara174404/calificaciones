"""bd

Revision ID: 9d3f3f01c072
Revises: 
Create Date: 2021-06-14 21:35:03.810472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d3f3f01c072'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=120), nullable=True),
    sa.Column('apellido_materno', sa.String(length=120), nullable=True),
    sa.Column('profesor', sa.Boolean(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('matricula', sa.String(length=10), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_apellido_paterno'), 'users', ['apellido_paterno'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_matricula'), 'users', ['matricula'], unique=True)
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('id_profesor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_profesor'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tareas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_curso', sa.Integer(), nullable=True),
    sa.Column('titulo', sa.String(length=150), nullable=True),
    sa.Column('fecha_de_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_de_entrega', sa.DateTime(), nullable=True),
    sa.Column('descripcion', sa.String(length=1500), nullable=True),
    sa.Column('puntaje', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_curso'], ['cursos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario_curso',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_curso', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_curso'], ['cursos.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id_user', 'id_curso')
    )
    op.create_table('calificaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_tarea', sa.Integer(), nullable=True),
    sa.Column('id_alumno', sa.Integer(), nullable=True),
    sa.Column('calificacion', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_alumno'], ['users.id'], ),
    sa.ForeignKeyConstraint(['id_tarea'], ['tareas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calificaciones')
    op.drop_table('usuario_curso')
    op.drop_table('tareas')
    op.drop_table('cursos')
    op.drop_index(op.f('ix_users_matricula'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_apellido_paterno'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
