import os
import sys

def handle_file(filelist, root_dir):
    rm_files = [] # Lists of files to delete
    print(f"[+] Deleting total {len(filelist)} files.")
    for filename in filelist:
        if filename in rm_files:
            print(f"[+] Deleting {filename}...", flush=True)
            sys.stdout.flush()
            os.remove(os.path.join(root_dir, filename))

def handle_dir(root_dir):
    total_files = []
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isfile(path):
            total_files.append(item)
        elif os.path.isdir(path):
            handle_dir(path)
    if not total_files:
        print(f"[-] File not found")
    else:
        handle_file(total_files, root_dir)
            
def main():
    dir_path = os.path.expanduser(rf'{sys.argv[1]}')
    handle_dir(dir_path)

if __name__ == "__main__":
    if not len(sys.argv) >= 2:
        print("[!] Argument not found!")
        print(f"[+] Usage: {__file__} <dir>")
        sys.exit(404)
    print("[!] Started to look...")
    main()
    print("[+] Done!")