{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준9020","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyMsSCst8m1yNS9Gyj2dXcwx"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"fxo2w0a7ZMca"},"source":["# 골드바흐의 추측\n","\n","# prime list를 이용해서 짠 코드 (시간초과!)\n","def isPrime(num):\n","    if num == 1:\n","        return False\n","    for i in range(2,int(num**(1/2))+1):\n","        if num % i == 0:\n","            return False\n","    return True\n","\n","def primeList(num):\n","    p_list = []\n","    for i in range(2,num):\n","        if isPrime(i) == True:\n","            p_list.append(i)\n","    return p_list\n","\n","T = int(input())\n","for i in range(T):\n","    n = int(input())\n","    n_list = primeList(n)\n","    \n","    min_gap = n\n","    for j in range(len(n_list)):\n","        if n - n_list[j] in n_list:\n","            if min_gap > abs(n-2*n_list[j]):\n","                min_gap = abs(n-2*n_list[j])\n","                min1 = n_list[j]\n","                min2 = n-n_list[j]\n","\n","    print(min(min1,min2), max(min1,min2))"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"zODMUeTym3kO"},"source":["# list 사용없이\n","def isPrime(num):\n","    if num == 1:\n","        return False\n","    for i in range(2,int(num**(1/2))+1):\n","        if num % i == 0:\n","            return False\n","    return True\n","\n","T = int(input())\n","for i in range(T):\n","    n = int(input())\n","    \n","    for j in range(n//2):\n","        center = n//2\n","        front = center - j\n","        back = center + j\n","        if isPrime(front) and isPrime(back):\n","            print(front, back)\n","            break"],"execution_count":null,"outputs":[]}]}