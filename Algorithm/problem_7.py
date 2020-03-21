# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.is_route = False
        self.handler = handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler_, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler_)
        self.not_found_handler = not_found_handler

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for word in path_list:
            if not current_node.children.get(word):
                current_node.children[word] = RouteTrieNode()
            current_node = current_node.children[word]
        current_node.is_route = True
        current_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for word in path_list:
            if word == "":
                return current.handler
            if word not in current.children:
                return self.not_found_handler
            else:
                current = current.children[word]
        if current.handler == None:
            return self.not_found_handler
        return current.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if self.route_trie.find(path_list) == None:
            return self.route_trie.not_found_handler
        return self.route_trie.find(path_list)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')[1:]

router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/product", "product handler")
router.add_handler("/home/product/1", "product_1 handler")

# some lookups with the expected output
print(router.lookup("")) # should print root handler
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/product/")) # should print product handler
print(router.lookup("/home/product/1")) # should print product_1_handler
