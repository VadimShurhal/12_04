# os.popen
# os.spawn
# os.system


"""
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False,
               shell=False, cwd=None, timeout=None, check=False, encoding=None,
               errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)¶
"""
import subprocess

command = subprocess.run('Docker ps -a',
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         encoding='utf-8'
                         )

if command.returncode == 0:
    print("All good !")
    print(command.stdout)
else:
    print(command.stderr)