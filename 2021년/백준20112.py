{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준20112","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyOJFzg64pkrfTkncCJ0Ls7N"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"RCu-bph1S1vA","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1615988239682,"user_tz":-540,"elapsed":11064,"user":{"displayName":"S Hyeon lee","photoUrl":"","userId":"09000224211467185494"}},"outputId":"9a20e3c6-0caa-41b9-89d0-fcfffc33cb35"},"source":["# 사토르 마방진\r\n","\r\n","N = int(input())\r\n","\r\n","result = True\r\n","word = []\r\n","for i in range(N):\r\n","    x = input()\r\n","    word.append(x)\r\n","\r\n","for i in range(N):\r\n","    for j in range(N):\r\n","        if word[i][j] == word[j][i]:\r\n","            continue\r\n","        else:\r\n","            result = False\r\n","\r\n","if result == True:\r\n","    print('YES')\r\n","else:\r\n","    print('NO')"],"execution_count":8,"outputs":[{"output_type":"stream","text":["4\n","appl\n","ppap\n","padd\n","lpov\n","NO\n"],"name":"stdout"}]}]}