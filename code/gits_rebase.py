import subprocess
from subprocess import PIPE


def gits_rebase(args):
    print(args)
    print("Hello from GITS command line tools- Rebase")
    try:
        print("Is the rebase on current branch?")
        inp = input("[yes/no][y/n]")
        if inp.lower() == "yes" or inp.lower() == "y":
            process1 = subprocess.Popen(['git', 'rebase', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout)
            print(stderr)
        else:
            inp2 = input("Enter the name of the branch you want to rebase")
            # print(inp2)
            process2 = subprocess.Popen(['git', 'checkout', inp2, 'git', 'rebase', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process2.communicate()
            print(stdout)
            print(stderr)
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
