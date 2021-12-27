{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2108","provenance":[],"authorship_tag":"ABX9TyO6j0nooWaNT29tCSDbIFHt"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"tUkgxUbTlNNE","executionInfo":{"status":"ok","timestamp":1630951589790,"user_tz":-540,"elapsed":8374,"user":{"displayName":"이상현","photoUrl":"","userId":"09000224211467185494"}},"outputId":"5a97e9f0-cd07-44c8-abb0-4f6a0bcdb9eb"},"source":["# 통계학\n","import sys\n","\n","N = int(sys.stdin.readline())\n","nums = []\n","for _ in range(N):\n","    num = int(sys.stdin.readline())\n","    nums.append(num)\n","\n","freq = []\n","for i in set(nums):\n","    freq.append((i, nums.count(i)))\n","\n","print(round(sum(nums)/len(nums)))\n","print(sorted(nums)[len(nums)//2])\n","sorted_freq = sorted(freq, key=lambda x:(-x[1], x[0]))\n","if sorted_freq[0][1] == sorted_freq[1][1]:\n","    print(sorted_freq[1][0])\n","else:\n","    print(sorted_freq[0][0])\n","print(max(nums)-min(nums))"],"execution_count":70,"outputs":[{"output_type":"stream","name":"stdout","text":["5\n","-1\n","-2\n","-3\n","-1\n","-2\n","-2\n","-2\n","-1\n","2\n"]}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"yeDDsr3KmFJG","executionInfo":{"status":"ok","timestamp":1630951251558,"user_tz":-540,"elapsed":383,"user":{"displayName":"이상현","photoUrl":"","userId":"09000224211467185494"}},"outputId":"b2ce8ff4-5546-49ae-d508-4fff5bdbc8b2"},"source":["nums = [4,3,3,4,2,3,1,3,2,2,2]\n","\n","freq = []\n","for i in set(nums):\n","    freq.append((i, nums.count(i)))\n","\n","sorted_freq = sorted(freq, key=lambda x:(-x[1], x[0]))\n","if sorted_freq[0][0] == sorted_freq[1][0]:\n","    print(sorted_freq[1][0])\n","else:\n","    print(sorted_freq[0][0])"],"execution_count":62,"outputs":[{"output_type":"execute_result","data":{"text/plain":["[(2, 4), (3, 4), (4, 2), (1, 1)]"]},"metadata":{},"execution_count":62}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"TYTMx6BISUKb","executionInfo":{"status":"ok","timestamp":1630951537737,"user_tz":-540,"elapsed":406,"user":{"displayName":"이상현","photoUrl":"","userId":"09000224211467185494"}},"outputId":"2f7f4ebd-d166-491d-a2d0-f4d65a390499"},"source":["max(nums)"],"execution_count":67,"outputs":[{"output_type":"execute_result","data":{"text/plain":["-1"]},"metadata":{},"execution_count":67}]}]}