"""add_flibusta_models

Revision ID: 2a14f3e60060
Revises: 6a4e5ccb2054
Create Date: 2023-03-26 17:22:44.004089

"""
from alembic import op
import sqlalchemy as sa

from models.base_model import Id

# revision identifiers, used by Alembic.
revision = '2a14f3e60060'
down_revision = '6a4e5ccb2054'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libavtor',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('AvtorId', sa.Integer(), nullable=False),
    sa.Column('Pos', sa.Integer(), nullable=True),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('BookId', 'AvtorId', 'id')
    )
    op.create_table('libavtorname',
    sa.Column('AvtorId', sa.Integer(), nullable=False),
    sa.Column('FirstName', sa.String(length=99), nullable=False),
    sa.Column('MiddleName', sa.String(length=99), nullable=False),
    sa.Column('LastName', sa.String(length=99), nullable=False),
    sa.Column('NickName', sa.String(length=33), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('Email', sa.String(length=255), nullable=False),
    sa.Column('Homepage', sa.String(length=255), nullable=False),
    sa.Column('Gender', sa.String(length=1), nullable=False),
    sa.Column('MasterId', sa.Integer(), nullable=True),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('AvtorId', 'id')
    )
    op.create_table('libbook',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('FileSize', sa.Integer(), nullable=False),
    sa.Column('Time', sa.DateTime(), nullable=False),
    sa.Column('Title', sa.String(length=254), nullable=False),
    sa.Column('Title1', sa.String(length=254), nullable=False),
    sa.Column('Lang', sa.String(length=3), nullable=False),
    sa.Column('LangEx', sa.Integer(), nullable=False),
    sa.Column('SrcLang', sa.String(length=3), nullable=False),
    sa.Column('FileType', sa.String(length=4), nullable=False),
    sa.Column('Encoding', sa.String(length=32), nullable=False),
    sa.Column('Year', sa.Integer(), nullable=False),
    sa.Column('Deleted', sa.String(length=1), nullable=False),
    sa.Column('Ver', sa.String(length=8), nullable=False),
    sa.Column('FileAuthor', sa.String(length=64), nullable=False),
    sa.Column('N', sa.Integer(), nullable=False),
    sa.Column('keywords', sa.String(length=255), nullable=False),
    sa.Column('md5', sa.String(length=32), nullable=False),
    sa.Column('Modified', sa.DateTime(), nullable=False),
    sa.Column('pmd5', sa.String(length=32), nullable=False),
    sa.Column('InfoCode', sa.Integer(), nullable=False),
    sa.Column('Pages', sa.Integer(), nullable=False),
    sa.Column('Chars', sa.Integer(), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('BookId', 'id'),
    sa.UniqueConstraint('md5')
    )
    op.create_table('libfilename',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('FileName', sa.String(length=255), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('BookId', 'id'),
    sa.UniqueConstraint('FileName')
    )
    op.create_table('libgenre',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('GenreId', sa.Integer(), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libgenrelist',
    sa.Column('GenreId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('GenreCode', sa.String(length=45), nullable=False),
    sa.Column('GenreDesc', sa.String(length=99), nullable=False),
    sa.Column('GenreMeta', sa.String(length=45), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('GenreId', 'id')
    )
    op.create_table('librate',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('UserId', sa.Integer(), nullable=False),
    sa.Column('Rate', sa.String(length=1), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('BookId'),
    sa.UniqueConstraint('UserId')
    )
    op.create_table('libseq',
    sa.Column('BookId', sa.Integer(), nullable=False),
    sa.Column('SeqId', sa.Integer(), nullable=False),
    sa.Column('SeqNumb', sa.Integer(), nullable=False),
    sa.Column('Level', sa.SmallInteger(), nullable=False),
    sa.Column('Type', sa.Boolean(), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('BookId', 'SeqId', 'id')
    )
    op.create_table('libseqname',
    sa.Column('SeqId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('SeqName', sa.String(length=254), nullable=False),
    sa.Column('id', Id(), nullable=False),
    sa.PrimaryKeyConstraint('SeqId', 'id'),
    sa.UniqueConstraint('SeqName')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('libseqname')
    op.drop_table('libseq')
    op.drop_table('librate')
    op.drop_table('libgenrelist')
    op.drop_table('libgenre')
    op.drop_table('libfilename')
    op.drop_table('libbook')
    op.drop_table('libavtorname')
    op.drop_table('libavtor')
    # ### end Alembic commands ###
