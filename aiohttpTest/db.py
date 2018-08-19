from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date, Boolean
)

meta = MetaData()

flagStatus = Table(
	'flagStatus', meta,
	Column('id', Integer),
	Column('active', Boolean),
	Column('clickTime', Date)
)