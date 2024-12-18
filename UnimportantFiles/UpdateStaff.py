def page_replacement_optimal(n, m, pages):
    buffer = set()
    reads = 0

    for i in range(n):
        page = pages[i]

        if page in buffer:
            continue

        reads += 1

        if len(buffer) < m:
            buffer.add(page)
        else:
            farthest_page = -1
            farthest_distance = -1

            for p in buffer:
                if p not in pages[i + 1:]:
                    farthest_page = p
                    break
                else:
                    next_index = pages[i + 1:].index(p) + i + 1
                    if next_index > farthest_distance:
                        farthest_distance = next_index
                        farthest_page = p

            buffer.remove(farthest_page)
            buffer.add(page)

    return reads

if __name__ == '__main__':
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))

    print(page_replacement_optimal(n, m, pages))
