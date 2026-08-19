from sqlalchemy.orm import Session

from app.models.pg import PG
from app.schemas.pg import PGCreate, PGUpdate


def create_pg(
    db: Session,
    pg: PGCreate,
    owner_id: int
):
    db_pg = PG(
        name=pg.name,
        address=pg.address,
        owner_id=owner_id
    )

    db.add(db_pg)
    db.commit()
    db.refresh(db_pg)

    return db_pg


def get_pg_by_id(db: Session, pg_id: int):
    return db.query(PG).filter(PG.id == pg_id).first()


def get_pgs_by_owner(db: Session, owner_id: int):
    return (
        db.query(PG)
        .filter(PG.owner_id == owner_id)
        .all()
    )

def update_pg(
    db: Session,
    pg: PG,
    pg_data: PGUpdate
):
    pg.name = pg_data.name
    pg.address = pg_data.address

    db.commit()
    db.refresh(pg)

    return pg