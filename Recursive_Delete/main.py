import os

def handle_file(filelist, root_dir):
    rm_files = ["IMPORTANT.txt", "README.txt", "README.url"]
    for filename in filelist:
        if filename in rm_files:
            print(f"[+] Deleting {filename}")
            os.remove(os.path.join(root_dir, filename))

def handle_main(root_dir):
    total_files = []
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isfile(path):
            total_files.append(item)
        elif os.path.isdir(path):
            handle_main(path)
    if not total_files:
        print(f"[-] File not found")
    else:
        handle_file(total_files, root_dir)
            
def main():
    dir_path = os.path.expanduser(r"~/Telegram Desktop")
    handle_main(dir_path)

if __name__ == "__main__":
    print("[!] Started to look...")
    main()
    print("[+] Done!")