{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2920","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyP09o7jGUK+7S5e15a8q/DE"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"GwLuJlqNCuK0"},"source":["# 음계\n","\n","k = list(map(int, input().split()))\n","if k == sorted(k):\n","    print('ascending')\n","elif k == sorted(k, reverse=True):\n","    print('descending')\n","else:\n","    print('mixed')"],"execution_count":null,"outputs":[]}]}