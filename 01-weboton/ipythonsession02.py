# coding: utf-8
print(dir(s3))
elb_clnt = session.client('elb') 
elb_res = session.resource('elb') 
print(elb_clnt)
print(dir(elb_clnt))
for i in dir(elb_clnt):
    print(i)
    
ec2_clnt = session.client('ec2')
for i in enumerate(dir(elb_clnt)):
    print(i)
    
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession02 1-10')
