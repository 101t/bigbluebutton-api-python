from .base import BaseResponse

class UpdateRecordingsResponse(BaseResponse):
    def is_updated(self):
        return self.get_text("updated") == "true" or self.get_text("updated")