"""DB Init

Revision ID: cd701efe364f
Revises:
Create Date: 2023-10-18 18:47:52.874198

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cd701efe364f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "alerts",
        "azimuth",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=4, asdecimal=True),
        existing_nullable=True,
    )
    op.alter_column(
        "alerts", "lat", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "alerts", "lon", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "devices",
        "angle_of_view",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=2, asdecimal=True),
        existing_nullable=True,
    )
    op.alter_column(
        "devices",
        "elevation",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=1, asdecimal=True),
        existing_nullable=True,
    )
    op.alter_column(
        "devices", "lat", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "devices", "lon", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "devices",
        "azimuth",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=1, asdecimal=True),
        existing_nullable=True,
    )
    op.alter_column(
        "devices", "pitch", existing_type=sa.REAL(), type_=sa.Float(precision=1, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "events", "lat", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "events", "lon", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "sites", "lat", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    op.alter_column(
        "sites", "lon", existing_type=sa.REAL(), type_=sa.Float(precision=4, asdecimal=True), existing_nullable=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "sites", "lon", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "sites", "lat", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "events", "lon", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "events", "lat", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "devices", "pitch", existing_type=sa.Float(precision=1, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "devices",
        "azimuth",
        existing_type=sa.Float(precision=1, asdecimal=True),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    op.alter_column(
        "devices", "lon", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "devices", "lat", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "devices",
        "elevation",
        existing_type=sa.Float(precision=1, asdecimal=True),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    op.alter_column(
        "devices",
        "angle_of_view",
        existing_type=sa.Float(precision=2, asdecimal=True),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    op.alter_column(
        "alerts", "lon", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "alerts", "lat", existing_type=sa.Float(precision=4, asdecimal=True), type_=sa.REAL(), existing_nullable=True
    )
    op.alter_column(
        "alerts",
        "azimuth",
        existing_type=sa.Float(precision=4, asdecimal=True),
        type_=sa.REAL(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
