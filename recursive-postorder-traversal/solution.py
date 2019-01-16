post_ordered_list = []


class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self):

        if self.left_child is not None and self.right_child is not None:
            self.left_child.postorder()
            self.right_child.postorder()
            post_ordered_list.append(self.data)
        else:
            if self.left_child is not None:
                self.left_child.postorder()
                post_ordered_list.append(self.data)
            elif self.right_child is not None:
                self.right_child.postorder()
                post_ordered_list.append(self.data)
            else:
                post_ordered_list.append(self.data)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data