2025-04-21T17:43:50.6458556Z ##[debug]Evaluating condition for step: 'Run main.py'
##[debug]Evaluating: success()
##[debug]Evaluating success:
##[debug]=> true
##[debug]Result: true
##[debug]Starting: Run main.py
##[debug]Loading inputs
##[debug]Loading env
Run python main.py
##[debug]/usr/bin/bash -e /home/runner/work/_temp/9ab88792-b10c-43ba-9bcb-47c2ca335157.sh
Traceback (most recent call last):
  File "/home/runner/work/Shreealgo/Shreealgo/main.py", line 9, in <module>
    credentials = Credentials.from_service_account_file("credentials.json", scopes=scope)
  File "/opt/hostedtoolcache/Python/3.10.17/x64/lib/python3.10/site-packages/google/oauth2/service_account.py", line 260, in from_service_account_file
    info, signer = _service_account_info.from_filename(
  File "/opt/hostedtoolcache/Python/3.10.17/x64/lib/python3.10/site-packages/google/auth/_service_account_info.py", line 78, in from_filename
    with io.open(filename, "r", encoding="utf-8") as json_file:
FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'
Process completed with exit code 1.
##[debug]Finishing: Run main.py

