# pylint: skip-file
# type: ignore

class TypedAppRepository():
    def __init__(self, cursor):
        self._cursor = cursor
        print("app repository initialized")

    def countAllResourceGroupByType(self):
        return self._cursor.execute(
            f'SELECT COUNT("resource"."id"), "resource"."type" FROM "resource" GROUP BY "resource"."type"'
        )