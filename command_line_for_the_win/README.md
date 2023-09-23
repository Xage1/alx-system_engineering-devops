Command line for the win Project for the ALX SE Programme 

Uploading Screenshots Using SFTP

To demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to upload screenshots to the sandbox environment, I followed these steps:

 Establish SFTP Connection:
   To connect to the sandbox environment,I used the SFTP command-line tool. I replaced `username`, `hostname`, and `password` with the credentials provided for the sandbox environment:

   sftp 5b3d7fe790dc@5b3d7fe790dc.b063733e.alx-cod.online

Navigate to Destination Directory:
Once connected, I navigated to the directory where I wanted to upload the screenshots. In my case, I needed to upload the screenshots to the /root/alx-system_engineering-devops/command_line_for_the_win/ directory on the remote server:

sftp> cd /root/alx-system_engineering-devops/command_line_for_the_win/
Upload Screenshots:
To upload the screenshots from my local machine to the sandbox environment, I used the put command. I specified the file path using forward slashes and included a space after the put command:

sftp> put C:/Users/Angy/OneDrive/Pictures/Screenshots/0-first_9_tasks.png
We repeated this step for each screenshot we wanted to upload.

Confirm Transfer:
To confirm that the screenshots were successfully transferred, I listed the contents of the remote directory using the ls command:
sftp> ls
We ensured that our screenshots were listed among the files in the remote directory
