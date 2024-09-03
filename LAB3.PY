# REQ - 1 : Create dictionary
emp = {'ename':['hari','thomas','raj','laksh','subha'],'age':[21,22,23,25,30],'salary':[25000,30000,32000,35000,19000]}
print("The Employee datase is:",emp)
print("The Employee salaries are:",emp)
print(emp['salary'])
print("The salaries are:")
for v in emp['salary']:
    print(v)
L1= emp['salary']
print("The listed salaries:",L1)
print("The sorted salaries are:",sorted(L1))
print("The reversed salaries:",L1[::-1])
print("The minimum salary is:",min(L1))
print("The maximum salary is:",max(L1))
print("The total salary is:",sum(L1))
