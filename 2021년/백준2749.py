{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2749","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyOW5aP6oueCoThtEtikqLZG"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"mTDfkPOfdXEb","executionInfo":{"status":"ok","timestamp":1626190333911,"user_tz":-540,"elapsed":1145,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"0fb92506-26a5-45a5-ffb4-f0ccbd42d148"},"source":["# 피보나치 수3\n","\n","n = int(input())\n","a = 0\n","b = 1\n","for i in range(n):\n","    a, b = b%1000000, (a+b)%1000000\n","print(a)"],"execution_count":null,"outputs":[{"output_type":"stream","text":["5\n","5\n"],"name":"stdout"}]}]}