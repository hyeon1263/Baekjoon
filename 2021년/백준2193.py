{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준2193","private_outputs":true,"provenance":[],"authorship_tag":"ABX9TyMZVN74k6q4EEjkghE9XLgn"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"UVLxTB78HG4w"},"source":["# 이친수\n","\n","n = int(input())\n","cnt = 0\n","a = [0,1]\n","\n","for i in range(n):\n","    a.append(a[i] + a[i+1])\n","\n","print(a[n])"],"execution_count":null,"outputs":[]}]}