{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준7785","provenance":[],"authorship_tag":"ABX9TyPgzry57PKAMWIQHpyLHeqw"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"UsxpK9StlVFw","executionInfo":{"status":"ok","timestamp":1628440663538,"user_tz":-540,"elapsed":13598,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"e3bf66c6-54e6-4b4f-9248-a873ff9023ca"},"source":["# 회사에 있는 사람\n","import sys\n","input = sys.stdin.readline\n","n = int(input())\n","in_out = {}\n","for _ in range(n):\n","    name, state = input().split()\n","    if state == 'enter':\n","        in_out[name] = 1\n","    else:\n","        in_out[name] = 0\n","for j in sorted((i for i,v in in_out.items() if v), reverse=True):\n","    print(j)"],"execution_count":21,"outputs":[{"output_type":"stream","text":["4\n","baha enter\n","askar enter\n","baha leave\n","artem enter\n","askar\n","artem\n"],"name":"stdout"}]}]}