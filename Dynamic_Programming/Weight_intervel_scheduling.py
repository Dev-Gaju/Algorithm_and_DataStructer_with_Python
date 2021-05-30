# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search

# Class to represent a job
class Job:
    def __init__(self, start, end, profit):
        self.start= start
        self.end =end
        self.profit = profit


 # A Binary Search based function to find the latest job
    # (before current job) that doesn't conflict with current
    # job. "index" is index of the current job. This function
    # returns -1 if all jobs before index conflict with it.

def Binary_search(job, start_index):

    low =0
    high= start_index-1
    while low <=high:
        mid =(low +high )//2
        if job[mid].end <= job[start_index].start:
            if job[mid+1].end <= job[start_index].start:
                low = mid+1
            else:
                return mid
        else:
            high = mid-1
    return -1
# The main function that returns the maximum possible
    # profit from given array of jobs

def Schedule(job):
    # Sort jobs according to start time
    job =sorted(job, key=lambda j: j.start)
    # Create an array to store solutions of subproblems. table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]
    table[0]= job[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, n):
        # Find profit including the current job
        inclProof = job[i].profit
        legth= Binary_search(job, i)
        if (legth != -1):
            inclProof += table[1]
        # Store maximum of including and excluding
        table[i] = max(inclProof, table[i-1])
    return table[n-1]

# Driver code to test above function

job = [Job(1,2,50), Job(3,5,20), Job(6, 19,100), Job(2,100,200)]
print("Optimal Profit is", Schedule(job))



