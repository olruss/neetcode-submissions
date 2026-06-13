class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # let's create an adjustency list
        # but not course: prerequesite
        # but course: [this cource is prerequisite for ...]
        # so it's kind of inverted graph
        #
        # all courses that don't have prerequisites - they are strating points
        # they can be completed (and should be completed first)
        # 
        # so now we can go BFS from those courses and down
        # on every level we will add courses to completed
        # and add to seen
        # if cycle detected - fail
        # if uncompleted courses left - fail
        # add to queue, only when course don't have prerequisites (counter)

        adj = {i: [] for i in range(numCourses)}
        prereq_cnt = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            prereq_cnt[a] += 1

        # seeding with courses that don't have prerequesites
        q = deque([i for i, c in enumerate(prereq_cnt) if c == 0])
        # no need to track seen
        # because we only adding nodes that don't have prerequisites
        # seen = set()
        completed = []
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                completed.append(c)
                for p in adj[c]:
                    prereq_cnt[p] -= 1
                    if prereq_cnt[p] == 0:
                        q.append(p)

        return completed if len(completed) == numCourses else []