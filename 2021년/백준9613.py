{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준9613","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyMNiD4E39i1ipzvjQLwHJsf"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"TnQ9gzcsJ1Yq"},"source":["# GCD 합\n","'''\n","def get_gcd(n1, n2):\n","    gcd = 1\n","    for i in range(1, min(n1, n2)+1):\n","        if (n1 % i == 0) and (n2 % i == 0):\n","            gcd = i\n","    return gcd\n","'''\n","def get_gcd(n1, n2): # 유클리드 호제법\n","    while n2:\n","        n1, n2 = n2, n1 % n2\n","    return n1\n","\n","T = int(input())\n","for i in range(T):\n","    N, *num_list = map(int, input().split())\n","    sum = 0\n","    for i in range(N-1):\n","        for j in range(1,N-i):\n","            sum += get_gcd(num_list[i], num_list[i+j])\n","    print(sum)"],"execution_count":null,"outputs":[]}]}