print("**** HELPING YOU MAKE THE BASH SCRIPT ARRAY ****");
word=""
commandList=[];
while(word!="done"):
		word=input("Command to log: ");
		if(word!="done" and len(word)!=0 and commandList.count(word)==0):
			commandList.append(word);
			#print("len({}):{}".format(word,len(word)));
			#if(commandList.count(word)==0):
				#commandList.append(word);

print("commands=(",end="")
for command in commandList:
    print(" \"{}\"".format(command),end="");
print(" )",end="");
print("")

commandFile=open("commands.txt",'w',encoding='utf-8')

commandFile.write("commands=( ");
for command in commandList:
	commandFile.write("\"{}\" ".format(command))
commandFile.write(")");
commandFile.close();

print("DONE!");
