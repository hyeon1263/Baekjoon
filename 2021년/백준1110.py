{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1110","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyODiSpS/dtbGrVitbYDkMm6"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"Ozq14K5dt2DM"},"source":["# 더하기 사이클\r\n","\r\n","n = int(input())\r\n","cnt = 1\r\n","\r\n","t10 = n // 10\r\n","t1 = n % 10\r\n","m = t10 + t1\r\n","t = t1*10 + m%10\r\n","\r\n","while n != t:\r\n","    t10 = t // 10\r\n","    t1 = t % 10\r\n","    m = t10 + t1\r\n","    t = t1*10 + m%10\r\n","    cnt += 1\r\n","\r\n","print(cnt)"],"execution_count":null,"outputs":[]}]}