# all functions listed in the assignment description should be documented somewhat like the style below
"""
    Description of Function
    :param name: what is the parameter? (You don't need to do this for "self")
    :param name 2: (if you have other parameters, add them like above)
    :return: What does the function return, if anything?
    :time complexity: Runs in O(something) time, where something is (describe what something is)
                        (Explain why it in runs in O(something) time)
"""

############################## PUT YOUR CLASSES, METHODS, ETC HERE ##############################



########################################### MAIN ASSIGNMENT ###########################################
#make sure you put PJ02_assertions.py in the same directory as your project 2 file
import PJ02_assertions as pj  # DO NOT REMOVE OR MODIFY THIS LINE
#Note: contents of PJ02_assertions.py will change when this project is being graded
print("\n########################################### MAIN ASSIGNMENT  ###########################################")

T = BST() # make an instance of your BST class

with open('input.txt', 'r') as infile: #Don't modify this line

    # YOU CAN MODIFY THIS SECTION FROM THIS POINT UNTIL THE BEGINNING OF THE TESTS SECTION
    pass # obviously you'll want to remove this line at some point

    # read in MAX 
    max_val = int(infile.readline().strip())
    #insert the numbers 1 through MAX (1 is included, MAX is not) in your tree
    for i in range(1, max_val):
        T.insert(i)
    # read in N
    n_pairs = int(infile.readline().strip())
    # read in values to add and remove
    for _ in range(n_pairs):
        insert_val, remove_val = map(int, infile.readline().split())
    # add and remove the values from the tree
        T.insert(insert_val)  
        T.remove(remove_val)


    # read in M
    m_queries = int(infile.readline().strip())
    # read in the values to get the rank of (rank_num)
    for _ in range(m_queries):
        rank_query = int(infile.readline().strip())
    # print the rank of each value
    print(T.get_rank(rank_query))

    # read in K
    k_queries = int(infile.readline().strip())
    # read in low and high values (low and high)
    for _ in range(k_queries):
        low, high = map(int, infile.readline().split())
    # print number of keys in the range (where low is included and high is not)
    print(T.range_count(low, high))
    
########################################### TESTS  ###########################################

#                                   DO NOT MODIFY THIS SECTION!
# These tests are designed to help guide you through the project -- you are still 
# responsible for ensuring that your output from reading the input file is accurate and your code works as intended!

print("\n########################################### TESTS  ###########################################")

#Build/reset a tree. Also tests inserting a node to an empty tree
def build_tree():
    Test_tree = BST()
    for item in pj.Test_tree_list:
        Test_tree.insert(item)
        if item == pj.root_key_assert:
            assert Test_tree.root.key == pj.root_key_assert, "insert() isn't working correctly when tree is empty"
    return Test_tree

Test_tree = build_tree()

#list of references to nodes
node_list = []
for item in pj.Test_tree_list:
    node_list.append(Test_tree.search(item))

# generate lists to test against
key_list = [node.key for node in node_list]
size_list = [node.size for node in node_list]
min_list = [Test_tree.find_min(node).key for node in node_list]
max_list = [Test_tree.find_max(node).key for node in node_list]
successor_list = [Test_tree.find_successor(node).key if Test_tree.find_successor(node) is not None else None for node in node_list]
predecessor_list = [Test_tree.find_predecessor(node).key if Test_tree.find_predecessor(node) is not None else None for node in node_list]
get_rank_list = [Test_tree.get_rank(node.key) for node in node_list]
range_count_list = [Test_tree.range_count(node.key, pj.count_range_max_val) for node in node_list]

# print(key_list)
# print(size_list)
# print(min_list)
# print(max_list)
# print(successor_list)
# print(predecessor_list)
# print(get_rank_list)
# print(range_count_list)

# Test 1
# search() and/or insert()
assert key_list == pj.Test_tree_list\
    ,f"search() and/or insert() is not working correctly\
        \nexpected output:{pj.Test_tree_list}\
        \nyour output:\t{key_list}"

print("Test 1 passed")

# Test 2
# Check to see that node sizes are updated when nodes are inserted
assert size_list == pj.size_list_assert\
    ,f"make sure you update your node sizes when inserting nodes\
        \nexpected output:{pj.size_list_assert}\
        \nyour output:\t{size_list}"

print("Test 2 passed")

# Test 3
# Test find_min() 
assert min_list == pj.min_list_assert\
    ,f"find_min() isn't working correctly\
        \nexpected output:{pj.min_list_assert}\
        \nyour output:\t{min_list}"

# Test find_max()
assert max_list == pj.max_list_assert\
    ,f"find_max() isn't working correctly\
        \nexpected output:{pj._list_assert}\
        \nyour output:\t{max_list}"

print("Test 3 passed")

# Test 4
# Test find_successor()
assert successor_list == pj.successor_list_assert\
    ,f"find_successor() isn't working correctly\
        \nexpected output:{pj.successor_list_assert}\
        \nyour output:\t{successor_list}"

# Test find_predecessor()
assert predecessor_list == pj.predecessor_list_assert\
    ,f"predecessor_list() isn't working correctly\
        \nexpected output:{pj.predecessor_list_assert}\
        \nyour output:\t{predecessor_list}"

print("Test 4 passed")

# Test 5
#Test all traversal methods
assert Test_tree.traverse_inorder() == pj.inorder_assert, "traverse_inorder() not working correctly"
assert Test_tree.traverse_preorder() == pj.preorder_assert, "traverse_preorder() not working correctly"
assert Test_tree.traverse_postorder() == pj.postorder_assert, "traverse_postorder() not working correctly"

print("Test 5 passed")

# Test 6
# Test get_rank()
assert get_rank_list == pj.get_rank_assert_list\
    ,f"get_rank() isn't working correctly\
        \nexpected output:{pj.get_rank_assert_list}\
        \nyour output:\t{get_rank_list}"

print("Test 6 passed")

# Test 7
# Test range_count()
assert range_count_list == pj.count_range_assert_list\
    ,f"range_count is not working correctly\
        \nexpected output:{pj.count_range_assert_list}\
        \nyour output:\t{range_count_list}"

print("Test 7 passed")

#Test remove() -- any issues here could be with remove() or any functions that remove() uses, like transplant(), find_min(), etc.
#Also checks to see that node sizes are updated when a node is removed
after_removal_preorder_traversal_list = []
after_removal_node_sizes_list = []

# create the two lists above 
for item in pj.Test_tree_list:
    Test_tree = build_tree() # reset tree back to its original state
    Test_tree.remove(item) # remove node from tree

    # generate list of tree (in preorder traversal) after the node is deleted
    preorder_list = Test_tree.traverse_preorder()
    after_removal_preorder_traversal_list.append((preorder_list, item))

    # generate list of node sizes for each tree
    after_removal_node_sizes_list.append([Test_tree.search(node).size for node in preorder_list])

# reset Test_tree back to its original state
Test_tree = build_tree() 

# See if nodes can be deleted without messing up the tree
for index,list in enumerate(after_removal_preorder_traversal_list):
    if list[1] in pj.remove_case_list.keys():
        case = pj.remove_case_list[list[1]]
    else:
        case = None
# Test 8
    assert list[0] == pj.after_removal_preorder_assert[index]\
        ,f"remove() or one of its helper isn't working correctly when node removed had key = {list[1]}\
            \nexpected output:{pj.after_removal_preorder_assert[index]}\
            \nyour output:\t{list[0]}\n{'' if case is None else 'relevant case: ' + case}"
    
print("Test 8 passed")

# Test 9
# See if node sizes are updated correctly
for index, list in enumerate(after_removal_node_sizes_list):
    assert list == pj.after_removal_node_sizes_assert[index]\
        ,f"your node sizes aren't being updated correctly when you're removing nodes.\
            \nexpected output:{pj.after_removal_node_sizes_assert[index]}\
            \nyour output:\t{list}"

print("Test 9 passed")

print("############# All Tests passed! #############")