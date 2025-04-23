from collections import defaultdict


class Network:

    def __init__(self, N, M):
        self.N, self.M = N, M
        self.cnt = 0
        self.visited = [False] * (N + 1)
        self.visited[1] = True
        self.network = defaultdict(list)
        self._make_network()

    def _make_network(self):
        for _ in range(self.M):
            s, e = map(int, input().split())
            self.network[s].append(e)
            self.network[e].append(s)

    def search_computer(self, node=1):
        for n_node in self.network[node]:
            if self.visited[n_node]:
                continue
            self.visited[n_node] = True
            self.cnt += 1
            self.search_computer(n_node)


def main():
    N = int(input())
    M = int(input())

    network = Network(N, M)
    network.search_computer()
    print(network.cnt)


if __name__ == "__main__":
    main()
