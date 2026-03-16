import math

class ObjectLogic:

    type_mapping = {
        "string": str,
        "number": int,
        "boolean": bool,
        "float": float
    }

    def get_values(self, object : dict) -> list:
        return list(object.values())
    
    def transform_values(self, object : dict, value : int) -> dict:
        return {key: val * value for key, val in object.items()}
    
    def merge_objects(self, object1 : dict, object2 : dict) -> dict:
        res = object1.copy()
        for key, value in object2.items():
            if key in res:
                res[key] += value
            else:
                res[key] = value
        return res
    
    def filter_object(self, object : dict, value : int) -> dict:
        res = {}
        for key, val in object.items():
            if val <= value:
                res[key] = val
        return res
    
    def flat_to_nested(self, object : dict) -> dict:
        res = {}
        for key, value in object.items():
            keys = key.split('.')
            current = res
            for k in keys[:-1]:
                if k not in current:
                    current[k] = {}
                current = current[k]
            current[keys[-1]] = value
        return res
    
    def find_keys_by_value(self, object : dict, value : int) -> list:
        list_of_keys = []
        for key, val in object.items():
            if val == value:
                list_of_keys.append(key)
        return list_of_keys
    
    def create_object_from_arrays(self, list_a : list, list_b : list) -> dict:
        if len(list_a) != len(list_b):
            raise ValueError("Les deux listes doivent avoir la même longueur")
        result = {}
        for i in range(len(list_a)):
            result[list_a[i]] = list_b[i]
        return result
    
    def count_values(self, object : dict) -> dict:
        result = {}
        for key, val in object.items():
            if val in result:
                result[val] += 1
            else:
                result[val] = 1
        return result
    
    def extract_properties(self, object : dict, properties : list) -> dict:
        result = {}
        for prop in properties:
            if prop in object:
                result[prop] = object[prop]
        return result
    
    def sort_object_by_value(self, object: dict) -> dict:
        return dict(sorted(object.items(), key=lambda item: item[1]))
    
    def find_max_value(self, object: dict) -> dict:
        if not object:
            return None
        values = []
        for key, value in object.items():
            values.append(value)
        return max(values)
    
    def create_object_from_pairs(self, list_of_object: list) -> dict:
        result = {}
        for obj in list_of_object:
                result[obj[0]] = obj[1]
        return result
    
    def find_value_in_object(self, object: dict, value) -> bool:
        for key, val in object.items():
            if val == value:
                return True
            if isinstance(val, dict):
                if self.find_value_in_object(val, value):
                    return True
        return False
    
    def group_by_property(self, list_of_objects: list, value: str) -> dict:
        result = {}
        for obj in list_of_objects:
            if value in obj:
                key = obj[value]
                if key not in result:
                    result[key] = []
                result[key].append(obj)
        return result
    
    def validate_object(self, schema: dict, object: dict) -> bool:
        for key, val in schema.items():
            if key not in object or not isinstance(object[key], self.type_mapping[val]):
                return False
        return True
    
    def compare_differences(self, object_1 : dict, object_2 : dict) -> dict:
        result = {}
        for key in object_1:
            if key not in object_2:
                result[key] = {"type": "deleted", "old": object_1[key]}
            elif object_1[key] != object_2[key]:
                result[key] = {"type": "modified", "old": object_1[key], "new": object_2[key]}
        for key in object_2:
            if key not in object_1:
                result[key] = {"type": "added", "new": object_2[key]}
        return result
    
    def object_to_url_params(self, object: dict) -> str:
        params = []
        for key, value in object.items():
            val = value
            if isinstance(val, str) and " " in val:
                val = val.replace(" ", "%20")
            params.append(f"{key}={val}")
        return "&".join(params)
    
    def calculate_median(self, values: list) -> float:
        sorted_list = sorted(values)
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]
    
    def calculate_variance(self, values: list) -> float:
        mean = sum(values) / len(values)
        return (1/len(values) * sum((x - mean) ** 2 for x in values))

    def calculate_standard_deviation(self, values: list) -> float: #Ecart type
        variance = self.calculate_variance(values)
        return variance ** 0.5

    def get_object_stats(self, object: dict) -> dict:
        stats = {
            "basic": {
                "min": min(object.values()) if object else None,
                "max": max(object.values()) if object else None,
                "average": int(sum(object.values()) / len(object)) if object else None,
                "total": sum(object.values()) if object else None
            },
            "advanced": {
                "median": int(self.calculate_median(object.values())) if object else None,
                "variance": int(self.calculate_variance(object.values())) if object else None,
                "standardDeviation": round(self.calculate_standard_deviation(object.values()),2) if object else None
            }
        }
        return stats