{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1010","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNgn74aNq40xwhTI9kJ/qfW"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"kB829ALWpTsp"},"source":["# 다리 놓기\r\n","T = int(input())\r\n","for i in range(T):\r\n","    N, M = map(int, input().split())\r\n","    #c = mCn\r\n","    factorial, factorial_N, factorial_N1 = 1, 1, 1\r\n","    for x in range(M):\r\n","        factorial *= x+1\r\n","    for x in range(N):\r\n","        factorial_N *= x+1\r\n","    for x in range(M-N):\r\n","        factorial_N1 *= x+1\r\n","    c = factorial / (factorial_N*factorial_N1)\r\n","    print(int(c))"],"execution_count":null,"outputs":[]}]}