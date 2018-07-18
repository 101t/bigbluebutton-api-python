from .base import BaseResponse

class PublishRecordingsResponse(BaseResponse):
    def is_published(self):
        field = self.get_field("published")
        return field == "true" or (isinstance(field, bool) and field)
