{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1546","private_outputs":true,"provenance":[],"authorship_tag":"ABX9TyOSEkf7HlwVbD3nYT04kXQt"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"uxYzmabgAY27"},"source":["# 평균\n","N = int(input())\n","score = list(map(int, input().split()))\n","\n","sum = 0\n","for i in range(N):\n","    sum += score[i]/max(score)*100\n","print(sum/N)"],"execution_count":null,"outputs":[]}]}