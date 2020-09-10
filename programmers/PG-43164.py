# https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    def dfs(current, visited):

        if len(path) == len(tickets):
            path.append(current)
            return True

        for i, ticket in enumerate(tickets):
            if not visited[i] and ticket[0] == current:
                visited[i] = True
                path.append(current)
                is_done = dfs(ticket[1], visited)
                if is_done:
                    return True
                path.pop()
                visited[i] = False
        return False

    visited = [False] * len(tickets)
    tickets.sort(key=lambda x:(x[0],x[1]))

    path = []
    dfs('ICN', visited)

    return path
