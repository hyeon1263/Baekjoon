{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준7770","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyOjyIO+ChGHohWzzy6x8HBn"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"J-dUxl0sQTZ6"},"source":["# 아즈텍 피라미드\r\n","'''  1+3+5+7+9+11+9+7+5+3+1 = 61 -> 바닥 -20\r\n","    +1+3+5+7+9+7+5+3+1 =     41 2층 -16\r\n","    +1+3+5+7+5+3+1 =        25 3층 -12\r\n","    +1+3+5+3+1 =          13 4층  -8\r\n","    +1+3+1 =             5 5층 --4\r\n","    +1 =                1''' # 꼭대기\r\n","n = int(input())\r\n","cnt = 0 #층 수\r\n","sum = 1 # 바닥층의 개수\r\n","sum_0 = sum # 총 상자 개수\r\n","i = 4\r\n","while sum_0 <= n:\r\n","    sum += i\r\n","    sum_0 += sum\r\n","    cnt += 1\r\n","    i += 4\r\n","print(cnt)"],"execution_count":null,"outputs":[]}]}