import os
dir(os)

# help(os)
x = os.system("ls -l")

os.system("pwd")
os.getpwd()
os.chdir("/tmp")
os.listdir()
os.listdir("/etc")

# to create a new file
os.mknod("thisIsMyTestFile")
os.listdir()

# make directory
os.makedirs("test1/test2")
os.listdir()

for i in listdir():
    print(i)


os.environ
os.environ.get("OLDPWD")

os.getuid()
os.getgid()

os.rmdir("testDirOs")
os.listdir()

os.rmdirs("test1/test2")

os.rename("myfile1" "myfile")

####################### second part

dir(os.path)
os.path.exists("/etchosts")
os.path.exists("/etc/hostssss")
os.path.isfile("/etc/hosts")
os.path.isfile("/etc/hostssss")
os.path.isdir("/etc/hostssssss")
os.path.isdir("/etc")
os.path.islink("/etc/rc0.d")
ls -l /etc/rc0.d
os.path.islink("/etc/rc0.d/K0lspice-vdagent")
os.path.getsize("/etc/hosts")

os.path.basename("/etc/hosts")
os.path.dirname("etc/hosts")

os.path.join("/home", "testfile")
"home" + "/" + "testfile"

os.walk("/etc/tuned")
list(os.walk("/etc/tuned"))

list(os.walk("/etc/grub.d"))

###################################

import os

for dirname, dirpath, filename in os.walk("/home/saber/PycharmProjects/python/python_os_walk"):
    print(dirname)
    for file in filename:
        print(os.path.join(dirname, file))

###################################

