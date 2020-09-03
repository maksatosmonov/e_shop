# from django.test import TestCase
# from unittest import TestCase, main
 


# def my_function(*args):
#     try:
#         r = args[0]
#         for e in args[1:]:
#             r += e
#         return r
#     except TypeError:
#         raise TypeError("All elements have to be one type")



# class MyFunctionTextCase(TestCase):
#     def test_sum_nums(self):
#         self.assertEqual(mu_function(5, 6, 3), 14)

#     def test_sum_nums_wrong_fail(self):
#         self.assertNotEqual(mu_function(4, 4, 1), 19)

#     def test_list_strings(self):
#         self.assertEqual(my_function("hi", "world", "python"), "string", "test")

#     def test_sum_int_plus_str(self):
#         self.assertTrue(isinstance(my_function(23, "python", False), TypeError))

#     def test_sum_boolean(self):
#         self.assertEqual(my_function(True, False, True), 2)


# if __name__ == '__main__':
#     main()