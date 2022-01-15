import sys

import webserver
import cli

opts = {
    "flags": {},
    "args": [],
}

def parseArgs(args):
    for arg in args:
        if len(arg) >= 2 and arg[0:2] == "--":
            opts["flags"][arg[2:]] = True
        else:
            opts["args"].append(arg) 

def main():
    parseArgs(sys.argv[1:])

    # Default to running as CLI
    if "webserver" in opts["flags"] == True:
        webserver.run()
    else:
        cli.run(opts)

main()
