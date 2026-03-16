class ArrayObjectLogic:

    def filter_by_property(self,list_of_objects: list, case: str, value) -> list:
        result =[]
        for obj in list_of_objects:
            if case in obj and obj[case] == value:
                result.append(obj)
        return result
    
    def group_by(self, list_of_objects: list, case: str) -> dict:
        result = {}
        for obj in list_of_objects:
            if case in obj:
                key = obj[case]
                if key not in result:
                    result[key] = []
                result[key].append(obj)
        return result
    
    def find_intersection(self, list_object_1: list, list_object_2: list, case: str) -> list:
        result = []
        for obj1 in list_object_1:
            for obj2 in list_object_2:
                if case in obj1 and case in obj2 and obj1[case] == obj2[case]:
                    result.append(obj1)
                    break #Si déjà trouvé dans la deuxième liste, pas besoin de continuer à chercher
        return result

    def transform_array(self,list_of_objects: list, transformer: callable) -> list:
        result = []
        for obj in list_of_objects:
            result.append(transformer(obj)) #Transformation de chaque objet avec la fonction transformer fournie
        return result
    
    def aggregate_data(self,list_of_objects: list, category: str, case: str) -> dict:
        result = {}
        for obj in list_of_objects:
            if category in obj and case in obj:
                key = obj[category]
                value = obj[case]
                if key not in result:
                    result[key] = 0
                result[key] += value
        return result