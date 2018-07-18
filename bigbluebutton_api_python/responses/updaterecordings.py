from .base import BaseResponse

class UpdateRecordingsResponse(BaseResponse):
    def is_updated(self):
        field = self.get_field("updated")
        return field == "true" or (isinstance(field, bool) and field)