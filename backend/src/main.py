import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.core.exceptions import UserFacingException, SystemException, ApiErrorResponse, ErrorDevDetails

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(UserFacingException)
async def user_facing_exception_handler(request: Request, exc: UserFacingException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiErrorResponse(
            error_code=exc.error_code,
            user_message=exc.user_message,
            requires_user_action=exc.requires_user_action,
            dev_details=exc.dev_details
        ).model_dump()
    )

@app.exception_handler(SystemException)
async def system_exception_handler(request: Request, exc: SystemException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiErrorResponse(
            error_code=exc.error_code,
            user_message=exc.user_message,
            requires_user_action=exc.requires_user_action,
            dev_details=exc.dev_details
        ).model_dump()
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    tb = traceback.format_exc()
    return JSONResponse(
        status_code=500,
        content=ApiErrorResponse(
            error_code="UNEXPECTED_SYSTEM_ERROR",
            user_message="An unexpected error occurred. Please try again later.",
            requires_user_action=False,
            dev_details=ErrorDevDetails(traceback=tb, context={"path": request.url.path})
        ).model_dump()
    )

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "version": settings.VERSION}

from src.api.v1 import api_router
app.include_router(api_router, prefix="/api/v1")
