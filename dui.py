#!/data/data/com.termux/files/usr/bin/python
import subprocess, sys

pkg0 = 'com.android.documentsui'
cls0 = 'com.android.documentsui.LauncherActivity'
pkg1 = "com.google.android.documentsui"
cls1 = "com.android.documentsui.files.FilesActivity"

def ams(duipkg):
    subprocess.run(['am', 'start', '-n', duipkg, '--activity-clear-task'], check=True)

if __name__ == '__main__':
    try:
        ams(f'{pkg0}/{cls0}')
    except Exception:
        try:
            ams(f'{pkg1}/{cls1}')
        except Exception as e:
            print(f"Failed to start DocumentsUI: {e}")
