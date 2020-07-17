# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    graph_in = {}
    graph_out = {}
    # visited = [False for _ in range(n)]

    for i in range(1, n+1):
        graph_in[i] = set()
        graph_out[i] = set()

    for i in range(1, n+1):
        # update graph_out(win) and graph_in(lose) for given results
        for battle in results:
            # win
            if battle[0] == i:
                graph_out[i].add(battle[1])
            # lost
            elif battle[1] == i:
                graph_in[i].add(battle[0])

        # if k -> i and i -> j, then k -> j

        # the players who i won should be beaten by players who won i as well
        for j in graph_out[i]:
            graph_in[j].update(graph_in[i])

        # the players who won i should win the players who i won as well
        for j in graph_in[i]:
            graph_out[j].update(graph_out[i])

    answer = 0
    for i in range(1,n+1):
        if len(graph_out[i])+len(graph_in[i]) == n-1:
            answer += 1
    return answer
