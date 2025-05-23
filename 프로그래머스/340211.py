def solution(points, routes):
    # 포인트 번호 → 좌표 맵핑
    pos = {}
    for i, p in enumerate(points):
        pos[i+1] = (p[0], p[1])
    
    # 시간별로 좌표별 로봇 수
    path_count = [{} for _ in range(100001)]
    answer = 0

    def movePath(r):
        nonlocal answer
        time = 0
        # r: [1, 2, 3, 4] 같은 경로 리스트
        for i in range(len(r) - 1):
            s = list(pos[r[i]])
            e = pos[r[i+1]]
            final = e

            while tuple(s) != e:
                # 현재 시간, 좌표에 로봇 1대 도착
                path_count[time][tuple(s)] = path_count[time].get(tuple(s), 0) + 1
                if path_count[time][tuple(s)] == 2:
                    answer += 1
                dy = s[0] - e[0]
                dx = s[1] - e[1]
                if dy != 0:
                    if dy > 0:
                        s[0] -= 1
                    else:
                        s[0] += 1
                elif dx != 0:
                    if dx > 0:
                        s[1] -= 1
                    else:
                        s[1] += 1
                time += 1
        # 도착점
        path_count[time][final] = path_count[time].get(final, 0) + 1
        if path_count[time][final] == 2:
            answer += 1

    for route in routes:
        movePath(route)

    return answer
