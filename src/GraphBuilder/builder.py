
class GraphBuilder:

    def __init__(self, **args):
        from GraphBuilder.utils.utils import read_csv
        
        if args["data"]: 
            self.data_path = args["data"]
            self.data = read_csv(self.data_path)
        else:
            raise Exception("Provide data path")


    def run(self):
        from GraphBuilder.db.models import (
            Person, Country, Field
        )
        # print(len(self.data))
        for inst in self.data:
            professor = Person(name = inst["name"]).save()
            if not Country.nodes.get_or_none(code = inst["country"]):
                country = Country(code = inst["country"]).save()
            if not Field.nodes.get_or_none(name = inst["field"]):
                field = Field(name = inst["field"]).save()

            professor.country.connect(country)
            professor.field.connect(field)

    

    

    