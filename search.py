        # search.py
    # ---------bsc/com/ne/09/17


    """
    In search.py, you will implement generic search algorithms which are called by
    Pacman agents (in searchAgents.py).
    """

    import util

    class SearchProblem:
        """
        This class outlines the structure of a search problem, but doesn't implement
        any of the methods (in object-oriented terminology: an abstract class).

        You do not need to change anything in this class, ever.
        """

        def getStartState(self):
            """
            Returns the start state for the search problem.
            """
            util.raiseNotDefined()

        def isGoalState(self, state):
            """
              state: Search state

            Returns True if and only if the state is a valid goal state.
            """
            util.raiseNotDefined()

        def getSuccessors(self, state):
            """
              state: Search state

            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'act ion' is the action required to get there, and 'stepCost' is
            the incremental cost of expanding to that successor.
            """
            util.raiseNotDefined()

        def getCostOfActions(self, actions):
            """
             actions: A list of actions to take

            This method returns the total cost of a particular sequence of actions.
            The sequence must be composed of legal moves.
            """
            util.raiseNotDefined()


    def tinyMazeSearch(problem):
        """
        Returns a sequence of moves that solves tinyMaze.  For any other maze, the
        sequence of moves will be incorrect, so only use this for tinyMaze.
        """
        from game import Directions
        s = Directions.SOUTH
        w = Directions.WEST
        return  [s, s, w, s, w, w, s, w]

    def depthFirstSearch(problem):

        """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print("Start:", problem.getStartState())
        print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
        print("Start's successors:", problem.getSuccessors(problem.getStartState()))
        """

        "*** YOUR CODE HERE ***"
        "***This  is my code  here***"

        # DFS is general graph search with a Stack as the data structure
        #STACK works on the principle of Last-in First-out(LIFO)
        stack=util.Stack()   #use  stack data structure already provided in util.py, Initialize an empty Stack
        visited=[]     # visited states listed 
        startNode=(problem.getStartState(),[])       # current empty state   
        stack.push(startNode) # adds initial state to stack 
        while not stack.isEmpty(): #
            popped=stack.pop()  #remove the last item(top item) from the stack
            location=popped[0] 
            path=popped[1]                            #Every state keeps it's path from the starting state
            if location not in visited:               #if it's not then we are getting the successors and push
                visited.append(location)              # building the path in depth-first logic
                if problem.isGoalState(location):     # Check if current state = goal state
                    return path                     #return the path(from startnode) that leads to this location(if is it a goal state)
                successors=problem.getSuccessors(location) # Get successors of current state
                for succ in list(successors):   
                    if succ[0] not in visited:
                        stack.push((succ[0],path+[succ[1]])) # new states in stack and find  new path (new action) 
        return []
        util.raiseNotDefined()

    def breadthFirstSearch(problem):
        """Search the shallowest nodes in the search tree first."""
        "*** YOUR CODE HERE ***"
        "***This  is my code  here***"
         
         #QUEUE works on the principle of First-in first-out(FIFO)
         #POP removes remove first node that was pushed into the list,(instead of last node as in STACK)

        queue=util.Queue() #initialise an empty queue
        visited=[]        #list of visited states                                              
        startNode=(problem.getStartState(),[])   # initial/start state is current state, the list(path) is empty here                        
        queue.push(startNode) 
        while not queue.isEmpty():
            popped=queue.pop()
            location=popped[0]
            path=popped[1]
            if location not in visited:
                visited.append(location)
                if problem.isGoalState(location):
                    return path
                successors=problem.getSuccessors(location) 
                for suc in list(successors):
                    if suc[0] not in visited:
                        queue.push((suc[0],path + [suc[1]]))
        return []
        util.raiseNotDefined()



    def uniformCostSearch(problem):
        """Search the node of least total cost first."""
        "*** YOUR CODE HERE ***"

         # UCS is general graph search with the PriorityQueue sorting by the cost as the data structure
         # The cost for UCS only the backward cost


        priority_queue=util.PriorityQueue() # Construct an empty priority queue that sorts using this backwards cost 
        visited=dict() #create a dictionary of all the visted nodes
        state=problem.getStartState()
        nd = {}
        nd["pred"]=None                                                             
        nd["act"]=None                                                              
        nd["state"]=state
        nd["cost"]=0
        priority_queue.push(nd,nd["cost"])

        while not priority_queue.isEmpty():
            nd=priority_queue.pop()
            state=nd["state"]
            cost=nd["cost"]

            if state in visited:
                continue
            visited[state]=True
            if problem.isGoalState(state)==True:
                break
            for suc in problem.getSuccessors(state):
                if not suc[0] in visited:
                    new_nd={}
                    new_nd["pred"]=nd
                    new_nd["state"]=suc[0]
                    new_nd["act"]=suc[1]
                    new_nd["cost"]=suc[2]+cost
                    priority_queue.push(new_nd,new_nd["cost"])
        actions=[]
        while nd["act"] !=None:
            actions.insert(0,nd["act"])
            nd=nd["pred"]
        return actions
        util.raiseNotDefined()

       

    def nullHeuristic(state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest
        goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0

    def aStarSearch(problem, heuristic=nullHeuristic):
        """Search node that has the lowest combined cost and heuristic first."""
        "*** YOUR CODE HERE ***"

        priority_queue=util.PriorityQueue()
        visited=dict()


        state=problem.getStartState()
        nd={}
        nd["pred"]=None
        nd["act"]=None
        nd["state"]=state
        nd["cost"]=0
        nd["eq"]=heuristic(state,problem)
        priority_queue.push(nd,nd["cost"]+nd["eq"])

        while not priority_queue.isEmpty():
            nd=priority_queue.pop()
            state=nd["state"]
            cost=nd["cost"]
            v=nd["eq"]
                                                                                    
            if state in visited:                                              # cost = cost+ heuristic combined
                continue
            visited[state]=True
            if problem.isGoalState(state)==True:
                break
            for suc in problem.getSuccessors(state):
                if not suc[0] in visited:
                    new_nd={}
                    new_nd["pred"]=nd
                    new_nd["state"]=suc[0]
                    new_nd["act"]=suc[1]
                    new_nd["cost"]=suc[2] + cost
                    new_nd["eq"]=heuristic(new_nd["state"],problem)
                    priority_queue.push(new_nd,new_nd["cost"]+new_nd["eq"])
        actions= []
        while nd["act"]!=None:
            actions.insert(0,nd["act"])
            nd=nd["pred"]
        return actions
       
        util.raiseNotDefined()


    # Abbreviations used 

    dfs = depthFirstSearch
    astar = aStarSearch
    bfs = breadthFirstSearch
    ucs = uniformCostSearch
