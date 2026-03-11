# src/utils/setup_colab.py

def setup_repository(repo_name="Cyberbullying-Detection-in-Bilingual-English-Spanish-Text-A-Comparative-Study-"):
    from google.colab import drive
    import os
    import sys
    import subprocess

    # Mount Drive
    drive.mount('/content/drive')

    # Repository paths
    repo_path = f"/content/drive/MyDrive/{repo_name}"

    # Clone or pull (use subprocess instead of ! magic)
    if not os.path.exists(repo_path):
        subprocess.run(
            f"cd /content/drive/MyDrive && git clone https://github.com/YusrahS/{repo_name}",
            shell=True, check=True
        )
        print("✅ Repository cloned")
    else:
        subprocess.run(f"cd {repo_path} && git pull", shell=True, check=True)
        print("✅ Repository updated")

    # Create symlink (use subprocess instead of ! magic)
    subprocess.run(f"rm -f /content/{repo_name}", shell=True)
    subprocess.run(f"ln -sf {repo_path} /content/{repo_name}", shell=True)

    # Add to path
    if f'/content/{repo_name}' not in sys.path:
        sys.path.append(f'/content/{repo_name}')

    # Change directory (use os.chdir instead of %cd magic)
    os.chdir(f'/content/{repo_name}')

    print(f"\n✅ Ready to work in {os.getcwd()}")
    return True
