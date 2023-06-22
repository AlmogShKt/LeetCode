# 210.Course Schedule
def findOrder(numCourses: int, prerequisites):
    pre_req = {c: [] for c in range(numCourses)}

    for crs, pre in prerequisites:
        pre_req[crs].append(pre)

    output = []
    visited, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visited:
            return True

        cycle.add(crs)

        for pre in pre_req[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return []

    return output


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
findOrder(numCourses, prerequisites)
