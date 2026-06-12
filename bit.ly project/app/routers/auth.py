from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)
@router.post("/register")
def register():
    pass
@router.post("/login")
def login():
    pass