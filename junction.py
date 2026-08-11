"""Create directory junction (no admin needed)"""
import subprocess
import os

link = r'C:\Users\moyi\.claude\skills\kun-wisdom'
target = r'd:\project\人类经典品读\kun-wisdom'

# Remove existing if any
if os.path.exists(link):
    subprocess.run(['cmd', '/c', 'rmdir', link], shell=True)

# Create junction (mklink /J doesn't need admin)
result = subprocess.run(
    ['cmd', '/c', 'mklink', '/J', link, target],
    capture_output=True, text=True, shell=True
)
print('stdout:', result.stdout)
print('stderr:', result.stderr)
print('returncode:', result.returncode)

# Verify
print('exists after:', os.path.exists(link))
if os.path.exists(link):
    print('listdir:', os.listdir(link)[:5])
