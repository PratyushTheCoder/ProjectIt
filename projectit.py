from os import path, getcwd, chdir, mkdir, system, chroot
from sys import exit, argv
import json

if path.exists(getcwd() + "/projectit.json"):
    with open("./projectit.json") as f:
        config=json.load(f)
        defdir=config['defdir']
        defgit=config['defgit']
        defedi=config['defedi']
        f.close()

else:
    print("ProjectIt configration file not found creating one...")
    defdir=input("Please enter the default dir for your projects: ")
    defgit=input("Would you like to create a git repo in a new project by default(Yes): ")
    defedi=input("Please state the command for your favorite editor(code): ")
    if defgit=="":
        defgit="yes"
    else:
        defgit="no"
    if defedi=="":
        defedi="code"
    else:
        pass
    configTemplate={"version":"0.0.1 ALPHA","defdir":defdir,"defgit":defgit,"defedi":defedi}
    with open(getcwd() + "/projectit.json", "w+") as f:
        json.dump(configTemplate,f) 
        f.close()
    print("Please restart the app to load configration files")
    exit(0)

argv.remove(argv[0])

git_init=[
    "git init",
    "git add .",
    'git commit -m "initial commit"'
]

def projectit(mode):
    try:
        if mode=="def":
            chdir(defdir)
                
        else:
            project_path=input("Please enter the project path: ")
            chdir(project_path)

        project_name=input("Please enter the project name(new_project): ")
        if project_name=="":
            project_name="new_project"
        else:
            pass
        mkdir(project_name)
        chdir(project_name)
        if defgit=="no":
            git_choice=input("Do you want to initialized a git repository(no): ")
            if git_choice=="yes":
                for command in git_init:
                    system(command)
        else:
            for command in git_init:
                system(command)
        print("Opening editor")
        system(f'{defedi} .') 
    except Exception as e:
        chdir(defdir)
        with open("./projectit.log", "w+") as f:
            f.write(f'{e}\n')
            f.close()
            print("\nError occured")
            exit(1)


if len(argv)!=0:
    for i in argv:
        if "def" in i:
            projectit("def")
        else:
            projectit("")
else:
    projectit("")
        


