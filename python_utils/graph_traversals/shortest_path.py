from typing import Dict, List, Tuple, Callable, Iterator, Optional
import heapq


def dijkstra_parents[T](start: T, end: Callable[[T],bool], neighbors: Callable[[T,int],Iterator[Tuple[int,T]]]) -> Tuple[Optional[int],Dict[T,List[T]]]:
    
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

        for edge_score, neighbor in neighbors(current,current_score):
            neighbor_score = current_score + edge_score
            if neighbor not in scores or scores[neighbor] > neighbor_score:
                scores[neighbor] = neighbor_score
                parents[neighbor] = [current]
                heapq.heappush(queue,(neighbor_score,neighbor))

            elif scores[neighbor] == neighbor_score:
                # add extra parent
                parents[neighbor].append(current)
            
            # else not a better score, continue
        
    
    return None, parents


def dijkstra[T](start: T, end: Callable[[T],bool], neighbors: Callable[[T,int],Iterator[Tuple[int,T]]]) -> Optional[int]:
    """Finds the shortest (smallest edge-weight) path from the start node to a node considered the end.
    
    Give the starting node
    
    Give a predicate function for determining the end. Can be as simple as lambda x: x == end

    The graph is implied by the neighbors function. The neighbors function takes the current node, and the current score, and yields all neighbors and the edge weight for each
    
    If you need the path returned, try dijkstra_parents"""
    
    
    
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

        for edge_score, neighbor in neighbors(current,current_score):
            neighbor_score = current_score + edge_score
            if neighbor not in scores or scores[neighbor] > neighbor_score:
                scores[neighbor] = neighbor_score
                heapq.heappush(queue,(neighbor_score,neighbor))
            
            # else not a better score, continue
        
    
    return None


def a_star_parents[T](start: T, end: T, neighbors: Callable[[T,int],Iterator[Tuple[int,T]]],h: Callable[[T,T],int]) -> Tuple[Optional[int],Dict[T,List[T]]]:
    """A star finds the shortest path on a given a good idea of what the graph (usually a grid)
    
    start node, end node
    
    neighbors function: generates all neighbors from the current node
    
    h: function that estimates the distance (number of steps, edge weight total) to the goal"""

    
    scores: Dict[T,int] = {start: 0}
    parents: Dict[T,List[T]] = {}
    queue: List[Tuple[int,T]] = [(h(start,end),start)]

    while queue:
        _, current = heapq.heappop(queue)
        current_g_score = scores[current]

        if current == end:
            return current_g_score, parents

        for edge_score, neighbor in neighbors(current,current_g_score):
            neighbor_g_score = current_g_score + edge_score
            
            if neighbor not in scores or scores[neighbor] > neighbor_g_score:
                scores[neighbor] = neighbor_g_score
                f_score = neighbor_g_score + h(neighbor,end)
                parents[neighbor] = [current]
                heapq.heappush(queue,(f_score,neighbor))
            
            elif scores[neighbor] == neighbor_g_score:
                # add extra parent
                parents[neighbor].append(current)

            # else not a better score, continue
        
    
    return None, parents


def a_star[T](start: T, end: T, neighbors: Callable[[T,int],Iterator[Tuple[int,T]]],h: Callable[[T,T],int]) -> Optional[int]:
    """A star finds the shortest path on a given a good idea of what the graph (usually a grid)
    
    start node, end node
    
    neighbors function: generates all neighbors from the current node
    
    h: function that estimates the distance (number of steps, edge weight total) to the goal"""

    
    scores: Dict[T,int] = {start: 0}
    queue: List[Tuple[int,T]] = [(h(start,end),start)]

    while queue:
        _, current = heapq.heappop(queue)
        current_g_score = scores[current]

        if current == end:
            return current_g_score

        for edge_score, neighbor in neighbors(current,current_g_score):
            neighbor_g_score = current_g_score + edge_score
            
            if neighbor not in scores or scores[neighbor] > neighbor_g_score:
                scores[neighbor] = neighbor_g_score
                f_score = neighbor_g_score + h(neighbor,end)
                heapq.heappush(queue,(f_score,neighbor))

            # else not a better score, continue
        
    
    return None

