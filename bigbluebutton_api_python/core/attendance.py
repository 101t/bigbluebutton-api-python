class Attendance:
    def __init__(self, xml):
        self.__extId = xml["extId"]
        self.__name = xml["name"]
        self.__startTime = xml["createdOn"]
        self.__endTime = xml["endedOn"]
        self.__users = {}
        if xml.get("users", []):
            self.set_users(xml)

    def set_users(self, xml):
        for user in xml["users"]:
            for attendee in xml["users"][user]["intIds"]:
                self.__users[xml["users"][user]["name"]] = {
                    "registeredOn": xml["users"][user]["intIds"][attendee]["registeredOn"],
                    "leftOn": xml["users"][user]["intIds"][attendee]["leftOn"],
                    "userLeftFlag": xml["users"][user]["intIds"][attendee]["userLeftFlag"]
                }
            
    def get_users(self):
        return self.__users

    def get_name(self):
        return self.__name

    def get_starttime(self):
        return self.__startTime

    def get_endtime(self):
        return self.__endTime

    def get_meta(self, name):
        return self.meta.get_meta(name)
