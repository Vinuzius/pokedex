# Statistics DTOs

from sqlmodel import SQLModel


class StatusCount(SQLModel):
    status: str
    count: int


class CompletionStats(SQLModel):
    total: int
    collected: int
    completion_percentage: float
    by_status: list[StatusCount]
