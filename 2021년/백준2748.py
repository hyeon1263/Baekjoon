{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2748","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyMKhnj5IJ+K5OHWripUMzX9"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"UCNvyPA0SNZ9"},"source":["# 피보나치 수 2\n","fib = [0, 1]\n","\n","n = int(input())\n","if n < 2 :\n","    print(fib[n])\n","else:\n","    for i in range(2, n+1):\n","        fib.append(fib[i-2]+fib[i-1])\n","    print(fib[i])"],"execution_count":null,"outputs":[]}]}