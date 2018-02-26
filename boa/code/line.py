from byteplay3 import *

from boa.code import pyop


class Line(object):

    """

    """
    items = None

    def __init__(self, item_list):
        self.items = item_list

    @property
    def is_import(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if op in [pyop.IMPORT_NAME, pyop.IMPORT_FROM, pyop.IMPORT_STAR]:
                return True
        return False

    @property
    def is_constant(self):
        """

        :return:
        """
        is_correct_length = len(self.items) == 3 or len(self.items) == 5
        is_storing_constant = self.items[1][0] == pyop.LOAD_CONST and self.items[2][0] == pyop.STORE_NAME
        return is_correct_length and is_storing_constant

    @property
    def is_module_method_call(self):

        if not self.is_class:
            return self.items[-2][0] == pyop.CALL_FUNCTION and self.items[-1][0] == pyop.STORE_NAME
        return False

    @property
    def is_docstring(self):
        """
        returns whether a line is a docstring

        :return: whether a line is a documentation string
        :rtype: bool

        """
        for item in self.items:
            if item[0] == pyop.STORE_NAME and item[1] == '__doc__':
                return True
        return False

    @property
    def is_method(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if op == pyop.MAKE_FUNCTION:
                return True
        return False

    @property
    def is_class(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if op == pyop.LOAD_BUILD_CLASS:
                return True
        return False

    @property
    def code_object(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if type(arg) is Code:
                return arg
        return None

    @property
    def is_action_registration(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if arg == 'RegisterAction':
                return True

    @property
    def is_smart_contract_appcall_registration(self):
        """

        :return:
        """
        for i, (op, arg) in enumerate(self.items):
            if arg == 'RegisterAppCall':
                return True
