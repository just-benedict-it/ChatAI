"""[user activity table] activity_action added

Revision ID: dc98a121c824
Revises: e94dbea657fe
Create Date: 2024-02-29 11:03:23.401758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc98a121c824'
down_revision: Union[str, None] = 'e94dbea657fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_activity', sa.Column('activity_action', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_activity_activity_action'), 'user_activity', ['activity_action'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_activity_activity_action'), table_name='user_activity')
    op.drop_column('user_activity', 'activity_action')
    # ### end Alembic commands ###