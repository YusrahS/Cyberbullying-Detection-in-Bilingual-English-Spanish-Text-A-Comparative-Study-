#to set up drive and github
def setup_repository(repo_name="Cyberbullying-Detection-in-Bilingual-English-Spanish-Text-A-Comparative-Study-"):
    from google.colab import drive
    import os
    import sys
    
    # Mount Drive
    drive.mount('/content/drive')
    
    # Repository paths
    repo_path = f"/content/drive/MyDrive/{repo_name}"
    
    # Clone or pull
    if not os.path.exists(repo_path):
        !cd /content/drive/MyDrive/ && git clone https://github.com/YusrahS/{repo_name}
        print("✅ Repository cloned")
    else:
        !cd {repo_path} && git pull
        print("✅ Repository updated")
    
    # Create symlink
    !rm -f /content/{repo_name}
    !ln -sf {repo_path} /content/{repo_name}
    
    # Add to path
    if f'/content/{repo_name}' not in sys.path:
        sys.path.append(f'/content/{repo_name}')
    
    # Change directory
    %cd /content/{repo_name}
    
    print(f"\n✅ Ready to work in {os.getcwd()}")
    return True
