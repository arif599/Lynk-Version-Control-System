import os 
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lynk Version Control System CLI")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    add_parser = subparsers.add_parser("add", help="adding files")
    add_parser.add_argument("files", type=str, nargs="+", help = "enter one or more file names to add")

    snapshot_parser = subparsers.add_parser("snapshot", help="creating snapshots")
    snapshot_parser.add_argument("-m", "--message", type=str, required=True, help="the commit message")

    log_parser = subparsers.add_parser("log", help="snapshot logs")
    log_parser.add_argument("-d", "--detail", action="store_true", help="detailed logs")
    log_parser.add_argument("-s", "--simple", action="store_true", help="simple logs")

    push_parser = subparsers.add_parser("push", help="push files to remote repo")
    push_parser.add_argument("branch", type=str, help="the name of the branch to push")

    
    args = parser.parse_args()
    print(args)
