this is automation map
i am going to use github, aws and python
start with makefile 
- inside makefile i create url storage, call the links and then save the file
-i called the other two file (two process json to csv and to clean the data by using import subprocess call)
Other thing i did was tocreate file converter json to csv and cleaning the data
go to aws, create a bucket by typing s3, make it public(ACLs enabled) 
then go to permissions and add the policy:AWS "CORS" code for allowing other services to read data in our bucket: https://bit.ly/knight-cors
then go to s3(bucket and create a folder) inflation folder, eave other difault settings 
open inflation folder click add files (inflation.csv) from download
click the file, on right top setting (object_action will drop down to make public by acls - click that) - will take you to make public window
on object info copy url
Amazon Web Services: Making a User Account for our Automation Bot 
Go to aws(screen console): search for iam - identity and access manager, then:
Go to the policy, create a policy, click json to: bit.ly/upload-policy or (access.json)file here -copy and paste policy (replace what is aws) and edit resource sentence by naming your s3 bucket (eg: gwaliwa_project) on both two sentence. Click next - then create policy.This will prompt you to policy name: write the name eg: mybucketuploadpolicy,then create a policy
From same IAM create a user, details addname: github-uploads >next _ click attach policy direct button then select mybucketpolicy you created previously - click its checkbox  > next create user

Github Action: 
Click on the repo - map_project> go to the settings > on the left menu go to secret and variables > actions>new repository secret > Name: AWS_S3_BUCKET secret(name ofbucket: gwaliwa-projects *need to check), > add secret button
Create another secret while on same map_project: Name: AWS_ACCESS_KEY_ID Secret(Go to aws-IAM-Users-username:github_upload(created previously)-go to security credentials> create and access key > check out application run outside aws >next >create access key> window pop up,copy access key and paste on secret : AWS_ACCESS_KEY_ID then click Add secret.
Click to add another secret: Name: AWS_SECRET_ACCESS_KEY : paste the one from github credentials- copy and paste there. Add secret


Useful command-line tools:

csvkit ... to manage and process CSVs: https://csvkit.readthedocs.io
jq ... to manage json files: https://jqlang.github.io/jq/
mapshaper ... to handle geospatial data: https://bit.ly/mapshaper-commands

IMF inflation by country: https://www.imf.org/external/datamapper/PCPIPCH@WEO/WEOWORLD?year=2023

IMF countries & regions: https://www.imf.org/external/datamapper/api/v1/countries


