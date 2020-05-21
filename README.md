# Real time object detection from videos of recorded by rasperberry-pi cam

The folder scripts contain python programs that run on both raspberry-pi and AWS controller instance. 

Separate utility python modules are created for connecting to and interacting with various AWS services like S3, SQS and EC2 instances. 

# Running the application 

A main controller EC2 instance must be provisioned that is programmed to run the controller.py script continuously and is responsible for allocating new EC2 instances or restarting idle/stopped instances. In a nutshell it takes care of the auto-scaling of the entire application.

Raspberry-pi must be loaded with all the needed scripts for video recording, uploading and processing request from SQS queue. 
