{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2750","provenance":[],"authorship_tag":"ABX9TyNSN5IxxK2TZF4PeQhKCVrC"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/","height":238},"id":"09T9RbZN7Rpb","executionInfo":{"status":"error","timestamp":1634535973284,"user_tz":-540,"elapsed":348,"user":{"displayName":"이상현","photoUrl":"https://lh3.googleusercontent.com/a/default-user=s64","userId":"09000224211467185494"}},"outputId":"9b460cf3-ce76-469f-b475-22d1cc005e5f"},"source":["# 수 정렬하기\n","\n","import sys\n","\n","numbers = []\n","N = int(input())\n","for _ in range(N):\n","    numbers.append(int(sys.stdin.readline()))\n","for i in sorted(numbers):\n","    print(i)"],"execution_count":3,"outputs":[{"output_type":"error","ename":"ValueError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)","\u001b[0;32m<ipython-input-3-18f4aae199ed>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mnumbers\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mN\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mN\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0mnumbers\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"]}]}]}