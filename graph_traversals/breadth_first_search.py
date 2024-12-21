from typing import Dict, List, Tuple, Callable, Iterator, Optional, Union
import heapq


def breadth_first_search_parents[T](start: T, end: Callable[[T],bool], neighbors: Callable[[T,int],Iterator[Tuple[int,T]]]) -> Tuple[Optional[int],Dict[T,List[T]]]:
    # given a start point, an end point (or a function to say it is the end), a function that gives all neighbors
    
    scores: Dict[T,int] = {start: 0}
    parents: Dict[T,List[T]] = {}
    queue: List[Tuple[int,T]] = [(0,start)]

    while queue:
        queue_score, current = heapq.heappop(queue)
        current_score = scores[current]
        if queue_score > current_score:
            # this means that some other path was deemed better and this state
            # has already been checked
            continue

        if end(current):
            return current_score, parents

        for neighbor_score, neighbor in neighbors(current,current_score):
            if neighbor not in scores:
                scores[neighbor] = neighbor_score
                parents[neighbor] = [current]
                heapq.heappush(queue,(neighbor_score,neighbor))

            elif scores[neighbor] > neighbor_score:
                scores[neighbor] = neighbor_score
                parents[neighbor] = [current]
                heapq.heappush(queue,(neighbor_score,neighbor))
            
            elif scores[neighbor] == neighbor_score:
                # add extra parent
                parents[neighbor].append(current)
            
            # else not a better score, continue
        
    
    return None, parents


def breadth_first_search[T](start: T, end: Callable[[T],bool], neighbors: Callable[[T,int],Iterator[Tuple[int,T]]]) -> Union[int,Tuple[int,Dict[T,T]],None]:
    # given a start point, an end point (or a function to say it is the end), a function that gives all neighbors
    
    scores: Dict[T,int] = {start: 0}
    queue: List[Tuple[int,T]] = [(0,start)]

    while queue:
        queue_score, current = heapq.heappop(queue)
        current_score = scores[current]
        if queue_score > current_score:
            # this means that some other path was deemed better and this state
            # has already been checked
            continue

        if end(current):
            return current_score

        for neighbor_score, neighbor in neighbors(current,current_score):
            if neighbor not in scores:
                scores[neighbor] = neighbor_score
                heapq.heappush(queue,(neighbor_score,neighbor))

            elif scores[neighbor] > neighbor_score:
                scores[neighbor] = neighbor_score
                heapq.heappush(queue,(neighbor_score,neighbor))
            
            # else not a better score, continue
        
    
    return None
