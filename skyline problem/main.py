class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #structure scan
        structures = [[]]
        x = 0
        for b in buildings:
            if b[0] == 0:
                structures[0].append(b)
            elif b[0] > x:
                
            structures[-1].append(b)
            .sort(key=lambda b: b[2])
            x = b[1]
            structures.append([])

        #vertex form transformation
        def vertex(b: List[int], n: str):
            match n:
                case 'l':
                    return [b[0], b[2]]
                case 'r':
                    return [b[1], b[2]]

        # vertexes = []
        # for s in structures:
        #     v=[]
        #     for b in s:
        #         v.append([b[0], b[2]], [b[1], b[2]])
        #     vertexes.append(v)

        #I'm so smart
        result = []
        for s in structures:
            result.append(vertex(s[0],'l'))
            result.append([s[0][1], )
            skylineEdges = [s[0][0], s[0][1]]
            for b in s[1:]:
                if 

        #final answer
        for s in structures:
            lookuptable such that when x2 is searched, it goes 'case x1->x3, doing y                    '