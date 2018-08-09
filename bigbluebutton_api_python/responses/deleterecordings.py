from .base import BaseResponse

class DeleteRecordingsResponse(BaseResponse):
    def is_deleted(self):
        field = self.get_field("deleted")
        return field == "true" or (isinstance(field, bool) and field)