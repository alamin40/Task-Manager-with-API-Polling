from sqlalchemy import Table, Column, Integer, String, Boolean
from .database import metadata

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String(500)),
    Column("completed", Boolean, default=False)
)
