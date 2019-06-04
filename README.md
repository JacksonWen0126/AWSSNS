# AWSSNS
Using boto3 framework on Python to call AWS SNS API to send message to users 
if pip is not installed on EC2 use: sudo easy_install pip;
 sudo pip install boto3

#Need to download keypair when creating EC2 instance on AWS console.
Change permission before connect to AWS using SSH. 
.pem using commend: chmod 400 'FileName'.pem

Connect to EC2 using putty or Terminal

ssh -i "['FileName'.pem]" ec2-user@ec2-52-87-211-112.compute-1.amazonaws.com #example command that you can find it on AWS console 
when you click "Connect" on EC2 serve.

