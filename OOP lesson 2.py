# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#     def __init__(self, first , last , pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email =first + '.' + last + '@gmail.com'
#
#         Employee.num_of_emps += 1
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# print(Employee.num_of_emps)
#
# emp_1 = Employee('john', 'doe', 50000)
# emp_2 = Employee('Jon','Jones', 100000)
# print(Employee.num_of_emps)
# print(Employee.raise_amount)



def intersection():
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    min_list = min(nums1 , nums2 , key = len )
    max_list = max(nums1 , nums2 , key = len )
    res = set()
    for i in max_list:
        if i in min_list:
            res.add(i)
    print(res)
intersection()

