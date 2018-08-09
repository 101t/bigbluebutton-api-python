from .base import BaseResponse


class ApiVersionResponse(BaseResponse):
    def get_version(self):
        return self.get_field("version")
