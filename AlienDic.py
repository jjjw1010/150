# Invalid Solution, Still Working on it
def alienOrder(self, words: List[str]) -> str:
    def buildGraph(graph: Dict[str, Set[str]], words: List[str], inDegree: Dict[str, int]):
        # Create a node for each character in each word
        for word in words:
            for c in word:
                inDegree[c] = 0  # necessary for final char counting

        for first, second in zip(words, words[1:]):
            length = min(len(first), len(second))
            for j in range(length):
                u = first[j]
                v = second[j]
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        inDegree[v] += 1
                    break  # Later characters' order is meaningless
                if j == length - 1 and len(first) > len(second):
                    # If 'ab' comes before 'a', it's an invalid order
                    graph.clear()
                    return

    def topology(self, graph: Dict[str, Set[str]], inDegree: Dict[str, int]):
        result = ''
        q = collections.deque([c for c in inDegree if inDegree[c] == 0])

        while q:
            u = q.popleft()
            result += u
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        # If there are remaining characters in inDegree, it means there's a cycle
        if any(inDegree.values()):
            return ''

        # Words = ['z', 'x', 'y', 'x']
        return result if len(result) == len(indegree) else ''
    graph = collections.defaultdict(set)
    inDegree = collections.defaultdict(int)

    graph = buildGraph(graph, words, inDegree)
    return topology(graph, inDegree)