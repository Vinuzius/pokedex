# Statistics routes

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlmodel import Session, select

from models import Pokemon
from dtos.statisticsDTO import CompletionStats, StatusCount
from dependencies import get_session

router = APIRouter(prefix="/statistics", tags=["statistics"])


@router.get("/completion", response_model=CompletionStats)
def get_completion_stats(session: Session = Depends(get_session)):
    """Get completion statistics"""
    # Single query to get counts by status
    by_status = session.exec(
        select(Pokemon.status, func.count(Pokemon.id).label("count"))
        .group_by(Pokemon.status)
    ).all()
    
    # Convert to list of StatusCount objects
    status_list = [StatusCount(status=str(status), count=count) 
                   for status, count in by_status]
    
    # Calculate total from status counts
    total = sum(count for _, count in by_status)
    collected = next((count for status, count in by_status if str(status) == "coletado"), 0)
    percentage = round((collected / total * 100), 2) if total > 0 else 0.0

    return CompletionStats(
        total=total,
        collected=collected,
        completion_percentage=percentage,
        by_status=status_list
    )
