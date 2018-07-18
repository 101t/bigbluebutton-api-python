from .base import BaseResponse

class SetConfigXMLResponse(BaseResponse):
    def get_token(self):
        return self.get_field("token")