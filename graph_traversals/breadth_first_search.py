from typing import Dict, List, Tuple, Callable, Generator, Optional
import heapq


def breadth_first_search[T](start: T, end: T, neighbors: Callable[[T,int],Generator[Tuple[int,T],None,None]]) -> Optional[int]:
    # given a start point, an end point, a function that gives all neighbors
    scores: Dict[T,int] = {start: 0}
    queue: List[Tuple[int,T]] = [(0,start)]

    while queue:
        _, current = heapq.heappop(queue)
        current_score = scores[current]

        if current == end:
            return current_score

        for neighbor_score, neighbor in neighbors(current,current_score):
            if neighbor not in scores:
                scores[neighbor] = neighbor_score
                heapq.heappush(queue,(neighbor_score,neighbor))

            elif scores[neighbor] > neighbor_score:
                print('multi score')
                print(scores[neighbor], neighbor_score)
                exit(1)
            
            elif scores[neighbor] == neighbor_score:
                # add extra parent
                pass
            
            # else not a better score, continue
        
    
    return None
