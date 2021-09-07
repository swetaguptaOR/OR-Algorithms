#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Memozining Approach for Knapsack Problem
#Defining a -1 matrix
t=[[-1 for i in range(capacity+1)] for x in range(n+1)]
#Defining the knapsack function
def knapsack(value,weight,capacity,n):
               #If there is no capacity or no item
                if(value==0 or n==0):
                    return 0
                #Checking the memozizied matrix
                elif(t[n][capacity]!=-1):
                    return t[n][capacity]
                #Defining reccursive function
                elif(weight[n-1]<=capacity):
                    return max(value[n-1]+ knapsack(value,weight,capacity-weight[n-1],n-1),knapsack(value,weight,capacity,n-1))
                #Checking the function when capacity is higher
                else:
                    return knapsack(value,weight,capacity,n-1)


# In[23]:


#Driver Function
value=[100,300,120]
weight=[10,20,30]
capacity=50
n=len(value)
print(knapsack(value,weight,capacity,n))


# In[ ]:




