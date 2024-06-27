print("SCP HELPER APP");
print("-"*68);
print("This helps create an SCP command to pull a file off a remote server");
print("-"*68);
# This helps pull a file off a server when needed
# SCP is an odd duck and can be difficult to construct the command under pressure.
# Intended Use: pull a file from a remote (Linux) Server from a Windows PC via PowerShell 

# 
remoteServerUsername=input("Username on remote server: ").strip();
# 
remoteServer=input("Server Name / IP: ").strip();
#  (optional - and for intended use not required (port 22))
port=input("Port (if applicable): ").strip();
# 
sourceLocation=input("Full Path to file on Source: ").strip();
# 
destinationLocation=input("Full Path to file on Destination: ").strip();
# 
fileNameOnSource=input("file name: ").strip();
#this is mainly for remote hosts on VirtualBox 

if(port!=""):
    # scp -p (port number) username@server:path/filename destPath/filename
    print(f"scp -P {port} {remoteServerUsername}@{remoteServer}:{sourceLocation}/{fileNameOnSource} {destinationLocation}/{fileNameOnSource}");
else:
    print(f"scp {remoteServerUsername}@{remoteServer}:{sourceLocation}/{fileNameOnSource} {destinationLocation}/{fileNameOnSource}");
