class MetaData:
    def __init__(self, xml):
        self.meta = {}
        for element in xml.iterchildren():
            self.meta[element.tag] = element.text

    def get_meta(self, name):
        if self.meta.keys().__contains__(name):
            return self.meta[name]
        return None
