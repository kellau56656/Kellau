router = APIRouter(
    prefix="/links",
    tags=["Links"]
)
@router.post("/")
def create_link():
    pass
@router.get("/")
def get_links():
    pass