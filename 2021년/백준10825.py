{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준10825","provenance":[],"authorship_tag":"ABX9TyMcd7Fy1PziUxLG9Vmz5KBs"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"SdCX7q48Cd1s","executionInfo":{"status":"ok","timestamp":1629641817254,"user_tz":-540,"elapsed":50045,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"1f92667e-6009-4444-ba03-2dc802eba00a"},"source":["# 국영수\n","import sys\n","\n","scores = []\n","N = int(input())\n","for _ in range(N):\n","    name, kor, eng, math = sys.stdin.readline().split()\n","    scores.append([name, int(kor), int(eng), int(math)])\n","\n","for i in sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0])):\n","    print(i[0])"],"execution_count":27,"outputs":[{"output_type":"stream","text":["12\n","Junkyu 50 60 100\n","Sangkeun 80 60 50\n","Sunyoung 80 70 100\n","Soong 50 60 90\n","Haebin 50 60 100\n","Kangsoo 60 80 100\n","Donghyuk 80 60 100\n","Sei 70 70 70\n","Wonseob 70 70 90\n","Sanghyun 70 70 80\n","nsj 80 80 80\n","Taewhan 50 60 90\n","Donghyuk\n","Sangkeun\n","Sunyoung\n","nsj\n","Wonseob\n","Sanghyun\n","Sei\n","Kangsoo\n","Haebin\n","Junkyu\n","Soong\n","Taewhan\n"],"name":"stdout"}]}]}