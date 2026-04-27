from ninja import NinjaAPI
from .auth import router as auth_router
from .courses import router as courses_router
from .enrollments import router as enrollments_router
from .auth_bearer import AuthBearer

api = NinjaAPI(auth=AuthBearer())  # 🔥 INI KUNCI

api.add_router("/auth", auth_router)
api.add_router("/courses", courses_router)
api.add_router("/enrollments", enrollments_router)