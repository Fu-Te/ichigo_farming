import subprocess

#pip install -r requirements.txt 必要なパッケージの一括インストール
def install_package():
    subprocess.run(['pip','install','-r','requirements.txt'])
    
install_package()