from typing import Optional
from pydantic import BaseModel

class ErrorDevDetails(BaseModel):
    traceback: Optional[str] = None
    context: Optional[dict] = None

class ApiErrorResponse(BaseModel):
    error_code: str
    user_message: str
    requires_user_action: bool
    dev_details: ErrorDevDetails

class BaseAPIException(Exception):
    def __init__(
        self,
        status_code: int,
        error_code: str,
        user_message: str,
        requires_user_action: bool,
        dev_details: Optional[ErrorDevDetails] = None
    ):
        self.status_code = status_code
        self.error_code = error_code
        self.user_message = user_message
        self.requires_user_action = requires_user_action
        self.dev_details = dev_details or ErrorDevDetails()
        super().__init__(self.user_message)

class UserFacingException(BaseAPIException):
    def __init__(self, error_code: str, user_message: str, dev_details: Optional[ErrorDevDetails] = None):
        super().__init__(
            status_code=400,
            error_code=error_code,
            user_message=user_message,
            requires_user_action=True,
            dev_details=dev_details
        )

class SystemException(BaseAPIException):
    def __init__(self, error_code: str, user_message: str, dev_details: Optional[ErrorDevDetails] = None):
        super().__init__(
            status_code=500,
            error_code=error_code,
            user_message=user_message,
            requires_user_action=False,
            dev_details=dev_details
        )
