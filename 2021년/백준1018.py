{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"백준1018","private_outputs":true,"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNBl4P17bmDijAIyyfNTBM5"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"7zptMsXNzMAA"},"source":["# 체스판 다시 칠하기\r\n","board = []\r\n","N, M = map(int, input().split())\r\n","for i in range(N):\r\n","    row = list(input().split())\r\n","    board.append(row)\r\n","\r\n","x, y = 0, 0\r\n","cnt = 0\r\n","while 1:\r\n","    if y >= M-1:\r\n","        x += 1\r\n","        y = 0\r\n","        if x >= N-1:\r\n","            break      \r\n","    if (board[x][y] == 'B') and (board[x][y+1] == 'B'):\r\n","        board[x][y+1] = 'W'\r\n","    elif (board[x][y] == 'W') and (board[x][y+1] == 'W'):\r\n","        board[x][y+1] = 'B'\r\n","    elif (board[x][y] == 'W') and (board[x+1][y] == 'W'):\r\n","        board[x+1][y] = 'B'\r\n","    elif (board[x][y] == 'B') and (board[x+1][y] == 'B'):\r\n","        board[x+1][y] = 'W'\r\n","    y += 1\r\n","\r\n","for i in board:\r\n","    for j in i:\r\n","        print(j, end=' ')\r\n","    print()"],"execution_count":null,"outputs":[]}]}