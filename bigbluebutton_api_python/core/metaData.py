class MetaData:
    def __init__(self, xml):
        self.meta = {}
        for element in xml:
            self.meta[element] = xml[element]

    def get_meta(self, name):
        if self.meta.keys().__contains__(name):
            return self.meta[name]
        return None
