from .base import BaseResponse

class DeleteRecordingsResponse(BaseResponse):
    def is_deleted(self):
        return self.get_text("deleted") == "true" or self.get_text("deleted")