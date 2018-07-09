from .base import BaseResponse

class PublishRecordingsResponse(BaseResponse):
    def is_published(self):
        return self.get_text("published") == "true" or self.get_text("published")