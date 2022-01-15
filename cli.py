import core.core as core

def printUsage():
    usage = """
=== Cli Usage ===

python3 main.py [URL] [FLAGS]

"""
    print(usage)

def run(config):
    if "help" in config["flags"] or len(config["args"]) == 0:
        printUsage()
    else:
        core.getJson(config["args"][0])