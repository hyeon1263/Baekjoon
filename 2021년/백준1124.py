{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1124","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyPnux71lMOE6zS0+HiS8FwU"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"wXsP-DuvVSZw"},"source":["# 언더프라임\n","def num_factor(n):    # 소인수의 개수를 반환\n","    cnt = 0\n","    for i in range(2,int(n**(1/2))+1):\n","        if n == 1:\n","            break\n","        while n % i == 0:\n","            n = n//i\n","            cnt += 1\n","    return cnt\n","        \n","def is_prime(n):    # 소수 판별\n","    if n == 1:\n","        return False\n","    if n == 2:\n","        return True\n","    for i in range(2,int(n**(1/2)+1)):\n","        if n % i == 0:\n","            return False\n","    return True\n","\n","A, B = map(int, input().split())\n","count = 0\n","for i in range(A,B+1):\n","    if is_prime(i) == True:\n","        continue\n","    if is_prime(num_factor(i)) == True:\n","        count += 1\n","print(count)"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"TN63ewJTxNsD","executionInfo":{"status":"ok","timestamp":1627238715309,"user_tz":-540,"elapsed":3090,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"51926480-0e35-44a4-85f8-8655f0376bd4"},"source":["def num_factor(n):    # 소인수의 개수를 반환\n","    cnt = 0\n","    num = 2\n","    while n > 1:\n","        if n % num == 0:\n","            n = n//num\n","            cnt += 1\n","        else:\n","            num += 1\n","    return cnt\n","\n","def is_prime(n):    # 소수 판별\n","    primes = [False, False, True] + [True]*(n-2)\n","    for i in range(2, int(n**(1/2))+1):\n","        if primes[i]:\n","            for j in range(2*i, n+1, i):\n","                primes[j] = False\n","    return primes[n]\n","\n","\n","A, B = map(int, input().split())\n","primes = [False, False, True] + [True]*(B-2)\n","for i in range(2, B+1):\n","    if primes[i]:\n","        for j in range(2*i, B+1, i):\n","            primes[j] = False\n","\n","count = 0\n","for i in range(A,B+1):\n","    if primes[i]:\n","        continue\n","    else:\n","        if primes[num_factor(i)]:\n","            count += 1\n","print(count)"],"execution_count":89,"outputs":[{"output_type":"stream","text":["2 12000\n","7662\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"PXOCkeAo5d6G","executionInfo":{"status":"ok","timestamp":1627238288522,"user_tz":-540,"elapsed":259,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"a17a6dfd-ca05-4509-d015-cf48d1bd703c"},"source":["def is_prime(n):    # 소수 판별\n","    primes = [False, False, True] + [True]*(n-2)\n","    for i in range(2, n+1):\n","        if primes[i]:\n","            for j in range(2*i, n+1, i):\n","                primes[j] = False\n","    return [i for i in range(n) if primes[i]]\n","\n","is_prime(8)"],"execution_count":77,"outputs":[{"output_type":"execute_result","data":{"text/plain":["[2, 3, 5, 7]"]},"metadata":{"tags":[]},"execution_count":77}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"t4YV96897i2P","executionInfo":{"status":"ok","timestamp":1627237868196,"user_tz":-540,"elapsed":242,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"78435e5c-9745-4493-f966-316c82df9dd6"},"source":["def is_prime(n):    # 소수 판별\n","    primes = [False, False, True] + [True]*(n-2)\n","    for i in range(2, int(n**(1/2))+1):\n","        if primes[i]:\n","            for j in range(2*i, n+1, i):\n","                primes[j] = False\n","    return primes[n]\n","\n","is_prime(14)"],"execution_count":70,"outputs":[{"output_type":"execute_result","data":{"text/plain":["False"]},"metadata":{"tags":[]},"execution_count":70}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ohBeAbhl9r_4","executionInfo":{"status":"ok","timestamp":1627238708903,"user_tz":-540,"elapsed":4236,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"c74c9238-2589-4ccc-e211-c4973e866a3c"},"source":["import math\n","def is_prime_number(n):\n","    array = [True for i in range(n+1)]\n","\n","    for i in range(2, int(math.sqrt(n)) + 1):\n","        if array[i] == True:\n","            j=2\n","            while i * j <= n:\n","                array[i * j] = False \n","                j += 1 \n","    return [ i for i in range(2, n+1) if array[i] ]\n","\n","A,B = map(int, input().split())\n","primes = is_prime_number(B)\n","result = []\n","for i in range(A,B+1):\n","    if i in primes:\n","        continue\n","    else:\n","        num = 2\n","        cnt = 0\n","        while i > 1:\n","            if i % num == 0:\n","                i = i//num\n","                cnt += 1\n","            else:\n","                num += 1\n","        result.append(cnt)\n","cnt = 0\n","for i in result:\n","    if i in primes:\n","        cnt+= 1\n","print(cnt)"],"execution_count":88,"outputs":[{"output_type":"stream","text":["2 12000\n","7662\n"],"name":"stdout"}]}]}