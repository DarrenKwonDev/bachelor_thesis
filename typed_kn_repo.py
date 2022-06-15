# pylint: skip-file
# type: ignore

class TypedKNRepository():
    def __init__(self, cursor):
        self._cursor = cursor
        print("kn repository initialized")

    def countAllNode(self):
        return self._cursor.execute(
            f'SELECT COUNT("graph_node"."id") FROM "graph_node"'
        )

    def countAllEdge(self):
        return self._cursor.execute(
            f'SELECT COUNT("graph_edge"."id") FROM "graph_edge"'
        )

    def countNodeGroupByType(self):
        return self._cursor.execute(
            f'SELECT COUNT("graph_node"."id"), "graph_node"."node_type" FROM "graph_node" GROUP BY "graph_node"."node_type"'
        )

    def countEdgeEachNode(self):
        # 자기 자신을 edge로 가지고 있어 COUNT에서 1을 빼야 함.
        return self._cursor.execute(
            f'SELECT COUNT("graph_node"."id") - 1 FROM "graph_node" \
            LEFT JOIN "graph_edge" ON "graph_node"."id" = "graph_edge"."source_id" \
            GROUP BY "graph_node"."id"'
        )

    def countEdgeGroupBySourceId(self):
        return self._cursor.execute(
            f'SELECT COUNT("graph_edge"."id") FROM "graph_edge" GROUP BY "graph_edge"."source_id" \
            ORDER BY COUNT("graph_edge"."id") DESC'
        )

    def countSingletonNode(self):
        return self._cursor.execute(
            f'SELECT COUNT("graph_node"."id") FROM "graph_node" \
            LEFT JOIN "graph_edge" ON "graph_node"."id" = "graph_edge"."source_id" \
            WHERE "graph_edge"."id" IS NULL'
        )

    def getDocumentByUserId(self, userId):
        return self._cursor.execute(
            f'SELECT "graph_node"."metadata", "graph_node"."id", "graph_node"."title" FROM "graph_node" \
            WHERE "graph_node"."user_id" = \'{userId}\' AND "graph_node"."node_type" = \'document\''
        )
    
    def getDocumentDegreeByDocumentId(self, docId):
        return self._cursor.execute(
            f'SELECT COUNT("graph_edge"."id") FROM "graph_edge" \
            WHERE "graph_edge"."source_id" = \'{docId}\''
        )
