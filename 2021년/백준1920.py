{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1920","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNeKRB1iXowAUBDy+Q6VR/9"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"6NDrJREm1Qj7"},"source":["# 수 찾기\n","from collections import defaultdict\n","\n","N = int(input())\n","A = defaultdict(int)\n","for i in map(int, input().split()):\n","    A[i] = 1\n","M = int(input())\n","for i in map(int, input().split()):\n","    if A[i] == 1:\n","        print(1)\n","    else:\n","        print(0)"],"execution_count":null,"outputs":[]}]}