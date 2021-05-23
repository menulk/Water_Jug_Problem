import collections

def main():
    start_node = [[0, 0]]
    jugs = get_jugs()
    target_capacity = get_target(jugs)
    check_dict = {}
    search(start_node, jugs, target_capacity, check_dict)

def get_index(node):
    return pow(7, node[0]) * pow(5, node[1])

#Get volume of the jugs
def get_jugs():
    
    jugs = []
    temp = int(input("Enter first jug volume: "))
    while temp < 1:
            temp = int(input("Enter a valid amount (>1): "))       
    jugs.append(temp)
    
    temp = int(input("Enter second jug volume: "))
    while temp < 1:
            temp = int(input("Enter a valid amount (>1): "))     
    jugs.append(temp)
    
    return jugs
    
#**Desired water capacity
def get_target(jugs):
  
    max_capacity = max(jugs[0], jugs[1])
    s = "Desired water capacity : ".format(max_capacity)
    target_capacity = int(input(s))
    while target_capacity < 1 or target_capacity > max_capacity:
        target_capacity = int(input("Enter a valid amount (1 - {0}): ".format(max_capacity)))
        
    return target_capacity

##

#**
def search(start_node, jugs, target_capacity, check_dict):
    
    target = []
    accomplished = False
    
    q = collections.deque()
    q.appendleft(start_node)
    
    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True
        if len(path) >= 2:
            print(transition(path[-2], path[-1], jugs), path[-1])
        if is_target(path, target_capacity):
            accomplished = True
            target = path
            break

        next_moves = next_transitions(jugs, path, check_dict)
        for i in next_moves:
                q.append(i)

    if accomplished:
        print("\nReached to the Target capacity : Sequence")
        print_path(target, jugs)
    else:
        print("Can't find a solution.")


if __name__ == '__main__':
    main()