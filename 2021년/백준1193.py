{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1193.py","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyOkDH87aUyvK8TbWMBllknD"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"pbF33CaxUDzU"},"source":["# 분수 찾기\r\n","\r\n","X = int(input())\r\n","line = 1\r\n","\r\n","while X>line:\r\n","    X -= line\r\n","    line += 1\r\n","\r\n","if line % 2 == 0: # line이 짝수\r\n","    a = X\r\n","    b = line - X + 1\r\n","else :            # line이 홀수\r\n","    b = X\r\n","    a = line - X + 1\r\n","\r\n","print(a, b, sep='/')\r\n","\r\n","'''\r\n","홀수(x) 분자 : x --> 1 내림차순\r\n","        분모 : 1 --> x 오름차순\r\n","\r\n","짝수(y) 분자 : 1 --> y 오름차순\r\n","        분모 : y --> 1 내림차순\r\n","'''"],"execution_count":null,"outputs":[]}]}