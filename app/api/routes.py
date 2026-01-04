# from fastapi import APIRouter, HTTPException
# from app.models.user_model import User
# from app.service.user_service import UserService
#
# router = APIRouter()
# service = UserService()
#
# @router.get("/health")
# def health():
#     return {"status": "UP"}
#
# @router.post("/users")
# def create_user(user: User):
#     user_id = service.create_user(user.dict(exclude={"id"}))
#     return {"id": user_id}
#
# @router.get("/users")
# def list_users():
#     return service.list_users()
#
# @router.get("/users/{user_id}")
# def get_user(user_id: str):
#     user = service.get_user(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
# @router.put("/users/{user_id}")
# def update_user(user_id: str, user: User):
#     service.update_user(user_id, user.dict(exclude={"id"}))
#     return {"status": "updated"}
#
# @router.delete("/users/{user_id}")
# def delete_user(user_id: str):
#     service.delete_user(user_id)
#     return {"status": "deleted"}
