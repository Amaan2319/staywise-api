from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.crud.pg import create_pg, get_pg_by_id, get_pgs_by_owner
from app.dependencies.permissions import (
    get_current_user,
    get_current_owner
)
from app.models.user import User
from app.schemas.pg import PGCreate, PGResponse


router = APIRouter(
    prefix="/pgs",
    tags=["PG Management"]
)


@router.post(
    "",
    response_model=PGResponse,
    status_code=status.HTTP_201_CREATED
)
def create_pg_route(
    pg: PGCreate,
    db: Session = Depends(get_db),
    current_owner: User = Depends(get_current_owner)
):
    return create_pg(
        db,
        pg,
        current_owner.id
    )


@router.get(
    "/my",
    response_model=list[PGResponse]
)
def get_my_pgs(
    db: Session = Depends(get_db),
    current_owner: User = Depends(get_current_owner)
):
    return get_pgs_by_owner(
        db,
        current_owner.id
    )


@router.get(
    "/{pg_id}",
    response_model=PGResponse
)
def get_pg(
    pg_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    pg = get_pg_by_id(db, pg_id)

    if not pg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PG not found"
        )

    return pg