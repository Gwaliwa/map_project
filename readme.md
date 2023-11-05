this is automation map
i am going to use github, aws and python
start with makefile 
- inside makefile i create url storage, call the links and then save the file
-i called the other two file (two process json to csv and to clean the data by using import subprocess call)
Other thing i did was tocreate file converter json to csv and cleaning the data
go to aws, create a bucket by typing s3, make it public(ACLs enabled) 
then go to permissions and add the policy:AWS "CORS" code for allowing other services to read data in our bucket: https://bit.ly/knight-cors