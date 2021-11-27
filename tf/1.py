import subprocess
import os


path = "/Users/bytedance/honey/tf"

for i in range(4, 43):
    os.chdir(os.path.join(path, str(i), "contracts"))
    os.system("rm crowdsale.sol")
    os.system("mv " + str(i) + ".txt " + "crowdsale.sol")
    # os.system("mv " + str(i)+".txt " + str(i)+"/contracts/")