{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준9205","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNWsqNVWc0FtrJyawPTHZkR"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"rxd-6n-PWyjG"},"source":["# 맥주 마시면서 걸어가기\n","T = int(input())\n","storeX = []\n","storeY = []\n","for i in range(T):\n","    cango = True\n","    N = int(input())\n","    from_x, from_y = map(int, input().split()) # 출발 지점\n","    for i in range(N):\n","        store_x, store_y = map(int, input().split()) # 편의점 좌표\n","        storeX.append(store_x)\n","        storeY.append(store_y)\n","    to_x, to_y = map(int, input().split())  # 도착 지점\n","    \n","    while 1:\n","        min_value = abs(from_x - storeX[0])+abs(from_y - storeY[0])\n","        min_index = 0\n","        for i in range(len(storeX)):\n","            if min_value > abs(from_x-storeX[i])+abs(from_y-storeY[i]):\n","                min_index = i\n","        if abs(from_x-storeX[min_index])+abs(from_y-storeY[min_index]) > 1000:\n","            cango = False\n","        \n","        from_x = storeX[min_index]\n","        from_y = storeY[min_index]\n","        storeX.remove(storeX[min_index])\n","        storeY.remove(storeY[min_index])\n","        if len(storeX) == 0:\n","            break\n","       \n","    if abs(from_x-to_x) + abs(from_y-to_x) > 1000:\n","        cango = False\n","    \n","    if cango == True:\n","        print('happy')\n","    else:\n","        print('sad')"],"execution_count":null,"outputs":[]},{"cell_type":"code","metadata":{"id":"fh_rViI9l1ix"},"source":[""],"execution_count":null,"outputs":[]}]}