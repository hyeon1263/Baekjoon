{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2217","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyN6k2M2uMjyj559SbI/5tg0"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"uIZnVd3X-PxU","executionInfo":{"status":"ok","timestamp":1618403450755,"user_tz":-540,"elapsed":5546,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"407ed91b-54c6-4810-cf1b-8c23936e7fb5"},"source":["# 로프\n","\n","N = int(input())\n","rope_list = []\n","for i in range(N):\n","    rope = int(input())\n","    rope_list.append(rope)\n","rope_list.sort()\n","\n","max = rope_list[0] * N\n","for i in range(N):\n","    if max < rope_list[i] * (N-i):\n","    \n","print(max)"],"execution_count":7,"outputs":[{"output_type":"stream","text":["3\n","5\n","20\n","30\n","40\n"],"name":"stdout"}]}]}